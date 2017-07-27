class mock_entity(dict):
    """Mock entity for faking Ftrack entities

    Requires keyword argument "entity_type" on creation.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, args)

        if "entity_type" not in kwargs.keys():
            raise ValueError('Need the keyword argument "entity_type"')

        self.__dict__ = kwargs


def get_work_file(session, task, application, version):
    """Gets the assumed path to the work file of the application."""

    components = session.query(
        'Component where version.task_id is "{0}" and '
        'version.asset.name is "{1}" and name is "{2}"'.format(
            task["id"], task["name"], application
        )
    )

    component = None
    for entity in components:
        if entity["version"]["version"] > version:
            version = entity["version"]["version"]
            component = entity

    extension_mapping = {
        ".hrox": "nukestudio",
        ".nk": "nuke",
        ".mb": "maya",
        ".hip": "houdini"
    }
    extension = None
    for key, value in extension_mapping.iteritems():
        if value == application:
            extension = key
    if not component:
        # Faking an Ftrack component for the location structure.
        asset = mock_entity(("parent", task["parent"]), entity_type="Asset")
        assetversion = mock_entity(
            ("version", version),
            ("task", task),
            ("asset", asset),
            entity_type="AssetVersion"
        )
        component = mock_entity(
            ("version", assetversion),
            ("file_type", extension),
            entity_type="FileComponent"
        )

    location = session.pick_location()
    return location.structure.get_resource_identifier(component)
