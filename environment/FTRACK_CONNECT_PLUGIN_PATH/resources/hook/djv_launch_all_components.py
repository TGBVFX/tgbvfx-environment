import logging

import ftrack

log = logging.getLogger(__name__)


def modify_launch(event):
    """Returns all components for the DJV launch"""

    # Collect non-latest components
    data = {}
    for item in event["data"].get("selection", []):

        versions = []
        component_names = []

        # Add latest version of "img" and "mov" type from tasks.
        if item["entityType"] == "task":
            task = ftrack.Task(item["entityId"])
            for asset in task.getAssets(assetTypes=["img", "mov"]):
                versions.extend(reversed(asset.getVersions()[:-1]))

                # Get latest version component names for exclusion, because
                # it is already being added by the public djv plugin.
                for component in asset.getVersions()[-1].getComponents():
                    component_names.append(component.getName())

        for version in versions:
            for component in version.getComponents():
                if component.getName() in component_names:
                    continue
                else:
                    component_names.append(component.getName())

                component_list = data.get(component.getName(), [])
                component_list.append(component)
                data[component.getName()] = component_list

                label = "v{0} - {1} - {2}"
                label = label.format(
                    str(version.getVersion()).zfill(3),
                    version.getAsset().getType().getName(),
                    component.getName()
                )

                file_path = component.getFilesystemPath()
                if component.isSequence():
                    if component.getMembers():
                        frame = int(component.getMembers()[0].getName())
                        file_path = file_path % frame

                event["data"]["items"].append(
                    {"label": label, "value": file_path}
                )

    return event


def register(registry, **kw):
    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    ftrack.EVENT_HUB.subscribe("topic=djvview.launch", modify_launch)
