from tgbvfx_environment import utils
import test_project_templates as tpt
import lib


def get_project_sequence():
    return utils.mock_entity(
        ("parent", tpt.get_project()),
        ("project", tpt.get_project()),
        ("name", "sq001"),
        entity_type="Sequence"
    )


def test_project_sequence():
    lib.assert_entity(get_project_sequence())


def get_project_sequence_shot():
    return utils.mock_entity(
        ("parent", get_project_sequence()),
        ("project", tpt.get_project()),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_sequence_shot():
    lib.assert_entity(get_project_sequence_shot())


def get_project_sequence_shot_task():
    return utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("project", tpt.get_project()),
        ("version", 1),
        ("name", "compositing"),
        entity_type="Task"
    )


def get_project_sequence_shot_task_workfiles():
    entities = []
    for ext in lib.get_workfile_extensions():
        entity = utils.mock_entity(
            ("parent", get_project_sequence_shot()),
            ("project", tpt.get_project()),
            ("version", 1),
            ("file_type", ext),
            ("name", "compositing"),
            entity_type="Task"
        )
        entities.append(entity)
    return entities


def test_project_sequence_shot_task_workfiles():
    for entity in get_project_sequence_shot_task_workfiles():
        lib.assert_entity(entity)


def get_project_sequence_shot_task_files():
    entities = []

    # project/sq001/sh0010/compositing/.gizmo
    assettype = utils.mock_entity(
        ("short", "nuke_gizmo"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "Group1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".gizmo"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.nk file
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "BackdropNode1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".nk"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.mov file
    assettype = utils.mock_entity(
        ("short", "mov"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "write1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".mov"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.mov file
    assettype = utils.mock_entity(
        ("short", "mov"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "write1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".R3D"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.psd file
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "write1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".psd"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.abc file
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "writegeo1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".abc"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.fbx file
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "writegeo1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".fbx"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.abc camera file
    assettype = utils.mock_entity(
        ("short", "camera"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".abc"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.abc model file
    assettype = utils.mock_entity(
        ("short", "model"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "writegeo1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".abc"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.mb file
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "set1_mayaBinary"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".mb"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.ma file
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", get_project_sequence_shot()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_sequence_shot_task()),
        ("version", 1),
        ("metadata", {"instance_name": "set1_mayaAscii"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".ma"),
        entity_type="FileComponent"
    )
    entities.append(component)

    return entities


def test_project_sequence_shot_task_files():
    for entity in get_project_sequence_shot_task_files():
        lib.assert_entity(entity)


def get_project_sequence_shot_task_imagefiles():
    entities = []

    # project/sq001/sh0010/compositing imagefiles
    for ext in lib.get_imagefile_extensions():
        assettype = utils.mock_entity(
            ("short", "img"),
            entity_type="AssetType"
        )
        asset = utils.mock_entity(
            ("parent", get_project_sequence_shot()),
            ("type", assettype),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", get_project_sequence_shot_task()),
            ("version", 1),
            ("metadata", {"instance_name": "Write1"}),
            entity_type="AssetVersion"
        )
        sequence_component = utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ext),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
        entities.append(sequence_component)

        file_component = utils.mock_entity(
            ("version", None),
            ("container", sequence_component),
            ("file_type", ext),
            ("name", "1001"),
            entity_type="FileComponent"
        )
        entities.append(file_component)

    return entities


def test_project_folder_sequence_shot_task_imagefiles():
    for entity in get_project_sequence_shot_task_imagefiles():
        lib.assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project_sequence())
    entities.append(get_project_sequence_shot())
    entities.extend(get_project_sequence_shot_task_files())
    entities.extend(get_project_sequence_shot_task_workfiles())
    entities.extend(get_project_sequence_shot_task_imagefiles())

    return entities
