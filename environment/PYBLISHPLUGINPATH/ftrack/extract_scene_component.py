import pyblish.api


class TGBFtrackExtractSceneComponent(pyblish.api.InstancePlugin):
    """Appending output files from local extraction as components."""

    order = pyblish.api.ExtractorOrder
    label = "Scene Component"
    families = ["source"]

    def process(self, instance):
        import ftrack_api

        # Add ftrack family
        families = instance.data.get("families", [])
        instance.data["families"] = families + ["ftrack"]

        # Add component
        components = instance.data.get("ftrackComponentsList", [])

        # Since we are manually validating the location of the source, we don't
        # need the location to manage the data hence using "ftrack.unmanaged".
        # This is because there is no published scene location.
        location = instance.context.data["ftrackSession"].query(
            'Location where name is "ftrack.unmanaged"'
        ).one()

        components.append(
            {
                "assettype_data": {"short": "scene"},
                "assetversion_data": {
                    "version": instance.context.data["version"]
                },
                "component_data": {
                    "name": pyblish.api.current_host(),
                },
                "component_path": instance.context.data["currentFile"],
                "component_overwrite": True,
                "component_location": location
            }
        )

        instance.data["ftrackComponentsList"] = components
