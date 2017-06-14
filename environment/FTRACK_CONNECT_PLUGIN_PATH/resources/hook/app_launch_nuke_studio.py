import os
import shutil

import ftrack
import ftrack_api
import ftrack_template


def get_work_file(event):

    data = event["data"]
    if not data["context"]["selection"]:
        return

    session = ftrack_api.Session()
    task = session.get("Task", data["context"]["selection"][0]["entityId"])
    query = "AssetVersion where task.id is \"{0}\" and asset.name is "
    query += "\"nukestudio\""
    versions = session.query(query.format(task["id"]))

    if not versions:
        return

    version = list(versions)[-1]

    templates = ftrack_template.discover_templates()
    work_file, template = ftrack_template.format(
        {
            "nukestudio": "nukestudio",
            "padded_version": str(version["version"]).zfill(3)
        },
        templates,
        entity=task
    )

    if not os.path.exists(work_file):
        location = session.pick_location()
        src = location.get_resource_identifier(version["components"][0])

        if not os.path.exists(os.path.dirname(work_file)):
            os.makedirs(os.path.dirname(work_file))

        shutil.copy(src, work_file)

    return work_file


def ftrack_event_plugin_path(event):
    """Modify the nuke studio environment to include studio processors"""
    data = event["data"]

    # Add custom processors
    data["options"]["env"]["FTRACK_EVENT_PLUGIN_PATH"] = (
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "tgbvfx-environment",
            "nuke_studio_processors"
        ) + os.pathsep +
        data["options"]["env"].get("FTRACK_EVENT_PLUGIN_PATH", "")
    )

    # Open work file
    work_file = get_work_file(event)
    if work_file and os.path.exists(work_file):
        data["command"].append(work_file)

    return data


def register(registry, **kw):
    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    subscription = "topic=ftrack.connect.application.launch and "
    subscription += "data.application.identifier=nuke_studio*"
    ftrack.EVENT_HUB.subscribe(subscription, ftrack_event_plugin_path)
