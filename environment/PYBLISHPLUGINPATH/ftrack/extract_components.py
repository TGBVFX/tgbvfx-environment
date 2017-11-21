import os

import pyblish.api
from tgbvfx_environment import utils


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

    order = pyblish.api.ExtractorOrder + 0.1
    label = "TGBVFX Detail Components"
    families = [
        "img", "gizmo", "lut", "scene", "cache", "mov", "camera", "geometry"
    ]
    hosts = ["maya", "nuke", "nukeassist", "ftrack", "nukestudio"]

    def recursive_available_version(self, component, location):

        path = location.structure.get_resource_identifier(component)

        if os.path.exists(path):
            component["version"]["version"] += 1
            return self.recursive_available_version(component, location)
        else:
            return component["version"]["version"]

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

        if "geometry" in families:
            instance.data["assettype_data"] = {"short": "model"}

        if "camera" in families:
            instance.data["assettype_data"] = {"short": "camera"}

        if "camera" in families or "geometry" in families:
            # Ensure never to overwrite
            instance.data["component_overwrite"] = False
            # Version starts from context version
            version = instance.context.data["version"]
            # Check for next available version on disk
            assettype = utils.mock_entity(
                ("short", instance.data["assettype_data"]["short"]),
                entity_type="Asset"
            )
            asset = utils.mock_entity(
                ("parent", instance.context.data["ftrackTask"]["parent"]),
                ("type", assettype),
                entity_type="Asset"
            )
            assetversion = utils.mock_entity(
                ("asset", asset),
                ("task", instance.context.data["ftrackTask"]),
                ("version", version),
                ("metadata", {"instance_name": instance.data["name"]}),
                entity_type="AssetVersion"
            )
            component = utils.mock_entity(
                ("version", assetversion),
                (
                    "file_type",
                    os.path.splitext(instance.data["output_path"])[1]
                ),
                entity_type="FileComponent"
            )

            location = instance.context.data["ftrackSession"].pick_location()
            instance.data["version"] = self.recursive_available_version(
                component, location
            )
