import os

import lucidity

import test_project_templates as tpt
import test_project_assetbuilds_templates as tpat
import test_project_folder_assetbuilds_templates as tpfat
import test_project_sequence_templates as tpst
import test_project_folder_sequence_templates as tpfst


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
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop/files",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/_ASSET_TEMPLATE/"
        "photoshop/rendered",
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
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing",
        "//10.11.0.184/171001_ftrack/tgbvfx/editorial/nukestudio/"
        "pipeline_test_v001.hrox",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/nuke/scripts/"
        "pipeline_test_editing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/houdini/"
        "pipeline_test_editing_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/editing/maya/scenes/"
        "pipeline_test_editing_v001.mb",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/editing/Group1/"
        "Group1_v001.gizmo",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/mari",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/"
        "_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/_plates",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop/files",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/photoshop/"
        "rendered",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/houdini/_out",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "textures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "caches/arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "outputScenes/renderScenes",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts/workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders/comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "renders/slapcomp",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nukestudio/"
        "pipeline_test_lizard_lookdev_v001.hrox",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/"
        "houdini/pipeline_test_lizard_lookdev_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/maya/"
        "scenes/pipeline_test_lizard_lookdev_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/lizard/nuke/"
        "scripts/pipeline_test_lizard_lookdev_v001.nk",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "lizard/lookdev/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/"
        "lizard/lookdev/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/lizard/lookdev/"
        "BackdropNode1/BackdropNode1_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "lizard/lookdev/WriteGeo1/WriteGeo1_v001.abc",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "lizard/lookdev/WriteGeo1/WriteGeo1_v001.fbx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "lizard/lookdev/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "lizard/lookdev/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/lizard/"
        "lookdev/Write1/Write1_v001.mov",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/lizard/"
        "lookdev/Write1/Write1_v001.psd",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.%04d.hdr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "lizard/lookdev/Write1_v001/"
        "Write1_v001.1001.hdr",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/mari",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "_plates",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop/files",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/photoshop/"
        "rendered",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/houdini/"
        "_out",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "textures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "caches/arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "outputScenes/renderScenes",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts/workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders/comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "renders/slapcomp",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/"
        "houdini/pipeline_test_castle_lookdev_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/maya/"
        "scenes/pipeline_test_castle_lookdev_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nuke/"
        "scripts/pipeline_test_castle_lookdev_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_dev/castle/nukestudio/"
        "pipeline_test_castle_lookdev_v001.hrox",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/"
        "castle/lookdev/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/castle/lookdev/"
        "Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/castle/lookdev/"
        "BackdropNode1/BackdropNode1_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "castle/lookdev/WriteGeo1/WriteGeo1_v001.abc",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/"
        "castle/lookdev/WriteGeo1/WriteGeo1_v001.fbx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "castle/lookdev/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/"
        "castle/lookdev/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/castle/lookdev/"
        "Write1/Write1_v001.mov",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/castle/lookdev/"
        "Write1/Write1_v001.psd",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.%04d.hdr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/"
        "castle/lookdev/Write1_v001/"
        "Write1_v001.1001.hdr",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/nuke/scripts/"
        "pipeline_test_sq001_compositing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/nukestudio/"
        "pipeline_test_sq001_compositing_v001.hrox",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/maya/scenes/"
        "pipeline_test_sq001_compositing_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/houdini/"
        "pipeline_test_sq001_compositing_v001.hip",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/sq001/"
        "compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/sq001/"
        "compositing/Group1/Group1_v001.gizmo",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/mari",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_plates",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/_references",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop/files",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/photoshop/"
        "rendered",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/_out",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "workspace.mel",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/textures",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/caches/"
        "arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/"
        "outputScenes/renderScenes",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke",
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
        "workspace",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/houdini/"
        "pipeline_test_sq001_sh0010_compositing_v001.hip",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nuke/scripts/"
        "pipeline_test_sq001_sh0010_compositing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/maya/scenes/"
        "pipeline_test_sq001_sh0010_compositing_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/sq001/sh0010/nukestudio/"
        "pipeline_test_sq001_sh0010_compositing_v001.hrox",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/BackdropNode1/BackdropNode1_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/set1_mayaAscii/set1_mayaAscii_v001.ma",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/sq001/"
        "sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/sq001/"
        "sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001/sh0010/"
        "compositing/write1/write1_v001.mov",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/sq001/sh0010/"
        "compositing/write1/write1_v001.R3D",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/sq001/sh0010/"
        "compositing/write1/write1_v001.psd",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/sq001/sh0010/"
        "compositing/writegeo1/writegeo1_v001.abc",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/sq001/sh0010/"
        "compositing/writegeo1/writegeo1_v001.fbx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/camera/sq001_sh0010/"
        "standard/0001/camera.abc",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/asset/writegeo1/"
        "model/sq001_sh0010/0001/model.abc",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.hdr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/sq001_sh0010/"
        "sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.hdr",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/_plates",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/_references",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/3dsmax",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/mari",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop/"
        "files",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/photoshop/"
        "rendered",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/_in",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/_out",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/geo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/"
        "render",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini/temp",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/caches",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "caches/arnold",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/cacheScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/dynamicScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "outputScenes/renderScenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/scenes",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/source",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "textures",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/renders",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renders/comp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renders/slapcomp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/"
        "renderScripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/scripts",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/scripts/"
        "workspace",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke/temp",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya/"
        "workspace.mel",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nukestudio"
        "/pipeline_test_sq001_sh0010_compositing_v001.hrox",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/nuke"
        "/scripts/pipeline_test_sq001_sh0010_compositing_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/maya"
        "/scenes/pipeline_test_sq001_sh0010_compositing_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/RND/sq001/sh0010/houdini"
        "/pipeline_test_sq001_sh0010_compositing_v001.hip",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/nuke_gizmo/RND/sq001"
        "/sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/lut/RND/sq001"
        "/sh0010/compositing/Group1/Group1_v001.gizmo",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/BackdropNode1/BackdropNode1_v001.nk",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/mov/RND/sq001"
        "/sh0010/compositing/write1/write1_v001.mov",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/write1/write1_v001.psd",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/RND/sq001"
        "/sh0010/compositing/writegeo1/writegeo1_v001.abc",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/cache/RND/sq001"
        "/sh0010/compositing/writegeo1/writegeo1_v001.fbx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/set1_mayaBinary/set1_mayaBinary_v001.mb",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/scene/RND/sq001"
        "/sh0010/compositing/set1_mayaAscii/set1_mayaAscii_v001.ma",

        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.exr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.dpx",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpeg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.jpg",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.%04d.hdr",
        "//10.11.0.184/171001_ftrack/tgbvfx/vfx/_publish/img/RND/sq001_sh0010"
        "/sq001_sh0010_Write1_v001/sq001_sh0010_Write1_v001.1001.hdr",
    ]


