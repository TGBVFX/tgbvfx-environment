import pyblish.api


class TGBFtrackValidateFileTemplate(pyblish.api.InstancePlugin):
    """Validate the existence of a lucidity template for the file extension."""

    order = pyblish.api.ValidatorOrder
    label = "File Template"
    optional = True

    def process(self, instance):
        import os
        import lucidity

        templates = lucidity.discover_templates()
        path = ""
        if "collection" in instance.data.keys():
            path = instance.data["collection"].format("{head}{padding}{tail}")
        if "output_path" in instance.data.keys():
            path = instance.data["output_path"]

        extension = os.path.splitext(path)[1]
        file_template_exists = False
        for template in templates:
            if extension in template.name:
                file_template_exists = True

        msg = "Could not find any file templates for extension \"{0}\""
        assert file_template_exists, msg.format(extension)
