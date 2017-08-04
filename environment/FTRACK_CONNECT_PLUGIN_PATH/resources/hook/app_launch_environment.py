import os
import platform

import ftrack_api
import ftrack_connect


def ftrack_event_plugin_path(event):
    """Modify the application environment to include new api location."""

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

    session = ftrack_connect.session.get_shared_session()
    task = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    # Need to enforce variable to string type, as returned type is unicode.
    data["options"]["env"]["PROJECT_PATH"] = (
        str(
            os.path.abspath(
                os.path.join(
                    task["project"]["disk"][system_name],
                    task["project"]["root"]
                )
            )
        )
    )

    return data


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = "topic=ftrack.connect.application.launch"
    session.event_hub.subscribe(subscription, ftrack_event_plugin_path)
