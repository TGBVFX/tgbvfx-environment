import os

import ftrack_api
import lucidity


class Structure(ftrack_api.structure.base.Structure):

    data = {}

    def get_resource_identifier(self, entity, context=None):

        templates = lucidity.discover_templates()

        self.data["entity"] = entity

        path = lucidity.format(self.data, templates)[0].replace("\\", "/")

        return os.path.abspath(path)


def get_location():

    session = ftrack_api.Session()
    location = session.query(
        "Location where name is \"lucidity\""
    ).one()
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50
    return location
