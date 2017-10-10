import maya.cmds as mayaM
import maya.utils as mayaUtilsM

if not mayaM.about(batch=True):
    mayaUtilsM.executeDeferred(
        'import pipeline.maya.scripts.shelf as shelfM;shelfM.createShelves()'
    )
