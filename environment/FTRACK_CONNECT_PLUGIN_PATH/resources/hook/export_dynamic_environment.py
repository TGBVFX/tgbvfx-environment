import os
import json
import threading
import traceback
import sys

import ftrack_api
from ftrack_hooks.action import BaseAction


def async(fn):
    """Run *fn* asynchronously."""
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


def get_children_recursive(entity, children=[]):

    for child in entity["children"]:
        children.append(child)
        children.extend(get_children_recursive(child, []))

    return children


@async
def create_job(entities, event, session):
    import dynamic_environment

    user = session.query(
        "User where username is \"{0}\"".format(os.environ["LOGNAME"])
    ).one()
    job = session.create(
        "Job",
        {
            "user": user,
            "status": "running",
            "data": json.dumps({
                "description": "Export Dynamic Environments."
            })
        }
    )
    # Commit to feedback to user.
    session.commit()

    # Get task entities
    job_entities = []

    for entity_type, entity_id in entities:
        entity = session.get(entity_type, entity_id)
        job_entities.append(entity)

        # Collect children if requested
        if event["data"]["values"]["include_children"]:
            job_entities.extend(get_children_recursive(entity, []))
        # Collect parents if requested
        if event["data"]["values"]["include_parents"]:
            for item in reversed(entity["link"][:-1]):
                job_entities.insert(
                    0, session.get(item["type"], item["id"])
                )

    # Filter to tasks only
    task_entities = []
    for entity in job_entities:
        if entity.entity_type == "Task":
            task_entities.append(entity)

    # Write batch scripts
    application_identifiers = ["maya_2017", "nuke_10.5v3"]

    location = session.pick_location()

    try:
        for entity in task_entities:
            root = location.structure.get_resource_identifier(entity["parent"])

            if not os.path.exists(root):
                os.makedirs(root)

            for application_identifier in application_identifiers:
                environment = dynamic_environment.get_dynamic_environment(
                    session, entity, application_identifier
                )
                batch_data = ""
                for variable, paths in environment.iteritems():
                    batch_data += "set {0}={1}\n".format(variable, paths)

                batch_path = os.path.join(
                    root, "{0}.bat".format(application_identifier)
                )
                try:
                    print "Writing {0}".format(batch_path)
                    with open(batch_path, "w") as the_file:
                        the_file.write(batch_data)
                except IOError:
                    pass
    except Exception:
        print traceback.format_exc()
        job["status"] = "failed"
    else:
        job["status"] = "done"

    # Commit to end job.
    session.commit()


class ExportAction(BaseAction):

    label = "Export Dynamic Environments"
    variant = None
    identifier = "export-dynamic-environments"
    description = None

    def __init__(self, session):
        """Expects a ftrack_api.Session instance"""
        super(ExportAction, self).__init__(session)

    def discover(self, session, entities, event):

        # Only discover the action if any selection is made.
        if entities:
            return True

        return False

    def launch(self, session, entities, event):

        # Adding dynamic environments module to PYTHONPATH
        import ftrack_hooks
        path = os.path.abspath(
            os.path.join(
                ftrack_hooks.__file__,
                "..",
                "..",
                "dynamic_environment",
                "resource",
                "hook"
            )
        )
        sys.path.append(path)

        if "values" in event["data"]:
            create_job(entities, event, session)
            return True

        return {
            "success": True,
            "message": "",
            "items": [
                {
                    "label": "Include parents",
                    "type": "boolean",
                    "name": "include_parents",
                    "value": False
                },
                {
                    "label": "Include children",
                    "type": "boolean",
                    "name": "include_children",
                    "value": False
                }
            ]
        }


def register(session):

    # Validate that session is an instance of ftrack_api.Session. If not,assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    # Create action and register to respond to discover and launch actions.
    action = ExportAction(session)
    action.register()
