import pyblish.api


class IntegrateCreateStructure(pyblish.api.InstancePlugin):
    """Create project structure."""

    order = pyblish.api.IntegratorOrder
    families = ["ftrack", "trackItem"]
    match = pyblish.api.Subset
    label = "Create Structure"
    optional = True
    hosts = ["nukestudio"]

    def process(self, instance):
        import os
        import shutil

        import lucidity

        session = instance.context.data["ftrackSession"]
        templates = lucidity.discover_templates()
        path_templates = []
        for item in instance.data["ftrackShot"]["link"]:

            data = {}
            data["entity"] = session.get(item["type"], item["id"])
            entity_type = session.get(item["type"], item["id"]).entity_type

            for template in templates:

                if entity_type != template.name:
                    continue

                try:
                    path = os.path.abspath(template.format(data))
                except lucidity.error.FormatError:
                    continue
                else:
                    path_templates.append((path.replace("\\", "/"), template))

        for path, template in path_templates:
            if hasattr(template, "source"):
                if not os.path.exists(os.path.dirname(path)):
                    self.log.debug(
                        'Creating directory: "{0}".'.format(
                            os.path.dirname(path)
                        )
                    )
                    os.makedirs(os.path.dirname(path))

                self.log.debug(
                    'Copying "{0}" to "{1}".'.format(template.source, path)
                )
                shutil.copy(template.source, path)
            else:
                if not os.path.exists(path):
                    self.log.debug('Creating directory: "{0}".'.format(path))
                    os.makedirs(path)
