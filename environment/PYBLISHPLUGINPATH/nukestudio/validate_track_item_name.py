import pyblish.api


class ValidateTrackItemName(pyblish.api.InstancePlugin):
    """Validate track item name to follow studio naming convention

    Studio naming convention: sq%03d--sh%04d (sq001--sh0010)
    """

    order = pyblish.api.ValidatorOrder
    label = "Task Item Name"
    families = ["trackItem"]
    optional = True
    hosts = ["nukestudio"]

    def process(self, instance):
        import re

        if instance.data["family"] != "trackItem":
            return

        pattern = r"sq[0-9]{4}--sh[0-9]{4}"

        failure_message = (
            'The track item "{0}" is not named according to the studios naming'
            ' convention. The naming convention follows "sq%04d--sh%04d", for '
            'example "sq0010--sh0010"'.format(instance.data["item"].name())
        )
        assert re.match(pattern, instance.data["item"].name()), failure_message
