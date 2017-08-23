import os
import re
import logging
import subprocess

import ftrack
import ftrack_api
from tgbvfx_environment import utils

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
        # Ignore NukeStudio until we can generate a work file.
        return

    # Maya
    if identifier.startswith("maya"):
        app_id = "maya"

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
    work_file = utils.get_work_file(session, task, app_id, 1)

    # Find all work files and categorize by version.
    files = {}
    work_file_head = work_file.split("".join(version_get(work_file, "v")))[0]
    if os.path.exists(os.path.dirname(work_file)):
        for f in os.listdir(os.path.dirname(work_file)):

            # If the file extension doesn't match, we'll ignore the file.
            if os.path.splitext(f)[1] != os.path.splitext(work_file)[1]:
                continue

            try:
                version = version_get(f, "v")[1]
                value = files.get(version, [])
                file_path = os.path.abspath(
                    os.path.join(os.path.dirname(work_file), f)
                )
                f_head = file_path.split("v" + version)[0]
                # Only compare against the head because user can have notations
                # after version number.
                if f_head == work_file_head:
                    value.append(file_path)
                    files[version] = value
            except ValueError:
                pass

    # Determine highest version files
    if files:
        work_file = max(files[max(files.keys())], key=os.path.getctime)

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
    output_file = output.replace("\\", "/").splitlines()[0]
    if os.path.exists(output_file):
        data["command"].append(output_file)
    else:
        data["command"] = ""

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
