import lucidity

from tgbvfx_environment import utils


def get_test_paths():
    return [
        "//10.11.0.184/171001_ftrack/tgbvfx",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial",
        "//10.11.0.184/171001_ftrack/tgbvfx/io",
        "//10.11.0.184/171001_ftrack/tgbvfx/preproduction",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/aaf",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/audio",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/edl",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/footage",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/nukestudio",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/omf",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/qt_offline",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/xml",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/nukestudio/"
        "pipeline_test_v001.hrox",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/nukestudio/workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/client",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/graphics",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/outsource",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/references",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/setdata",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/sourcefootage",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/transcodedfootage",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/client/from_client",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/client/to_client",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/outsource/company",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/outsource/company/from_broncos",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/outsource/company/to_broncos",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/setdata/grids",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/setdata/HDRs",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/setdata/measurements",
        "//10.11.0.184/171001_ftrack/tgbvfx/io/setdata/references",
        "//10.11.0.184/171001_ftrack/tgbvfx/preproduction/moodboards",
        "//10.11.0.184/171001_ftrack/tgbvfx/preproduction/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/preproduction/storyboards",
        "//10.11.0.184/171001_ftrack/tgbvfx/preproduction/treatments",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts/"
        "pipeline_test_editing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/houdini/"
        "pipeline_test_editing_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/maya/scenes/"
        "pipeline_test_editing_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/"
        "pipeline_test_sq001_sh0010_compositing_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_plates",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_out",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/compositing/maya/scenes/"
        "pipeline_test_sq001_sh0010_compositing_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/texures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches/"
        "arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/renderScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders/"
        "comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/renders/"
        "slapcomp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts/"
        "pipeline_test_sq001_sh0010_compositing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts/"
        "workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/_plates",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini/render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/houdini/_out",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/texures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/caches/"
        "arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/maya/"
        "outputScenes/renderScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/renders/"
        "comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/renders/"
        "slapcomp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/scripts/"
        "pipeline_test_sq001_sh0020_compositing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0020/nuke/scripts/"
        "workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/_plates",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini/render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/houdini/_out",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/texures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/caches/"
        "arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/maya/"
        "outputScenes/renderScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/renders/"
        "comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/renders/"
        "slapcomp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/scripts/"
        "pipeline_test_sq002_sh0010_editing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq002/sh0010/nuke/scripts/"
        "workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/mari",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/houdini/"
        "_out",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "textures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "caches/arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/maya/"
        "outputScenes/renderScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders/comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/nuke/"
        "renders/slapcomp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0020",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0020/"
        "plate_linear_aces/sq001_sh0020_plate_linear_aces_v003.%04d.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0020/"
        "plate_linear_aces/sq001_sh0020_plate_linear_aces_v003.1001.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0020/"
        "plate_linear_aces/sq001_sh0020_plate_linear_aces_v003.%04d.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0020/"
        "plate_linear_aces/sq001_sh0020_plate_linear_aces_v003.1001.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "sq001_sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "sq001_sh0010/plateprep",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "sq001_sh0010/plateprep/sq001_sh0010_plateprep_main_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001_sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001_sh0010/"
        "plateprep",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001_sh0010/"
        "plateprep/sq001_sh0010_plateprep_BackdropNode4_main_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001_sh0010/"
        "plate001/sq001_sh0010_plate001_v001.mov"
    ]


