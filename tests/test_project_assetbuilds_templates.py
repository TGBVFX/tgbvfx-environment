from tgbvfx_environment import utils
import test_project_templates as tpt
import lib


def get_project_assetbuild():
    assetbuildtype = utils.mock_entity(
        ("name", "Character"),
        entity_type="Type"
    )
    project = tpt.get_project()
    return utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "lizard"),
        ("type", assetbuildtype),
        entity_type="AssetBuild"
    )


def test_project_assetbuild():
    lib.assert_entity(get_project_assetbuild())


def get_project_assetbuild_task():
    return utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("project", tpt.get_project()),
        ("version", 1),
        ("name", "lookdev"),
        entity_type="Task"
    )


def get_project_assetbuild_task_workfiles():
    entities = []
    for ext in lib.get_workfile_extensions():
        entity = utils.mock_entity(
            ("parent", get_project_assetbuild()),
            ("project", tpt.get_project()),
            ("version", 1),
            ("file_type", ext),
            ("name", "lookdev"),
            entity_type="Task"
        )
        entities.append(entity)
    return entities


def test_project_assetbuild_task_workfiles():
    for entity in get_project_assetbuild_task_workfiles():
        lib.assert_entity(entity)


def get_project_assetbuild_task_files():
    entities = []

    # project/lizard/lookdev/.gizmo
    assettype = utils.mock_entity(
        ("short", "nuke_gizmo"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
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

    # project/lizard/lookdev/.nk
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
        ("version", 1),
        ("metadata", {"instance_name": "BackdropNode1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        ("name", "main"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/lizard/lookdev/.abc
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
        ("version", 1),
        ("metadata", {"instance_name": "WriteGeo1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".abc"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/lizard/lookdev/.fbx
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
        ("version", 1),
        ("metadata", {"instance_name": "WriteGeo1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".fbx"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/lizard/lookdev/.mb
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
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

    # project/lizard/lookdev/.ma
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
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

    # project/lizard/lookdev/.mov
    assettype = utils.mock_entity(
        ("short", "mov"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
        ("version", 1),
        ("metadata", {"instance_name": "Write1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".mov"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/lizard/lookdev/.psd
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="AssetType"
    )
    asset = utils.mock_entity(
        ("parent", get_project_assetbuild()),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", get_project_assetbuild_task()),
        ("version", 1),
        ("metadata", {"instance_name": "Write1"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("name", "main"),
        ("file_type", ".psd"),
        entity_type="FileComponent"
    )
    entities.append(component)

    return entities


def test_project_assetbuild_task_files():
    for entity in get_project_assetbuild_task_files():
        lib.assert_entity(entity)


def get_project_assetbuild_task_image_files():
    entities = []

    # project/lizard/lookdev imagefiles
    for ext in lib.get_imagefile_extensions():
        assettype = utils.mock_entity(
            ("short", "img"),
            entity_type="AssetType"
        )
        asset = utils.mock_entity(
            ("parent", get_project_assetbuild()),
            ("type", assettype),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", get_project_assetbuild_task()),
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


def test_project_assetbuild_task_images_files():
    for entity in get_project_assetbuild_task_image_files():
        lib.assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project_assetbuild())
    entities.extend(get_project_assetbuild_task_workfiles())
    entities.extend(get_project_assetbuild_task_files())
    entities.extend(get_project_assetbuild_task_image_files())

    return entities
