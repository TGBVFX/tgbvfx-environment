import pyblish.api


class TGBFtrackExtractComponents(pyblish.api.InstancePlugin):
    """Setting all components from NukeStudio to not overwrite."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Components"
    families = ["task"]
    hosts = ["nukestudio"]

    def process(self, instance):

        instance.data["component_overwrite"] = False
        instance.data["component_metadata"] = {"video_track": "plate001"}
