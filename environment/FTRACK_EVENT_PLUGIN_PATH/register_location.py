import ftrack_api
import ftrack_locations


def configure_locations(event):
    '''Configure locations for session.'''
    session = event['data']['session']

    location = session.query(
        "Location where name is \"project.disk.root\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = ftrack_locations.get_new_structure()
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
