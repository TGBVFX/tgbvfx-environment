import pyblish.api


class CollectExcludeSets(pyblish.api.ContextPlugin):
    """Exclude sets for decluttering."""

    order = pyblish.api.CollectorOrder + 0.2
    label = "Exclude sets"
    hosts = ["maya"]
    targets = ["default", "process"]

    def process(self, context):

        exclude_instances = []
        for instance in context:
            if "playblast" not in instance.data["families"]:
                exclude_instances.append(instance)

        for instance in exclude_instances:
            context.remove(instance)
