import ftrack_api
import ftrack_connect


def modify_launch(event):
    """Modify the task launched to status "In Progress"."""

    session = ftrack_connect.session.get_shared_session()
    task = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )

    # Only operate on "Not Started" and "Pending Changes"
    if task["status"]["name"] not in ["Not Started", "Pending Changes"]:
        return

    status = session.query("Status where name is \"In Progress\"").one()
    task["status"] = status
    session.commit()


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
