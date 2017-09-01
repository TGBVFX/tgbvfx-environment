import pyblish.api


class TGBFtrackRepairCurrentFile(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def nukestudio_save(self, path):
        import hiero
        hiero.ui.activeSequence().project().saveAs(path)

    def process(self, context, plugin):
        from tgbvfx_environment import utils
        import os

        work_file = utils.get_work_file(
            context.data["ftrackSession"],
            context.data["ftrackTask"],
            pyblish.api.current_host(),
            context.data["version"]
        )

        msg = (
            "Can't save file because \"{0}\" already exists. Please resolve "
            "this manually."
        )
        assert not os.path.exists(work_file), msg.format(work_file)

        application_save = {"nukestudio": self.nukestudio_save}
        application_save[pyblish.api.current_host()](work_file)


class TGBFtrackValidateCurrentFile(pyblish.api.ContextPlugin):
    """Validate the current file directory against the studio templates."""

    order = pyblish.api.ValidatorOrder
    label = "Current File"
    actions = [TGBFtrackRepairCurrentFile]
    optional = True
    hosts = ["nuke"]

    def process(self, context):
        import os
        from tgbvfx_environment import utils

        # Ignore this validator when there is no ftrack task. Below validator
        # will flag the issue.
        if not context.data["ftrackTask"]:
            return

        work_file = utils.get_work_file(
            context.data["ftrackSession"],
            context.data["ftrackTask"],
            pyblish.api.current_host(),
            context.data["version"]
        )
        current_file = os.path.abspath(
            context.data["currentFile"]
        ).replace("\\", "/")

        msg = "Current file \"{0}\" is not at expected path \"{1}\"".format(
            current_file, work_file
        )
        assert work_file == current_file, msg


class TGBFtrackValidateTask(pyblish.api.ContextPlugin):
    """Validate the application is launched from a task."""

    order = pyblish.api.ValidatorOrder
    label = "Ftrack Task"

    def process(self, context):

        msg = (
            "Could not find Ftrack task. Please launch from a task in Ftrack."
        )
        assert context.data["ftrackTask"], msg
