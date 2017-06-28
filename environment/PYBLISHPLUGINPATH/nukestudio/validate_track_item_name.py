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

        pattern = r"sq[0-9]{3}--sh[0-9]{4}"

        failure_message = (
            'The track item "{0}" is not named according to the studios naming'
            ' convention. The naming convention follows "sq%03d--sh%04d", for '
            'example "sq001--sh0010"'.format(instance[0].name())
        )
        assert re.match(pattern, instance[0].name()), failure_message
