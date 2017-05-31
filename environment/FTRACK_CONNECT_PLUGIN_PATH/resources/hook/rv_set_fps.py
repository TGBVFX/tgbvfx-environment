import logging

import ftrack
import ftrack_api

log = logging.getLogger(__name__)


def modify_launch(event):
    """Modify the application launch command with potential files to open"""
    app_id = event["data"]["application"]["identifier"].split("_")[0]

    # RV
    if app_id == "rv":
        session = ftrack_api.Session()
        task = session.get(
            "Task", event["data"]["context"]["selection"][0]["entityId"]
        )

        if not task:
            return

        if "fps" in task["parent"]["custom_attributes"]:
            fps = task["parent"]["custom_attributes"]["fps"]
            event["data"]["command"].append("-fps")
            event["data"]["command"].append(str(fps))

    return event


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
        modify_launch
    )