def assert_entity(entity):
    templates = lucidity.discover_templates()
    msg = (
        "No valid templates found for template name: \"{0}\", and entity: "
        "\"{1}\"".format(templates[0].get_template_name(entity), entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg

    get_resolved_paths(entity)


def get_resolved_paths(entity):
    templates = lucidity.discover_templates()
    valid_templates = templates[0].get_valid_templates(entity, templates)
    resolved_paths = []
    for template in valid_templates:
        try:
            resolved_paths.append(template.format(entity))
        except lucidity.error.FormatError as e:
            msg = e.message + "\nTemplate name: {0}".format(template.name)
            raise type(e)(msg)

    return resolved_paths


def get_workfile_extensions():
    return [".hrox", ".nk", ".mb", ".hip"]


def get_imagefile_extensions():
    return [".exr", ".dpx", ".jpeg", ".jpg", ".hdr"]


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def get_entities():
    entities = []

    entities.extend(tpt.get_entities())
    entities.extend(tpat.get_entities())
    entities.extend(tpfat.get_entities())
    entities.extend(tpst.get_entities())
    entities.extend(tpfst.get_entities())

    return entities


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

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


def test_unused_templates():
    templates = lucidity.discover_templates()

    used_templates = []
    for entity in get_entities():
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg


def test_excess_templates():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg
