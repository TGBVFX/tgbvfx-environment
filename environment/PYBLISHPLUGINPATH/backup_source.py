import os
import datetime
import shutil

import pyblish.api
import filelink


class TGBBackupSource(pyblish.api.ContextPlugin):
    """Extracts a backup of the source scene."""

    order = pyblish.api.ExtractorOrder
    label = "Backup Source"
    targets = ["default", "process"]

    def process(self, context):

        src = context.data["currentFile"]

        path, ext = os.path.splitext(src)
        dst = os.path.join(
            os.path.dirname(src),
            "workspace",
            "backup",
            "{0}_{1}{2}".format(
                os.path.basename(path),
                datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                ext
            )
        )

        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))

        try:
            filelink.create(src, dst)
        except WindowsError as e:
            if e.winerror == 17:
                self.log.warning(
                    "File linking failed due to: \"{0}\". "
                    "Resorting to copying instead.".format(e)
                )
                shutil.copy(src, dst)
            else:
                raise e
