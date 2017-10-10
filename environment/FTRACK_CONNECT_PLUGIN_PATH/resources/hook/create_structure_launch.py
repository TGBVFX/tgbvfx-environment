import os
import shutil

import ftrack_api
from ftrack_connect.session import get_shared_session
import lucidity


def modify_launch(event):
    """Return each entities in the selection in data dictionaries."""

    session = get_shared_session()
    templates = lucidity.discover_templates()
    entity = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )
    for link in entity["link"]:

        entity = session.get(link["type"], link["id"])
        valid_templates = templates[0].get_valid_templates(
            entity, templates
        )

        for template in valid_templates:

            try:
                path = os.path.abspath(
                    template.format(entity)
                ).replace("\\", "/")
            except lucidity.error.FormatError:
                continue
            else:

                if os.path.exists(path):
                    continue

                if hasattr(template, "source"):
                    print "Copying \"{0}\" to \"{1}\"".format(
                        template.source, path
                    )
                    shutil.copy(template.source, path)
                else:
                    print "Creating \"{0}\"".format(path)
                    os.makedirs(path)


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
