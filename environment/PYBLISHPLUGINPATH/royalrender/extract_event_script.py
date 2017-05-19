import os
import shutil

import pyblish.api as api
from dirsync import sync


class TGBVFXEnvironmentRoyalRenderExtractEventScript(api.InstancePlugin):
    """ Add event script for updating Ftrack status. """

    order = api.ExtractorOrder
    label = "Event Script"
    families = ["royalrender", "ftrack"]
    match = api.Subset

    def process(self, instance):

        data = instance.data.get("royalrenderData", {})

        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "royalrender"
        )

        if not os.path.exists(directory):
            os.makedirs(directory)

        destination = os.path.join(directory, "event_script.py")
        shutil.copy(
            os.path.join(
                os.path.dirname(__file__),
                "event_script",
                "event_script.py"
            ),
            destination
        )

        # Add required custom variables
        data["CustomEventScript"] = destination
        data["CustomFTRACK_SERVER"] = os.environ["FTRACK_SERVER"]
        data["CustomFTRACK_APIKEY"] = os.environ["FTRACK_APIKEY"]
        data["CustomLOGNAME"] = os.environ["LOGNAME"]
        data["CustomFTRACK_TASKID"] = os.environ["FTRACK_TASKID"]

        # Copy required files
        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "royalrender",
            "PYTHONPATH"
        )

        sync(
            os.path.join(os.path.dirname(__file__), "PYTHONPATH"),
            directory,
            "sync",
            create=True,
            purge=True,
            modtime=True
        )

        data["CustomPYTHONPATH"] = directory

        # Setting data
        instance.data["royalrenderData"] = data
