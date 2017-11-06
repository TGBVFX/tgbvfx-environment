import os
import shutil
import ctypes
from ctypes import POINTER, WinError
from ctypes.wintypes import DWORD, HANDLE, BOOL

import pyblish.api
import filelink
import clique


LPDWORD = POINTER(DWORD)

GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000

FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004

FILE_SUPPORTS_HARD_LINKS = 0x00400000
FILE_SUPPORTS_REPARSE_POINTS = 0x00000080

FILE_ATTRIBUTE_DIRECTORY = 0x00000010
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400

FILE_FLAG_OPEN_REPARSE_POINT = 0x00200000
FILE_FLAG_BACKUP_SEMANTICS = 0x02000000

OPEN_EXISTING = 3

MAX_PATH = 260

INVALID_HANDLE_VALUE = -1


class FILETIME(ctypes.Structure):
    _fields_ = [("dwLowDateTime", DWORD),
                ("dwHighDateTime", DWORD)]


class BY_HANDLE_FILE_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("dwFileAttributes", DWORD),
        ("ftCreationTime", FILETIME),
        ("ftLastAccessTime", FILETIME),
        ("ftLastWriteTime", FILETIME),
        ("dwVolumeSerialNumber", DWORD),
        ("nFileSizeHigh", DWORD),
        ("nFileSizeLow", DWORD),
        ("nNumberOfLinks", DWORD),
        ("nFileIndexHigh", DWORD),
        ("nFileIndexLow", DWORD)
    ]


# http://msdn.microsoft.com/en-us/library/windows/desktop/aa363858
CreateFile = ctypes.windll.kernel32.CreateFileW
CreateFile.argtypes = [ctypes.c_wchar_p, DWORD, DWORD, ctypes.c_void_p,
                       DWORD, DWORD, HANDLE]
CreateFile.restype = HANDLE

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa364944
GetFileAttributes = ctypes.windll.kernel32.GetFileAttributesW
GetFileAttributes.argtypes = [ctypes.c_wchar_p]
GetFileAttributes.restype = DWORD

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa364952
GetFileInformationByHandle = ctypes.windll.kernel32.GetFileInformationByHandle
GetFileInformationByHandle.argtypes = [
    HANDLE, POINTER(BY_HANDLE_FILE_INFORMATION)
]
GetFileInformationByHandle.restype = BOOL

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa364996
GetVolumePathName = ctypes.windll.kernel32.GetVolumePathNameW
GetVolumePathName.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p, DWORD]
GetVolumePathName.restype = BOOL

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa364993
GetVolumeInformation = ctypes.windll.kernel32.GetVolumeInformationW
GetVolumeInformation.argtypes = [
    ctypes.c_wchar_p, ctypes.c_wchar_p, DWORD, LPDWORD, LPDWORD, LPDWORD,
    ctypes.c_wchar_p, DWORD
]
GetVolumeInformation.restype = BOOL

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa363216
DeviceIoControl = ctypes.windll.kernel32.DeviceIoControl
DeviceIoControl.argtypes = [HANDLE, DWORD, ctypes.c_void_p, DWORD,
                            ctypes.c_void_p, DWORD, LPDWORD, ctypes.c_void_p]
DeviceIoControl.restype = BOOL

# http://msdn.microsoft.com/en-us/library/windows/desktop/ms724211
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL


def getfileinfo(path):
    """
    Return information for the file at the given path. This is going to be a
    struct of type BY_HANDLE_FILE_INFORMATION.
    """
    hfile = CreateFile(
        path, GENERIC_READ, FILE_SHARE_READ, None, OPEN_EXISTING, 0, None
    )
    if hfile is None:
        raise WinError()
    info = BY_HANDLE_FILE_INFORMATION()
    rv = GetFileInformationByHandle(hfile, info)
    CloseHandle(hfile)
    if rv == 0:
        raise WinError()
    return info


def samefile(path1, path2):
    """
    Returns True if path1 and path2 refer to the same file.
    """
    # Check if both are on the same volume and have the same file ID
    info1 = getfileinfo(path1)
    info2 = getfileinfo(path2)
    return (info1.dwVolumeSerialNumber == info2.dwVolumeSerialNumber and
            info1.nFileIndexHigh == info2.nFileIndexHigh and
            info1.nFileIndexLow == info2.nFileIndexLow)


class TGBFtrackManageComponentData(pyblish.api.InstancePlugin):
    """Manage the data of the Ftrack components."""

    order = pyblish.api.IntegratorOrder + 1
    label = "Manage Data"
    families = ["ftrack"]

    def manage_data(self, src, dst):
        try:
            filelink.create(src, dst)
            self.log.debug("Linking: \"{0}\" to \"{1}\"".format(src, dst))
        except WindowsError as e:
            if e.winerror == 17:
                self.log.warning(
                    "File linking failed due to: \"{0}\". "
                    "Resorting to copying instead.".format(e)
                )
                shutil.copy(src, dst)
            else:
                raise e

    def process(self, instance):

        for data in instance.data.get("ftrackComponentsList", []):

            location = data.get(
                "component_location",
                instance.context.data["ftrackSession"].pick_location()
            )
            if location["name"] == "ftrack.server":
                continue

            component = data.get("component", None)
            if not component:
                continue

            # Create destination directory
            resource_identifier = location.get_resource_identifier(component)
            if not os.path.exists(os.path.dirname(resource_identifier)):
                os.makedirs(os.path.dirname(resource_identifier))

            collection = instance.data.get("collection", None)
            if collection:
                target_collection = clique.parse(
                    resource_identifier,
                    pattern="{head}{padding}{tail}"
                )

                for f in collection:
                    dst = f.replace(collection.head, target_collection.head)

                    # If the files are the same, continue
                    if os.path.exists(dst) and samefile(f, dst):
                        self.log.debug(
                            "\"{0}\" is the same as \"{1}\". "
                            "Skipping...".format(f, dst)
                        )
                        continue

                    # Delete existing files if overwriting.
                    if data.get("component_overwrite", False):
                        if os.path.exists(dst):
                            os.remove(dst)

                    if not os.path.exists(dst):
                        self.manage_data(f, dst)

            output_path = instance.data.get("output_path", "")
            if output_path:

                # If the files are the same, continue
                if (os.path.exists(resource_identifier) and
                   samefile(output_path, resource_identifier)):
                    self.log.debug(
                        "\"{0}\" is the same as \"{1}\". "
                        "Skipping...".format(output_path, resource_identifier)
                    )
                    return

                # Delete existing file if overwriting
                if data.get("component_overwrite", False):
                    if os.path.exists(resource_identifier):
                        os.remove(resource_identifier)

                if not os.path.exists(resource_identifier):
                    self.manage_data(output_path, resource_identifier)
