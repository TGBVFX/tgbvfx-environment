import os
import re
import logging
import subprocess

import ftrack
import ftrack_api

log = logging.getLogger(__name__)


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
    identifier = event["data"]["application"]["identifier"]

    # DJV View, files get selected by the user.
    if identifier.startswith("djvview"):
        return

    # RV
    if identifier.startswith("rv"):
        return

    app_id = None

    # Nuke applications.
    if identifier.startswith("nuke"):
        app_id = "nuke"
    if identifier.startswith("nukex"):
        app_id = "nuke"
    if identifier.startswith("nuke_studio"):
        app_id = "nukestudio"

    # Return if application is not recognized.
    if not app_id:
        print 'Application is not recognized to open a file: "{0}"'.format(
            identifier
        )
        return

    session = ftrack_api.Session()
    task = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )
    components = session.query(
        'Component where version.task_id is "{0}" and '
        'version.asset.name is "{1}" and name is "{2}"'.format(
            task["id"], task["name"], app_id
        )
    )

    component = None
    version = 0
    for entity in components:
        if entity["version"]["version"] > version:
            version = entity["version"]["version"]
            component = entity

    extension_mapping = {
        ".hrox": "nukestudio", ".nk": "nuke", ".mb": "maya", ".hip": "houdini"
    }
    extension = None
    for key, value in extension_mapping.iteritems():
        if value == app_id:
            extension = key
    if not component:
        component = {
            "version": {
                "version": 1, "task": task, "asset": {"parent": task["parent"]}
            },
            "file_type": extension
        }

    location = session.pick_location()
    work_file = location.structure.get_resource_identifier(component)

    # Find all work files and categorize by version.
    files = {}
    for f in os.listdir(os.path.dirname(work_file)):

        # If the file extension doesn't match, we'll ignore the file.
        if os.path.splitext(f)[1] != os.path.splitext(work_file)[1]:
            continue

        try:
            version = version_get(f, "v")[1]
            value = files.get(version, [])
            value.append(os.path.join(os.path.dirname(work_file), f))
            files[version] = value
        except ValueError:
            pass

    # Determine highest version files
    if files:
        work_file = max(files[max(files.keys())], key=os.path.getctime)
    print work_file
    # If no work file exists, create a work file
    if not os.path.exists(work_file):

        if not os.path.exists(os.path.dirname(work_file)):
            os.makedirs(os.path.dirname(work_file))

        # Call Nuke terminal to create an empty work file
        if app_id == "nuke":
            subprocess.call([
                event["data"]["application"]["path"],
                "-i",
                "-t",
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), "..", "nuke_save.py"
                    )
                ),
                work_file
            ])
        # Call Mayapy terminal to create an empty work file
        if app_id == "maya":
            subprocess.call(
                [
                    os.path.join(
                        os.path.dirname(
                            event["data"]["application"]["path"]
                        ),
                        "mayapy.exe"
                    ),
                    os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), "..", "maya_save.py"
                        )
                    ),
                    work_file
                ]
            )
        # Call hypthon terminal to create an empty work file
        if app_id == "houdini":
            subprocess.call([
                os.path.join(
                    os.path.dirname(event["data"]["application"]["path"]),
                    "hython2.7.exe"
                ),
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), "..", "houdini_save.py"
                    )
                ),
                work_file
            ])

    output = subprocess.check_output([
        "python",
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "open_work_file.py"
            )
        ),
        work_file
    ])

    data["command"].append(output.replace("\\", "/").splitlines()[0])
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
    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    subscription = "topic=ftrack.connect.application.launch"
    ftrack.EVENT_HUB.subscribe(subscription, modify_application_launch)
