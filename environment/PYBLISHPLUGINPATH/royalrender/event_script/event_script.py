import sys
import os
import argparse
import struct

# Setup arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--event-type",
    action="store",
    default="",
    dest="event-type"
)
parser.add_argument(
    "--event-script",
    action="store",
    default="",
    dest="event-script"
)
parser.add_argument(
    "--job-id",
    action="store",
    default="",
    dest="job-id"
)
args = parser.parse_args()
results = vars(args)


def findRR_Root():
    # findRR_Root adds the RR path as search path for the module
    # This function will only work if RR was installed on the machine
    # If you are using it from an external machine, you have to add the path
    # to the rrPy module yourself sys.path.append(MyModulePath)
    if "RR_ROOT" not in os.environ:
        return
    modPath = os.environ["RR_ROOT"]
    is64bit = (struct.calcsize("P") == 8)
    if (sys.platform.lower() == "win32"):
        if (is64bit):
            modPath = modPath + "/bin/win64"
        else:
            modPath = modPath + "/bin/win"
        modPath = modPath.replace("\\", "/")
    elif (sys.platform.lower() == "darwin"):
        if (is64bit):
            modPath = modPath + "/bin/mac64/lib/python/27"
        else:
            modPath = modPath + "/bin/mac/lib/python/27"
    else:
        modPath = modPath + "/bin/lx64/lib"
    modPath = modPath.replace("_debug", "_release")
    sys.path.append(modPath)
    print("added module path "+modPath)


findRR_Root()
import libpyRR2 as rrLib

print("Set up server and login info.")
# A login is required if you have enabled
# "Auth required for all connections" in rrConfig tab rrLogin
# Or if you connect via an router (router has to be setup in rrConfig as well)
# Note:  tcp does not keep an open connection to the rrServer.
# Every command re-connects to the server
tcp = rrLib._rrTCP("")
# This function does only work in your company.
# It uses the RR_ROOT environment installed by rrWorkstationInstaller
rrServer = tcp.getRRServer()
if (len(rrServer) == 0):
    print (tcp.errorMessage())
if not tcp.setServer(rrServer, 7773):
    print ("Error setServer: " + tcp.errorMessage())
    sys.exit()

tcp.setLogin("TestUser", "Password")
tcp.jobGetInfoSend()
jobs = tcp.jobs

# Setup environment
value = jobs.getJobBasic(int(results["job-id"])).custom_Str("FTRACK_SERVER")
# Temp workaround of RR converting / to \
os.environ["FTRACK_SERVER"] = value.replace("\\", "/")
value = jobs.getJobBasic(int(results["job-id"])).custom_Str("FTRACK_APIKEY")
os.environ["FTRACK_APIKEY"] = value
value = jobs.getJobBasic(int(results["job-id"])).custom_Str("LOGNAME")
os.environ["LOGNAME"] = value
value = jobs.getJobBasic(int(results["job-id"])).custom_Str("FTRACK_TASKID")
os.environ["FTRACK_TASKID"] = value

status_mapping = {
    "pre": "Processing Queued",
    "preview": "Processing",
    "post": "Processing Done",
}
event_type = results["event-type"]

# Add ftrack module
path = os.path.join(os.path.dirname(results["event-script"]), "PYTHONPATH")
print "Adding path: " + path
sys.path.append(path)

import ftrack

ft_status = None
for status in ftrack.getTaskStatuses():
    if status.getName() == status_mapping[event_type]:
        ft_status = status
        break

task = ftrack.Task(os.environ["FTRACK_TASKID"])
task.setStatus(ft_status)
msg = "Setting \"{0}\" to \"{1}\"".format(
    task.getName(), ft_status.getName()
)
print msg
