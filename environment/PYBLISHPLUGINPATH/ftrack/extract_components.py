import pyblish.api


class TGBFtrackExtractComponents(pyblish.api.InstancePlugin):
    """Setting all components from NukeStudio to not overwrite."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Components"
    families = ["task"]
    hosts = ["nukestudio"]

    def process(self, instance):

        if "scene" not in instance.data["families"]:
            instance.data["component_overwrite"] = True

        data = instance.data.get("assetversion_data", {})

        metadata = data.get("metadata", {})
        metadata.update({"video_track": instance[0]._track.name()})

        data["metadata"] = metadata

        instance.data["assetversion_data"] = data
