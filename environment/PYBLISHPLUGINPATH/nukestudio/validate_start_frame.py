import pyblish.api


class ValidateStartFrame(pyblish.api.InstancePlugin):
    """Validate start frame to be 1001, per studio preference."""

    order = pyblish.api.ValidatorOrder
    label = "Start Frame"
    families = ["trackItem.task"]
    optional = True
    hosts = ["nukestudio"]

    def process(self, instance):

        msg = (
            "Start frame of the task is not the studio preference of \"1001\"."
            " Please specify the start frame to be \"1001\" in the export "
            "dialog, and subtract any handles. If you have 10 frame handles, "
            "the start frame should be 991."
        )
        assert instance.data["parent"].data["startFrame"] == 1001, msg
