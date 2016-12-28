import os
import re

import ftrack
import ftrack_api
import ftrack_template


def version_get(string, prefix, suffix=None):
    """ Extract version information from filenames.
    Code from Foundry"s nukescripts.version_get()
    """

    if string is None:
        raise ValueError("Empty version string - no match")

    regex = "." + prefix + "\d+"
    matches = re.findall(regex, string, re.IGNORECASE)
    if not len(matches):
        msg = "No " + prefix + " found in \"" + string + "\""
        raise ValueError(msg)
    return (matches[-1:][0][1], re.search("\d+", matches[-1:][0]).group())


def get_task_data(event):

    data = event["data"]
    app_id = event["data"]["application"]["identifier"].split("_")[0]

    session = ftrack_api.Session()
    task = session.get("Task", data["context"]["selection"][0]["entityId"])

    if app_id == "nukex":
        app_id = "nuke"

    templates = ftrack_template.discover_templates()
    work_file = ftrack_template.format(
        {app_id: app_id, "padded_version": "001"}, templates, entity=task
    )[0]
    work_area = os.path.dirname(work_file)

    max_version = 0
    launch_file = None
    for f in os.listdir(work_area):
        try:
            version = version_get(f, "v")[1]
            if version > max_version:
                max_version = version
                launch_file = os.path.join(work_area, f)
        except:
            pass

    if launch_file:
        data["command"].append(launch_file)

    return data


def modify_application_launch(event):
    """Modify the application launch command with potential files to open"""

    data = event["data"]
    selection = event["data"]["context"]["selection"]

    if not selection:
        return

    entityType = selection[0]["entityType"]

    # task based actions
    if entityType == "task":
        data = get_task_data(event)

    return data


def register(registry, **kw):
    """Register location plugin."""

    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    ftrack.EVENT_HUB.subscribe(
        "topic=ftrack.connect.application.launch",
        modify_application_launch
    )
