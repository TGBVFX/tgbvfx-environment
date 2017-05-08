import os

import ftrack_api
import nuke


def init():
    session = ftrack_api.Session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])
    fps = task["parent"]["custom_attributes"]["fps"]

    msg = "tgvvfx-environment\environment\NUKE_PATH: Setting FPS to {0}."
    print msg.format(fps)
    nuke.root()["fps"].setValue(fps)


nuke.addOnScriptLoad(init)
