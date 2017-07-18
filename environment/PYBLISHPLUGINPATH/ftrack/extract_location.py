import pyblish.api


class TGBFtrackExtractLocation(pyblish.api.InstancePlugin):
    """Setup location for each component."""

    order = pyblish.api.ExtractorOrder
    label = "Location"
    families = ["task"]
    hosts = ["nukestudio"]

    def process(self, instance):

        location = instance.context.data["ftrackSession"].query(
            'Location where name is "lucidity"'
        ).first()

        instance.data["component_location"] = location
