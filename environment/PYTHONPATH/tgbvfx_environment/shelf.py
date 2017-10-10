import maya.cmds as mayaM
import maya.mel as melM


def createShelves():
    tgbvfx()


def tgbvfx():
    shelfName = 'TGBVFX'
    if mayaM.shelfLayout(shelfName, exists=True):
        mayaM.deleteUI(shelfName)

    melM.eval('global string $gShelfTopLevel')
    gShelfTopLevel = melM.eval('$temp = $gShelfTopLevel')
    if gShelfTopLevel:
        shelf = mayaM.shelfLayout(
            shelfName, parent=gShelfTopLevel, style='iconOnly'
        )
    else:
        shelf = mayaM.shelfLayout(shelfName, style='iconOnly')

    mayaM.shelfButton(
        parent=shelf,
        image='reloadShelf.png',
        label='Reload Shelf',
        annotation='Reload Shelf',
        command='mayaUtilsM.executeDeferred("import pipeline.maya'
        '.scripts.shelf as shelfM;reload(shelfM);shelfM.tgbvfx()")'
    )

    mayaM.shelfButton(
        parent=shelf,
        image='transparent.png',
        label='',
        annotation='',
        imageOverlayLabel=''
    )

    mayaM.shelfButton(
        parent=shelf,
        image='assetSystem.png',
        label='Publish Asset',
        annotation='Publish Asset',
        imageOverlayLabel='Publish',
        overlayLabelColor=[1, 1, 1],
        overlayLabelBackColor=[0, 0, 0, 1],
        command='import assetPublish as assetPublishM;reload(assetPublishM);'
        'assetPublishM.main()'
    )
    mayaM.shelfButton(
        parent=shelf,
        image='assetSystem.png',
        label='Load Asset',
        annotation='Load Asset',
        imageOverlayLabel='Load',
        overlayLabelColor=[1, 1, 1],
        overlayLabelBackColor=[0, 0, 0, 1],
        command='import assetLoad as assetLoadM;reload(assetLoadM);'
        'assetLoadM.main()'
    )
    mayaM.shelfButton(
        parent=shelf,
        image='assetSystem.png',
        label='Manage Asset',
        annotation='Manage Asset',
        imageOverlayLabel='Manage',
        overlayLabelColor=[1, 1, 1],
        overlayLabelBackColor=[0, 0, 0, 1],
        command='import assetManage as assetManageM;reload(assetManageM);'
        'assetManageM.main()'
    )

    mayaM.shelfButton(
        parent=shelf,
        image='transparent.png',
        label='',
        annotation='',
        imageOverlayLabel=''
    )

    mayaM.shelfButton(
        parent=shelf,
        image='sceneGraph.png',
        label='SceneGraph',
        command='import sceneGraph as sceneGraphM;reload(sceneGraphM);'
        'sceneGraphM.main()'
    )

    mayaM.shelfTabLayout(gShelfTopLevel, edit=True, selectTab=shelfName)
