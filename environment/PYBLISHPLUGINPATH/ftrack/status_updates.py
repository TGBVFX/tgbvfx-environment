import pyblish.api


class TGBFtrackStatusUpdate(pyblish.api.InstancePlugin):
    """Update thumbnails on task and shot in Ftrack."""

    order = pyblish.api.IntegratorOrder + 1
    label = "Status Update"

    def process(self, instance):

        families = [instance.data["family"]]
        families += instance.data.get("families", [])
        if "source" in families:
            return

        asset_versions = []
        for data in instance.data.get("ftrackComponentsList", []):
            component = data.get("component", None)
            if component:
                asset_versions.append(component["version"])

        session = instance.context.data["ftrackSession"]
        status = session.query("Status where name is \"In Progress\"").one()
        for asset_version in list(set(asset_versions)):
            asset_version["status"] = status

        session.commit()
