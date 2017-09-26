import pyblish.api


class TGBFtrackExtractComponents(pyblish.api.ContextPlugin):
    """Setting data for all components."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Components"

    def process(self, context):

        for instance in context:

            asset_data = instance.data.get("asset_data", {})
            asset_data.update(
                {
                    "name": "{0}_{1}".format(
                        instance.context.data["ftrackTask"]["name"],
                        instance.data["name"]
                    )
                }
            )
            instance.data["asset_data"] = asset_data

            component_data = instance.data.get("component_data", {})
            component_data.update({"name": "main"})
            instance.data["component_data"] = component_data


class TGBFtrackExtractComponentsNukeStudio(pyblish.api.InstancePlugin):
    """Setting data for all components from NukeStudio."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX NukeStudio Components"
    families = ["trackItem.task"]
    hosts = ["nukestudio"]

    def process(self, instance):
        families = instance.data.get("families", [])
        families += [instance.data["family"]]

        if "scene" not in families:
            instance.data["component_overwrite"] = True

        # AssetVersion data
        data = instance.data.get("assetversion_data", {})

        metadata = data.get("metadata", {})
        video_track = instance.data["parent"].data["item"].parent()
        metadata.update({"instance_name": video_track.name()})

        data["metadata"] = metadata

        instance.data["assetversion_data"] = data


class TGBFtrackExtractOverwriteNukeStudio(pyblish.api.InstancePlugin):
    """Option to overwrite Nuke scripts."""

    order = TGBFtrackExtractComponents.order + 0.01
    label = "TGBVFX Overwrite Nuke Scripts"
    families = ["trackItem.task"]
    hosts = ["nukestudio"]
    optional = True
    active = False

    def process(self, instance):
        families = instance.data.get("families", [])
        families += [instance.data["family"]]

        if "scene" in families:
            instance.data["component_overwrite"] = True


class TGBFtrackExtract(pyblish.api.InstancePlugin):
    """Enable overwriting image sequence components."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Detail Components"
    families = ["img", "gizmo", "lut", "backdrop", "cache"]
    hosts = ["nuke", "ftrack"]

    def process(self, instance):
        instance.data["component_overwrite"] = True
        families = instance.data.get("families", [])
        families += [instance.data["family"]]

        # Only commiting first and last frame to optimize calls to Ftrack.
        # Need first and last for later importing with ftrack-connect-nuke.
        if "collection" in instance.data.keys():
            indexes = instance.data["collection"].indexes
            ranges = "[{0},{1}]".format(min(indexes), max(indexes))
            instance.data["pattern"] = "{head}{padding}{tail} " + ranges

        if "img" in families:
            data = instance.data.get("assetversion_data", {})
            metadata = data.get("metadata", {})
            metadata.update({"instance_name": instance.data["name"]})
            data["metadata"] = metadata
            instance.data["assetversion_data"] = data

        if "cache" in families:
            data = instance.data.get("assetversion_data", {})
            metadata = data.get("metadata", {})
            metadata.update({"instance_name": instance.data["name"]})
            data["metadata"] = metadata
            instance.data["assetversion_data"] = data

        if "backdrop" in families:
            data = instance.data.get("assetversion_data", {})
            metadata = data.get("metadata", {})
            metadata.update(
                {
                    "template": "Backdrop",
                    "instance_name": instance.data["name"]
                }
            )
            data["metadata"] = metadata
            instance.data["assetversion_data"] = data
