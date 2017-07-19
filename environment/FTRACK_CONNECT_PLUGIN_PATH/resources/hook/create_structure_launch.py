import os

import ftrack_api
from ftrack_connect.session import get_shared_session
import lucidity


def modify_launch(event):
    """Return each entities in the selection in data dictionaries."""

    session = get_shared_session()
    templates = lucidity.discover_templates()
    for item in event["data"]["selection"]:
        entity = session.get(item[0], item[1])
        for link in entity["link"]:

            data = {}
            data["entity"] = session.get(link["type"], link["id"])
            entity_type = session.get(link["type"], link["id"]).entity_type

            for template in templates:

                if entity_type != template.name:
                    continue

                try:
                    path = os.path.abspath(
                        template.format(data)
                    ).replace("\\", "/")
                except lucidity.error.FormatError:
                    continue
                else:
                    if hasattr(template, "source"):
                        event["data"]["files"].append((template.source, path))
                    else:
                        event["data"]["directories"].append(path)

    return event


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    session.event_hub.subscribe('topic=create_structure.launch', modify_launch)
