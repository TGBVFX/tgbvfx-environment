import ftrack_api
import ftrack_connect_nuke_studio.processor


class ScenePlugin(ftrack_connect_nuke_studio.processor.ProcessorPlugin):
    """Publish the Nuke Studio project"""

    def __init__(self, session, *args, **kwargs):
        """Initialise processor."""
        super(ScenePlugin, self).__init__(
            *args, **kwargs
        )

        self.session = session

        self.name = "processor.scene"
        self.defaults = {
            'OUT': {
                'file_type': 'hrox'
            }
        }

    def discover(self, event):
        """Return discover data for *event*."""
        data = {
            "defaults": self.defaults,
            "name": "Scene",
            "processor_name": self.name,
            "asset_name": "scene"
        }

        data["process"] = True

        return data

    def launch(self, event):
        """Launch processor from *event*."""
        project_entity = self.session.query(
            'Project where id is "{0}"'.format(
                event['data']['input']['entity_id']
            )
        ).one()

        asset = None
        assettype_entity = self.session.query(
            'AssetType where short is "scene"'
        ).one()

        try:
            query = 'Asset where parent.id is "{0}" and type.short is "scene"'
            query += ' and name is "nukestudio"'
            asset = self.session.query(
                query.format(project_entity['id'])
            ).one()
        except:
            asset = self.session.create(
                'Asset',
                {
                    'name': 'nukestudio',
                    'type': assettype_entity,
                    'parent': project_entity
                }
            )

        task = None
        try:
            query = 'Task where parent.id is "{0}" and type.name is "Editing"'
            query += ' and name is "editing"'
            task = self.session.query(query.format(project_entity['id'])).one()
        except:
            tasktype = self.session.query('Type where name is "Editing"').one()
            task = self.session.create(
                "Task",
                {'parent': project_entity, 'type': tasktype, 'name': 'editing'}
            )

        asset_version = self.session.create(
            'AssetVersion', {
                'asset': asset,
                'task': task
            }
        )

        self.session.commit()

        file_path = event['data']['input']['application_object'].path()
        asset_version.create_component(
            file_path, location='auto'
        )

        self.session.commit()

    def register(self):
        """Register processor"""
        self.session.event_hub.subscribe(
            "topic=ftrack.processor.discover and "
            "data.object_type=show",
            self.discover
        )
        self.session.event_hub.subscribe(
            "topic=ftrack.processor.launch and data.name={0}".format(
                self.name
            ),
            self.launch
        )


def register(session, **kw):
    """Register plugin. Called when used as an plugin."""
    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an old or incompatible API and
    # return without doing anything.
    if not isinstance(session, ftrack_api.session.Session):
        return

    plugin = ScenePlugin(
        session
    )

    plugin.register()
