import os
import logging

import ftrack


logging.basicConfig()
logger = logging.getLogger()


def appendPath(path, key, environment):
    """Append *path* to *key* in *environment*."""
    try:
        environment[key] = (
            os.pathsep.join([
                environment[key], path.replace("\\", "/")
            ])
        )
    except KeyError:
        environment[key] = path.replace("\\", "/")

    return environment


def modify_application_launch(event):
    """Modify the application launch command with potential files to open"""

    environment = {}

    identifier = event["data"]["application"]["identifier"]
    app_id = None

    # Nuke applications.
    if identifier.startswith("nuke"):
        app_id = "nuke"
    if identifier.startswith("nukex"):
        app_id = "nuke"
    if identifier.startswith("nuke_studio"):
        app_id = "nukestudio"

    # Maya
    if identifier.startswith("maya"):
        app_id = "maya"

    # Pyblish
    if identifier.startswith("pyblish"):
        app_id = "pyblish"

    # Return if application is not recognized.
    if not app_id:
        msg = '{0} - Application is not recognized to setup PYBLISHPATH: "{1}"'
        print msg.format(__file__, identifier)
        return

    # Get task type
    task_type = ""
    try:
        task_id = event["data"]["context"]["selection"][0]["entityId"]
        task = ftrack.Task(task_id)
        task_type = task.getType().getName().lower()
    except:
        pass

    # PYBLISHPLUGINPATH
    bumpybox_plugins_dir = os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins"
    )
    environment_plugins_dir = os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "tgbvfx-environment",
        "environment",
        "PYBLISHPLUGINPATH"
    )

    environment["PYBLISHPLUGINPATH"] = [
        os.path.join(environment_plugins_dir, "ftrack"),
        os.path.join(environment_plugins_dir, "royalrender"),
        os.path.join(environment_plugins_dir, app_id),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-ftrack",
            "pyblish_ftrack",
            "plugins"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-royalrender",
            "pyblish_royalrender",
            "plugins"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-" + app_id,
            "pyblish_" + app_id,
            "plugins"
        ),
        bumpybox_plugins_dir,
        os.path.join(bumpybox_plugins_dir, "ftrack"),
        os.path.join(bumpybox_plugins_dir, "royalrender"),
        os.path.join(bumpybox_plugins_dir, app_id),
        os.path.join(bumpybox_plugins_dir, app_id, task_type),
    ]

    # adding variables
    data = event["data"]
    for variable in environment:
        for path in environment[variable]:
            appendPath(path, variable, data["options"]["env"])

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
