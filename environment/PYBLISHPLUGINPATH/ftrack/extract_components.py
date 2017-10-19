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
    """Detailed component data."""

    order = pyblish.api.ExtractorOrder
    label = "TGBVFX Detail Components"
    families = [
        "img", "gizmo", "lut", "scene", "cache", "mov", "camera", "geometry"
    ]
    hosts = ["maya", "nuke", "ftrack"]

    def process(self, instance):
        instance.data["component_overwrite"] = True
        families = instance.data.get("families", [])
        families += [instance.data["family"]]

        # Only commiting first and last frame to optimize calls to Ftrack.
        # Need first and last for later importing with Ftrack Importer.
        if "collection" in instance.data.keys():
            indexes = instance.data["collection"].indexes
            ranges = "[{0},{1}]".format(min(indexes), max(indexes))
            instance.data["pattern"] = "{head}{padding}{tail} " + ranges

        if len(list(set(self.families) & set(families))) == 1:
            data = instance.data.get("assetversion_data", {})
            metadata = data.get("metadata", {})
            metadata.update({"instance_name": instance.data["name"]})
            data["metadata"] = metadata
            instance.data["assetversion_data"] = data

        if "camera" in families or "geometry" in families:
            # Ensure never to overwrite
            instance.data["component_overwrite"] = False
            # Ensure a new version is created every time
            instance.data["version"] = 0

        if "geometry" in families:
            instance.data["assettype_data"] = {"short": "model"}
