import os

import ftrack_api
import lucidity
import filelink


class FilelinkLocationMixin(object):
    '''Location that does not manage data.'''

    def _add_data(self, component, resource_identifier, source):
        '''Manage transfer of *component* data from *source*.

        *resource_identifier* specifies the identifier to use with this
        locations accessor.

        Most of the code is coming from the Location entity.
        '''

        # Read data from source and write to this location.
        if not source.accessor:
            raise ftrack_api.exception.LocationError(
                'No accessor defined for source location {location}.',
                details=dict(location=source)
            )

        if not self.accessor:
            raise ftrack_api.exception.LocationError(
                'No accessor defined for target location {location}.',
                details=dict(location=self)
            )

        is_container = 'members' in component.keys()
        if is_container:
            # TODO: Improve this check. Possibly introduce an inspection
            # such as ftrack_api.inspection.is_sequence_component.
            if component.entity_type != 'SequenceComponent':
                self.accessor.make_container(resource_identifier)

        else:
            # Try to make container of component.
            try:
                container = self.accessor.get_container(
                    resource_identifier
                )

            except ftrack_api.exception.AccessorParentResourceNotFoundError:
                # Container could not be retrieved from
                # resource_identifier. Assume that there is no need to
                # make the container.
                pass

            else:
                # No need for existence check as make_container does not
                # recreate existing containers.
                self.accessor.make_container(container)

            if self.accessor.exists(resource_identifier):
                # Note: There is a race condition here in that the
                # data may be added externally between the check for
                # existence and the actual write which would still
                # result in potential data loss. However, there is no
                # good cross platform, cross accessor solution for this
                # at present.
                raise ftrack_api.exception.LocationError(
                    'Cannot add component as data already exists and '
                    'overwriting could result in data loss. Computed '
                    'target resource identifier was: {0}'
                    .format(resource_identifier)
                )

            # Write data.
            filelink.create(
                source.get_resource_identifier(component),
                os.path.abspath(
                    os.path.join(self.accessor.prefix, resource_identifier)
                )
            )


class Structure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()

        valid_templates = templates[0].get_valid_templates(entity, templates)
        if valid_templates:
            return valid_templates[0].format(entity)

        msg = (
            'Could not find any templates for {0} with template name "{1}".'
        )
        raise ValueError(
            msg.format(entity, templates[0].get_template_name(entity))
        )


def configure_locations(event):
    '''Configure locations for session.'''
    session = event['data']['session']

    location = session.query(
        "Location where name is \"lucidity\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50
    ftrack_api.mixin(location, FilelinkLocationMixin, name="FilelinkLocation")


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
