import os

import pyblish.api as api


class TGBVFXEnvironmentRoyalRenderExtractEventScript(api.InstancePlugin):
    """ Add event script for updating Ftrack status.

    Offset to fetch Nuke job.
    """

    order = api.ExtractorOrder + 0.1
    label = "Event Script"
    families = ["royalrender"]
    targets = ["process.royalrender"]

    def process(self, instance):

        event_script_path = os.path.join(
            os.path.dirname(__file__),
            "event_script",
            "event_script.py"
        )
        pythonpath = os.path.join(
            os.path.dirname(__file__), "PYTHONPATH"
        )

        # Check if event script is local
        if event_script_path.lower().startswith("c"):
            network_path = (
                "//10.10.200.11/171000_TGB_Library/pipeline/repositories/"
                "tgbvfx-environment/tgbvfx-environment/environment/"
                "PYBLISHPLUGINPATH/royalrender/event_script/event_script.py"
            )
            self.log.warning(
                "\"{0}\" is a local path. Hardcoding to network path: "
                "\"{1}\"".format(event_script_path, network_path)
            )
            event_script_path = network_path

        # Check if pythonpath is local
        if pythonpath.lower().startswith("c"):
            network_path = (
                "//10.10.200.11/171000_TGB_Library/pipeline/repositories/"
                "tgbvfx-environment/tgbvfx-environment/environment/"
                "PYBLISHPLUGINPATH/royalrender/PYTHONPATH"
            )
            self.log.warning(
                "\"{0}\" is a local path. Hardcoding to network path: "
                "\"{1}\"".format(pythonpath, network_path)
            )
            pythonpath = network_path

        for job in instance.data["royalrenderJobs"]:

            # Add required custom variables
            job["CustomEventScript"] = event_script_path
            job["CustomFTRACK_SERVER"] = os.environ["FTRACK_SERVER"]
            job["CustomFTRACK_APIKEY"] = os.environ["FTRACK_APIKEY"]
            job["CustomLOGNAME"] = os.environ["LOGNAME"]
            job["CustomFTRACK_TASKID"] = os.environ["FTRACK_TASKID"]
            job["CustomPYTHONPATH"] = pythonpath
