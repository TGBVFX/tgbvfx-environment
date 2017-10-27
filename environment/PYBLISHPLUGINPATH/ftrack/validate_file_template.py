import pyblish.api


class TGBFtrackValidateFileTemplate(pyblish.api.InstancePlugin):
    """Validate the existence of a lucidity template for the file extension."""

    order = pyblish.api.ValidatorOrder
    label = "File Template"
    optional = True

    def process(self, instance):
        import os
        import lucidity
        from tgbvfx_environment import utils

        # Ignore source instance
        if "source" == instance.data["family"]:
            return

        templates = lucidity.discover_templates()

        families = [
            "img", "gizmo", "lut", "scene", "cache", "mov", "camera",
            "geometry"
        ]
        assettype_short = list(
            set(instance.data["families"]) & set(families)
        )[0]
        if assettype_short in ["gizmo", "lut"]:
            assettype_short = "nuke_gizmo"
        if assettype_short in ["geometry"]:
            assettype_short = "model"

        assettype = utils.mock_entity(
            ("short", assettype_short),
            entity_type="AssetType"
        )
        asset = utils.mock_entity(
            ("parent", instance.context.data["ftrackTask"]["parent"]),
            ("type", assettype),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", instance.context.data["ftrackTask"]),
            ("version", 1),
            ("metadata", {"instance_name": instance.data["name"]}),
            entity_type="AssetVersion"
        )

        entity = None
        if "collection" in instance.data.keys():
            path = instance.data["collection"].format("{head}{padding}{tail}")
            entity = utils.mock_entity(
                ("version", assetversion),
                ("name", "main"),
                ("file_type", os.path.splitext(path)[1]),
                entity_type="SequenceComponent"
            )
        if "output_path" in instance.data.keys():
            path = instance.data["output_path"]
            entity = utils.mock_entity(
                ("version", assetversion),
                ("name", "main"),
                ("file_type", os.path.splitext(path)[1]),
                entity_type="FileComponent"
            )

        file_template_exists = False
        template_name = templates[0].get_template_name(entity)
        for template in templates:
            if template_name == template.name:
                file_template_exists = True

        msg = "Could not find any file templates for \"{0}\""
        assert file_template_exists, msg.format(template_name)
