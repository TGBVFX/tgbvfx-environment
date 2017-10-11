import maya.cmds as mayaM
import maya.mel as melM


def create():

    # TGBVFX_ANIMATION shelf
    shelfName = 'TGBVFX_ANIMATION'
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
        image='studiolibrary_logo.png',
        label='Studio Library',
        annotation='Studio Library',
        imageOverlayLabel='Studio Library',
        overlayLabelColor=[1, 1, 1],
        overlayLabelBackColor=[0, 0, 0, 1],
        command="import studiolibrary;studiolibrary.main()"
    )

    mayaM.shelfButton(
        parent=shelf,
        image='aweControlPicker.png',
        annotation='aweControlPicker',
        label='aweControlPicker',
        command="source \"aweControlPicker.mel\";aweControlPicker;",
        sourceType="mel"
    )

    mayaM.shelfTabLayout(gShelfTopLevel, edit=True, selectTab=shelfName)

    # TGBVFX shelf
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
        command='mayaUtilsM.executeDeferred("import tgbvfx_environment.shelves'
        ' as shelves;reload(shelves);shelves.create()")'
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
