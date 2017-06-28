import pyblish.api


class IntegrateCreateStructure(pyblish.api.InstancePlugin):
    """"""

    order = pyblish.api.IntegratorOrder
    families = ["ftrack", "trackItem"]
    match = pyblish.api.Subset
    label = "Create Structure"
    optional = True
    active = False
    hosts = ["nukestudio"]

    def process(self, instance):
        import os

        import ftrack_template

        tasks = instance.data.get("ftrackTasks", [])
        templates = ftrack_template.discover_templates()
        for task in tasks:
            paths = ftrack_template.format(
                {}, templates, task, return_mode="all"
            )
            for path, template in paths:
                if not os.path.exists(path):
                    self.log.debug("Create directory: \"{0}\"".format(path))
                    os.makedirs(path)
