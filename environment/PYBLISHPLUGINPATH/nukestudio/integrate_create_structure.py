import pyblish.api


class IntegrateCreateStructure(pyblish.api.ContextPlugin):
    """Create project structure."""

    order = pyblish.api.IntegratorOrder
    label = "Create Structure"
    optional = True
    hosts = ["nukestudio"]

    def process(self, context):
        import os
        import shutil

        import lucidity

        session = context.data["ftrackSession"]
        templates = lucidity.discover_templates()

        # Get all entities in context and their parents.
        entities = []
        for instance in context:
            if "ftrackEntity" not in instance.data["families"]:
                continue
            for item in instance.data["entity"]["link"]:
                entities.append(session.get(item["type"], item["id"]))

        # Get all resolved paths and their templates.
        path_templates = []
        for entity in list(set(entities)):
            valid_templates = templates[0].get_valid_templates(
                entity, templates
            )
            for template in valid_templates:
                try:
                    path = os.path.abspath(template.format(entity))
                except lucidity.error.FormatError:
                    continue
                else:
                    path_templates.append(
                        (path.replace("\\", "/"), template)
                    )

        for path, template in path_templates:
            # Copy source templates.
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
                # Create directories.
                if not os.path.exists(path):
                    self.log.debug('Creating directory: "{0}".'.format(path))
                    os.makedirs(path)
