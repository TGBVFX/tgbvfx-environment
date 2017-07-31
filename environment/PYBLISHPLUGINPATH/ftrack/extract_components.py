import pyblish.api


class TGBFtrackExtractComponents(pyblish.api.InstancePlugin):
    """Setting all components from NukeStudio to not overwrite."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Components"
    families = ["trackItem.task"]
    hosts = ["nukestudio"]

    def process(self, instance):

        if "scene" not in instance.data["families"]:
            instance.data["component_overwrite"] = True

        # AssetVersion data
        data = instance.data.get("assetversion_data", {})

        metadata = data.get("metadata", {})
        video_track = instance.data["parent"].data["item"].parent()
        metadata.update({"video_track": video_track.name()})

        data["metadata"] = metadata

        instance.data["assetversion_data"] = data
