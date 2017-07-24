import pyblish.api


class TGBFtrackExtractComponentsOverwrite(pyblish.api.InstancePlugin):
    """Setting all components from NukeStudio to not overwrite."""

    order = pyblish.api.ExtractorOrder
    label = "Components Overwrite"
    families = ["task"]
    hosts = ["nukestudio"]

    def process(self, instance):

        instance.data["component_overwrite"] = False
