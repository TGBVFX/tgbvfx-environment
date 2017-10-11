import getpass

import ftrack_api
from ftrack_connect.session import get_shared_session


def callback(event):
    """Status change updates."""

    session = get_shared_session()

    for entity_data in event["data"].get("entities", []):

        if entity_data["action"] != "update":
            continue

        if "keys" not in entity_data:
            continue

        if "statusid" not in entity_data["keys"]:
            continue

        new_status = session.get(
            "Status", entity_data["changes"]["statusid"]["new"]
        )

        # AssetVersion changes
        if entity_data["entityType"] == "assetversion":
            entity = session.get("AssetVersion", entity_data["entityId"])

            if new_status["name"] == "Pending Changes":
                entity["task"]["status"] = new_status

            if new_status["name"] == "Internal Approval":
                entity["task"]["status"] = new_status

            if new_status["name"] == "External Review":
                entity["task"]["status"] = new_status

            if new_status["name"] == "External Approval":
                entity["task"]["status"] = new_status

        # Task changes
        if entity_data["entityType"] == "task":

            if new_status["name"] == "Internal Review":
                items = []

                # Description
                items.append(
                    {
                        "value": "## Please select which version(s) you want "
                        "to send for \"Internal Review\".",
                        "type": "label"
                    }
                )
                items.append(
                    {
                        "value": "## The current selection are version(s) that"
                        " are in \"In Progress\".",
                        "type": "label"
                    }
                )

                assetversions = session.query(
                    "select asset.name, version, id from AssetVersion where "
                    "task.id is \"{0}\" and status.name is "
                    "\"In Progress\"".format(entity_data["entityId"])
                )
                for assetversion in assetversions:
                    items.append(
                        {
                            "value": "{0} - v{1:02d}".format(
                                assetversion["asset"]["name"],
                                assetversion["version"]
                            ),
                            "type": "label"
                        }
                    )
                    items.append(
                        {
                            "label": "",
                            "name": assetversion["id"],
                            "value": True,
                            "type": "boolean"
                        }
                    )

                assetversions = session.query(
                    "select asset.name, version, id from AssetVersion where "
                    "task.id is \"{0}\" and status.name is_not "
                    "\"In Progress\"".format(entity_data["entityId"])
                )
                for assetversion in assetversions:
                    items.append(
                        {
                            "value": "{0} - v{1:02d}".format(
                                assetversion["asset"]["name"],
                                assetversion["version"]
                            ),
                            "type": "label"
                        }
                    )
                    items.append(
                        {
                            "label": "",
                            "name": assetversion["id"],
                            "value": False,
                            "type": "boolean"
                        }
                    )

                event = ftrack_api.event.base.Event(
                    topic="ftrack.action.trigger-user-interface",
                    data={
                        "type": "form",
                        "items": items,
                        "title": "Internal Review"
                    },
                    target=(
                        "applicationId=ftrack.client.web and "
                        "user.id={0}".format(
                            event["source"]["user"]["id"]
                        )
                    )
                )
                session.event_hub.publish(event)

    session.commit()


def action_launch(event):

    if "values" not in event["data"]:
        return

    session = get_shared_session()
    status = session.query("Status where name is \"Internal Review\"").one()
    for key, value in event["data"]["values"].iteritems():
        if value:
            session.get("AssetVersion", key)["status"] = status

    session.commit()


def register(session, **kw):
    """Register event listener."""

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = (
        "topic=ftrack.update and source.applicationId=ftrack.client.web and "
        "source.user.username={0}".format(getpass.getuser())
    )
    session.event_hub.subscribe(subscription, callback)

    subscription = (
        "topic=ftrack.action.launch and "
        "source.user.username={0}".format(getpass.getuser())
    )
    session.event_hub.subscribe(subscription, action_launch)
