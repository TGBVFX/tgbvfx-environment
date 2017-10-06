import os
import subprocess

from conda_git_deployment import utils
import ftrack_api


def modify_launch(data):
    """Prompt user to update pipeline."""

    if utils.updates_available():
        subprocess.call([
            "python",
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "pipeline_update.py"
                )
            )
        ])

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
    session.event_hub.subscribe(subscription, modify_launch)
