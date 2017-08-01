import pyblish.api


class TGBFtrackExtractComponents(pyblish.api.InstancePlugin):
    """Setting data for all components from NukeStudio."""

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


class TGBFtrackExtractOverwrite(pyblish.api.InstancePlugin):
    """Option to overwrite Nuke scripts."""

    order = TGBFtrackExtractComponents.order + 0.01
    label = "TGBVFX Overwrite Nuke Scripts"
    families = ["trackItem.task"]
    hosts = ["nukestudio"]
    optional = True
    active = False

    def process(self, instance):

        if "scene" in instance.data["families"]:
            instance.data["component_overwrite"] = True
