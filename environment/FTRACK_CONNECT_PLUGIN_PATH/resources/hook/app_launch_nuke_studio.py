import os

import ftrack


def modify_application_launch(event):
    """Modify the NukeStudio launch"""

    data = event["data"]

    env = ""
    for path in os.environ["FTRACK_EVENT_PLUGIN_PATH"].split(os.pathsep):
        if "ftrack-connect-nuke-studio" in path and "processor" in path:
            continue
        env += path + os.pathsep

    data["options"]["env"]["FTRACK_EVENT_PLUGIN_PATH"] = env

    return data


def register(registry, **kw):
    """Register location plugin."""

    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    subscription = "topic=ftrack.connect.application.launch and "
    subscription += "data.application.identifier=nuke_studio*"
    ftrack.EVENT_HUB.subscribe(
        subscription,
        modify_application_launch
    )
