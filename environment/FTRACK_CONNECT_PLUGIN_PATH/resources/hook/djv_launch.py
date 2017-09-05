import os

import ftrack_api
from ftrack_connect.session import get_shared_session
import lucidity
import clique


def modify_launch(event):
    """Return each entities in the selection in data dictionaries."""

    session = get_shared_session()
    templates = lucidity.discover_templates()

    file_paths = []
    paths_searched = []
    for item in event["data"].get("selection", []):
        entity = session.get(item["entityType"].title(), item["entityId"])
        template_name = templates[0].get_template_name(entity["parent"])
        for template in templates:
            if template.name == template_name:
                path = template.format(entity["parent"])
                for root, subFolder, files in os.walk(path):
                    path = os.path.abspath(root)
                    if path in paths_searched:
                        continue
                    else:
                        paths_searched.append(path)
                    for f in files:
                        if not f.endswith(".exr"):
                            continue
                        file_paths.append(
                            os.path.abspath(os.path.join(root, f))
                        )

    collections = clique.assemble(list(set(file_paths)))[0]
    for collection in collections:
        event["data"]["items"].append(
            {
                "label": os.path.basename(collection.format()),
                "value": list(collection)[0]
            }
        )

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
    session.event_hub.subscribe('topic=djvview.launch', modify_launch)
