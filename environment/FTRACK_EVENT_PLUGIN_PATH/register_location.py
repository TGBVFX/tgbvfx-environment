import os

import ftrack_api
import lucidity


class Structure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()
        data = {}

        data["entity"] = entity

        # Convert the integer version to string.
        data["entity"]["version"]["version"] = str(
            entity["version"]["version"]
        ).zfill(3)

        for template in templates:
            if template.name == entity["file_type"]:
                return os.path.abspath(template.format(data))

        raise ValueError("Could not find any templates for {0}".format(entity))


def configure_locations(event):
    '''Configure locations for session.'''
    session = event['data']['session']

    location = session.query(
        "Location where name is \"lucidity\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50


def register(session):

    # Validate that session is an instance of ftrack_api.Session. If not,assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    session.event_hub.subscribe(
        'topic=ftrack.api.session.configure-location',
        configure_locations
    )
