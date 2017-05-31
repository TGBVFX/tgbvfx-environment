import os

import ftrack


def modify_application_launch(event):
    """Modify the application environment."""

    data = event["data"]

    data["options"]["env"]["FTRACK_EVENT_PLUGIN_PATH"] = (
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "tgbvfx-environment",
            "environment",
            "FTRACK_EVENT_PLUGIN_PATH"
        ) + os.pathsep +
        data["options"]["env"].get("FTRACK_EVENT_PLUGIN_PATH", "")
    )

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
