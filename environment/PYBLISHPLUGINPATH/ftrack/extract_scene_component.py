import pyblish.api


class TGBFtrackExtractSceneComponent(pyblish.api.InstancePlugin):
    """Appending output files from local extraction as components."""

    order = pyblish.api.ExtractorOrder
    label = "Scene Component"
    families = ["source"]

    def process(self, instance):

        # Add ftrack family
        families = instance.data.get("families", [])
        instance.data["families"] = families + ["ftrack"]

        # Add component
        components = instance.data.get("ftrackComponentsList", [])

        components.append({
            "assettype_data": {"short": "scene"},
            "assetversion_data": {
                "version": instance.context.data["version"]
            },
            "component_data": {
                "name": pyblish.api.current_host(),
            },
            "component_path": instance.context.data["currentFile"],
            "component_overwrite": True
        })

        instance.data["ftrackComponentsList"] = components
