# :coding: utf-8
# :copyright: Copyright (c) 2015 ftrack

import sys
import argparse
import logging
import threading

import ftrack


def async(fn):
    '''Run *fn* asynchronously.'''
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


def getEntity(entityId, entityType):
    '''Return entity based on *entityId* and *entityType*.'''
    entity = None

    if entityType == ftrack.Project._type:
        entity = ftrack.Project(entityId)
    elif entityType == ftrack.Task._type:
        entity = ftrack.Task(entityId)
    elif entityType == 'assetversion':
        entity = ftrack.AssetVersion(entityId)

    if not entity:
        logging.warning(
            u'Entity ({0}, {1}) not a valid type, skipping..'
            .format(entityId, entityType)
        )

    return entity


@async
def findAndReplace(selection, attribute, find, replace):
    '''Find and replace *find* and *replace* in *attribute* for *selection*.'''

    for item in selection:
        entity = getEntity(item['entityId'], item['entityType'])

        if entity:
            if attribute in entity.keys():
                value = entity.get(attribute)

                if isinstance(value, basestring):
                    value = value.replace(find, replace)

                    entity.set(attribute, value)


class FindAndReplace(ftrack.Action):
    '''Find and replace text in attribute action.'''

    #: Action identifier.
    identifier = 'com.ftrack.find-and-replace'  # Unique identifier for your action.

    #: Action label.
    label = 'Find and replace'  # Action label which the user will see in the interface.

    def launch(self, event):
        '''Callback method for action.'''
        selection = event['data'].get('selection', [])
        self.logger.info(u'Launching action with selection {0}'.format(selection))

        # Validate selection and abort if not valid
        if not self.validateSelection(selection):
            self.logger.warning('Selection is not valid, aborting action')
            return

        data = event['data']

        if (
            'values' not in data or not (
                data['values'].get('attribute') and
                data['values'].get('find') and
                data['values'].get('replace')
            )
        ):

            # Valid attributes to update.
            attributes = [{
                'label': 'Name',
                'value': 'name'
            }, {
                'label': 'Description',
                'value': 'description'
            }, {
                'label': 'Custom attribute',
                'value': 'custom_attribute'
            },{
                'label': 'Main file path',
                'value': 'main_file_path'
            }]

            return {
                'items': [{
                    'label': 'Attribute',
                    'type': 'enumerator',
                    'name': 'attribute',
                    'value': attributes[0]['value'],
                    'data': attributes
                }, {
                    'type': 'text',
                    'label': 'Find',
                    'name': 'find'
                }, {
                    'type': 'text',
                    'label': 'Replace',
                    'name': 'replace'
                }]
            }

        attribute = data['values'].get('attribute')
        find = data['values'].get('find')
        replace = data['values'].get('replace')

        findAndReplace(
            selection, attribute, find, replace
        )

        return {
            'success': True,
            'message': 'Find and replace "{0}" with "{1}" on attribute "{2}"'.format(
                str(find), str(replace), attribute
            )
        }

    def discover(self, event):
        '''Return action config.'''
        selection = event['data'].get('selection', [])
        self.logger.info(u'Discovering action with selection: {0}'.format(selection))

        # validate selection, and only return action if it is valid.
        if self.validateSelection(selection):
            return super(FindAndReplace, self).discover(event)

    def validateSelection(self, selection):
        '''Return True if *selection* is valid'''
        # Replace with custom logic for validating selection.
        # For example check the length or entityType of items in selection.
        return True


def register(registry, **kw):
    '''Register action. Called when used as an event plugin.'''
    logger = logging.getLogger(
        'com.ftrack.find-and-replace'
    )

    # Validate that registry is an instance of ftrack.Registry. If not,
    # assume that register is being called from a new or incompatible API and
    # return without doing anything.
    if not isinstance(registry, ftrack.Registry):
        logger.debug(
            'Not subscribing plugin as passed argument {0!r} is not an '
            'ftrack.Registry instance.'.format(registry)
        )
        return

    action = FindAndReplace()
    action.register()


def main(arguments=None):
    '''Set up logging and register action.'''
    if arguments is None:
        arguments = []

    parser = argparse.ArgumentParser()
    # Allow setting of logging level from arguments.
    loggingLevels = {}
    for level in (
        logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING,
        logging.ERROR, logging.CRITICAL
    ):
        loggingLevels[logging.getLevelName(level).lower()] = level

    parser.add_argument(
        '-v', '--verbosity',
        help='Set the logging output verbosity.',
        choices=loggingLevels.keys(),
        default='info'
    )
    namespace = parser.parse_args(arguments)

    # Set up basic logging
    logging.basicConfig(level=loggingLevels[namespace.verbosity])

    # Subscribe to action.
    ftrack.setup()
    action = FindAndReplace()
    action.register()

    # Wait for events
    ftrack.EVENT_HUB.wait()

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
