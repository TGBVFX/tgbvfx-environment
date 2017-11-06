import pyblish.api


class CollectExcludeSets(pyblish.api.ContextPlugin):
    """Exclude sets for decluttering."""

    order = pyblish.api.CollectorOrder + 0.1
    label = "Exclude sets"
    hosts = ["maya"]
    targets = ["default", "process"]

    def process(self, context):

        sets_instances = []
        for instance in context:
            if "set" in instance.data["families"]:
                sets_instances.append(instance)

        for instance in sets_instances:
            context.remove(instance)
