import logging

import ftrack_api


class MyCustomAction(object):
    '''Custom action.'''

    label = 'My Action'
    identifier = 'my.custom.action'
    description = 'This is an example action'

    def __init__(self, session):
        '''Initialise action.'''
        super(MyCustomAction, self).__init__()
        self.session = session
        self.logger = logging.getLogger(
            __name__ + '.' + self.__class__.__name__
        )

    def register(self):
        '''Register action.'''
        self.session.event_hub.subscribe(
            'topic=ftrack.action.discover and source.user.username={0}'.format(
                self.session.api_user
            ),
            self.discover
        )

        self.session.event_hub.subscribe(
            'topic=ftrack.action.launch and data.actionIdentifier={0} and '
            'source.user.username={1}'.format(
                self.identifier,
                self.session.api_user
            ),
            self.launch
        )

    def discover(self, event):
        '''Return action config if triggered on a single asset version.'''
        data = event['data']

        # If selection contains more than one item return early since
        # this action can only handle a single version.
        selection = data.get('selection', [])
        self.logger.info('Got selection: {0}'.format(selection))
        if len(selection) != 1 or selection[0]['entityType'] != 'assetversion':
            return

        return {
            'items': [{
                'label': self.label,
                'description': self.description,
                'actionIdentifier': self.identifier
            }]
        }

    def launch(self, event):
        '''Callback method for custom action.'''
        selection = event['data'].get('selection', [])

        for entity in selection:

            version = self.session.get('AssetVersion', entity['entityId'])

            #DO SOMETHING WITH THE VERSION

        return {
            'success': True,
            'message': 'Ran my custom action successfully!'
        }


def register(session, **kw):
    '''Register plugin.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    action = MyCustomAction(session)
    action.register()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    session = ftrack_api.Session()
    register(session)

    # Wait for events.
    session.event_hub.wait()
