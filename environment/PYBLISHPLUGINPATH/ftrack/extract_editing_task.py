import pyblish.api


class TGBFtrackExtractEditingTask(pyblish.api.ContextPlugin):
    """Extract an "Editing" task to publish NukeStudio and Hiero scenes to.

    Offset to get context.data["ftrackProject"] from pyblish-grill plugins.
    """

    order = pyblish.api.ExtractorOrder + 0.1
    label = "Editing Task"
    hosts = ["nukestudio"]

    def process(self, context):

        session = context.data["ftrackSession"]
        parent = context.data["ftrackProject"]

        data = {
            "type.name": "Editing",
            "name": "editing",
            "parent.id": parent["id"]
        }
        query = "Task where "
        for key, value in data.iteritems():
            query += "{0} is \"{1}\" and ".format(key, value)
        query = query[:-5]

        task = session.query(query).first()

        if not task:
            tasktype = session.query("Type where name is \"Editing\"").first()
            status = session.query(
                "Status where name is \"In Progress\""
            ).first()
            task = session.create(
                "Task",
                {
                    "name": "editing",
                    "parent": parent,
                    "type": tasktype,
                    "status": status
                }
            )
            session.commit()

        context.data["ftrackTask"] = task
