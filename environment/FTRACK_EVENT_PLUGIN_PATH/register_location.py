import os

import ftrack_api
import lucidity


class Structure(ftrack_api.structure.base.Structure):

    def get_host(self):

        host = "*"

        # Nuke
        try:
            import nuke
            if "--hiero" in nuke.rawArgs or "--studio" in nuke.rawArgs:
                raise ImportError
            host = "nuke"
        except ImportError:
            pass

        # NukeStudio
        try:
            import nuke
            if "--studio" not in nuke.rawArgs:
                raise ImportError
            host = "nukestudio"
        except ImportError:
            pass

        return host

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()

        if hasattr(entity["version"], "get"):
            metadata = entity["version"].get("metadata", None)
            if metadata:
                for template in templates:
                    template_name = entity["version"]["metadata"].get(
                        "template", ""
                    )
                    if template.name == template_name:
                        return os.path.abspath(
                            template.ftrack_format(entity)
                        )

        template_name = templates[0].get_template_name(entity)
        host = self.get_host()
        for template in templates:
            if template_name == template.name and host in template.hosts:
                return os.path.abspath(
                    template.ftrack_format(entity, host=host)
                )

        msg = (
            'Could not find any templates for {0} with template name "{1}" '
            'and host "{2}".'
        )
        raise ValueError(msg.format(entity, template_name, host))


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
