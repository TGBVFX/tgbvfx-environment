import ftrack_api
import lucidity
from ftrack_connect.session import get_shared_session


def modify_launch(event):
    """Return each entities in the selection in data dictionaries."""

    data = event["data"]
    task = get_shared_session().get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )
    templates = lucidity.discover_templates()
    template_name = templates[0].get_template_name(task["parent"])
    for template in templates:
        if template.name == template_name:
            # Return first valid path. This is up to the templates
            # definition to order what comes first.
            return data["command"].extend(
                ["--path", template.format(task["parent"])]
            )


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = "topic=ftrack.connect.application.launch and "
    subscription += "data.application.identifier=pyblish*"
    session.event_hub.subscribe(subscription, modify_launch)