def assert_entity(entity, templates):

    msg = "Template name: \"{0}\"".format(
        templates[0].get_template_name(entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg


def test():

    entities = []
    templates = lucidity.discover_templates()

    assert templates, "No templates discovered."

    project = utils.mock_entity(
        ("disk", {"windows": "//10.11.0.184", "unix": "//10.11.0.184"}),
        ("root", "171001_ftrack"),
        ("name", "pipeline_test"),
        entity_type="Project"
    )
    entities.append(project)

    # project/editing
    task = utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )
    entities.append(task)

    # project/editing/.hrox file
    asset = utils.mock_entity(
        ("parent", project),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".hrox"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/editing/.nk file
    asset = utils.mock_entity(
        ("parent", project),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/editing/.hip file
    asset = utils.mock_entity(
        ("parent", project),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".hip"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/editing/.mb file
    asset = utils.mock_entity(
        ("parent", project),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".mb"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001
    sequence = utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "sq001"),
        entity_type="Sequence"
    )
    entities.append(sequence)

    # project/sq001/sh0010
    shot = utils.mock_entity(
        ("parent", sequence),
        ("project", project),
        ("name", "sh0010"),
        entity_type="Shot"
    )
    entities.append(shot)

    # project/sq001/sh0010/compositing
    task = utils.mock_entity(
        ("parent", shot),
        ("project", project),
        ("name", "compositing"),
        entity_type="Task"
    )

    # project/sq001/sh0010/compositing/.nk file
    asset = utils.mock_entity(
        ("parent", shot),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.hip file
    asset = utils.mock_entity(
        ("parent", shot),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".hip"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.mov file
    assettype = utils.mock_entity(
        ("short", "mov"),
        entity_type="Asset"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "plate001"}),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".mov"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/compositing/.mb file
    asset = utils.mock_entity(
        ("parent", shot),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".mb"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/plateprep/.gizmo file
    task = utils.mock_entity(
        ("project", project),
        ("name", "plateprep"),
        entity_type="Task"
    )
    assettype = utils.mock_entity(
        ("short", "nuke_gizmo"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        ("type", assettype),
        entity_type="Asset"
    )
    entities.append(asset)

    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    entities.append(assetversion)

    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".gizmo"),
        ("name", "main"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0010/plateprep/.nk backdrop file
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        ("type", assettype),
        entity_type="Asset"
    )
    entities.append(asset)

    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "BackdropNode4"}),
        entity_type="AssetVersion"
    )
    entities.append(assetversion)

    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        ("name", "main"),
        ("metadata", {"lucidity_template_name": "nuke_backdrop"}),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0020
    shot = utils.mock_entity(
        ("parent", sequence),
        ("project", project),
        ("name", "sh0020"),
        entity_type="Shot"
    )
    entities.append(shot)

    # project/sq001/sh0020/compositing/.nk file
    task = utils.mock_entity(
        ("parent", shot),
        ("project", project),
        ("name", "compositing"),
        entity_type="Task"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        entity_type="FileComponent"
    )
    entities.append(component)

    # project/sq001/sh0020/compositing/.exr sequence
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        ("type", assettype),
        entity_type="Asset"
    )
    entities.append(asset)

    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 3),
        ("metadata", {"instance_name": "plate_linear_aces"}),
        entity_type="AssetVersion"
    )
    sequence_component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".exr"),
        ("padding", 4),
        entity_type="SequenceComponent"
    )
    entities.append(sequence_component)

    file_component = utils.mock_entity(
        ("version", None),
        ("container", sequence_component),
        ("file_type", ".exr"),
        ("name", "1001"),
        entity_type="FileComponent"
    )
    entities.append(file_component)

    # project/sq001/sh0020/compositing/.jpg sequence
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        ("type", assettype),
        entity_type="Asset"
    )
    entities.append(asset)

    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 3),
        ("metadata", {"instance_name": "plate_linear_aces"}),
        entity_type="AssetVersion"
    )
    sequence_component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".jpg"),
        ("padding", 4),
        entity_type="SequenceComponent"
    )
    entities.append(sequence_component)

    file_component = utils.mock_entity(
        ("version", None),
        ("container", sequence_component),
        ("file_type", ".jpg"),
        ("name", "1001"),
        entity_type="FileComponent"
    )
    entities.append(file_component)

    # project/sq002
    sequence = utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "sq002"),
        entity_type="Sequence"
    )
    entities.append(sequence)

    # project/sq002/sh0010
    shot = utils.mock_entity(
        ("parent", sequence),
        ("project", project),
        ("name", "sh0010"),
        entity_type="Shot"
    )
    entities.append(shot)

    # project/sq002/sh0020/editing/.nk file
    task = utils.mock_entity(
        ("parent", shot),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )
    asset = utils.mock_entity(
        ("parent", shot),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    component = utils.mock_entity(
        ("version", assetversion),
        ("file_type", ".nk"),
        entity_type="FileComponent"
    )
    entities.append(component)

    template_paths = []
    used_templates = []
    for entity in entities:
        assert_entity(entity, templates)
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

        for template in valid_templates:
            try:
                template_paths.append(template.format(entity))
            except lucidity.error.FormatError as e:
                msg = e.message + "\nTemplate name: {0}".format(template.name)
                raise type(e)(msg)

    # Cover proposed paths
    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in paths:
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in template_paths:
        msg += "\n{0}".format(path)
    assert not paths, msg

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg
