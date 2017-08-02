import pyblish.api


class ValidateTrackItemName(pyblish.api.InstancePlugin):
    """Validate start frame to be 1001, per studio preference."""

    order = pyblish.api.ValidatorOrder
    label = "Start Frame"
    families = ["trackItem.task"]
    optional = True
    hosts = ["nukestudio"]

    def process(self, instance):

        msg = (
            'Start frame of the task is not the studio preference of "1001". '
            'Please specify the start frame to be "1001" in the export dialog.'
        )
        assert instance.data["parent"].data["startFrame"] == 1001, msg