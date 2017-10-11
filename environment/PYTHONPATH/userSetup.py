import maya.cmds as mayaM
import maya.utils as mayaUtilsM

if not mayaM.about(batch=True):
    mayaUtilsM.executeDeferred(
        'import tgbvfx_environment.shelves as shelves;shelves.create()'
    )
