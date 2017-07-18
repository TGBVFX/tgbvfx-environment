import os
import platform

from lucidity import Template


def register():
    '''Register templates.'''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    templates = []

    # Project level templates
    mount = "{entity.disk." + system_name + "}/{entity.root}/tgbvfx"
    templates.extend([
        Template("Project", mount),
        Template("Project", mount + "/editorial"),
        Template("Project", mount + "/editorial/audio"),
        Template("Project", mount + "/editorial/edl"),
        Template("Project", mount + "/editorial/nukestudio"),
        Template("Project", mount + "/editorial/omf"),
        Template("Project", mount + "/editorial/qt_offline"),
        Template("Project", mount + "/editorial/xml"),
        Template("Project", mount + "/editorial/aaf"),
        Template("Project", mount + "/io"),
        Template("Project", mount + "/io/client"),
        Template("Project", mount + "/io/client/from_client"),
        Template("Project", mount + "/io/client/to_client"),
        Template("Project", mount + "/io/graphics"),
        Template("Project", mount + "/io/outsource"),
        Template("Project", mount + "/io/outsource/company"),
        Template("Project", mount + "/io/outsource/company/from_broncos"),
        Template("Project", mount + "/io/outsource/company/to_broncos"),
        Template("Project", mount + "/io/references"),
        Template("Project", mount + "/io/setdata"),
        Template("Project", mount + "/io/setdata/grids"),
        Template("Project", mount + "/io/setdata/HDRs"),
        Template("Project", mount + "/io/setdata/measurements"),
        Template("Project", mount + "/io/setdata/references"),
        Template("Project", mount + "/io/sourcefootage"),
        Template("Project", mount + "/io/transcodedfootage"),
        Template("Project", mount + "/preproduction"),
        Template("Project", mount + "/preproduction/moodboards"),
        Template("Project", mount + "/preproduction/scripts"),
        Template("Project", mount + "/preproduction/storyboards"),
        Template("Project", mount + "/preproduction/treatments"),
        Template("Project", mount + "/vfx"),
        Template("Project", mount + "/vfx/_dev"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/_references"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/3dsmax"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/_in"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/_out"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/geo"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/render"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/houdini/temp"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/mari"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/caches"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/caches/arnold"
        ),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/cacheScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/dynamicScenes"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/outputScenes/renderScenes"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/renders"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/scenes"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/source"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/temp"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/textures"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders"),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders/comp"
        ),
        Template(
            "Project",
            mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renders/slapcomp"
        ),
        Template(
            "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/renderScripts"
        ),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/scripts"),
        Template("Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/nuke/temp"),
        Template("Project", mount + "/vfx/_publish"),
    ])

    # Projet level auxiliary files
    template = Template(
        "Project", mount + "/vfx/_dev/_ASSET_TEMPLATE/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # Shot level templates
    mount = (
        "{entity.project.disk." + system_name + "}/{entity.project.root}/"
        "tgbvfx/vfx/{entity.parent.name}/{entity.name}"
    )
    templates.extend([
        Template("Shot", mount + "/_plates"),
        Template("Shot", mount + "/_references"),
        Template("Shot", mount + "/houdini"),
        Template("Shot", mount + "/houdini/_in"),
        Template("Shot", mount + "/houdini/_out"),
        Template("Shot", mount + "/houdini/geo"),
        Template("Shot", mount + "/houdini/render"),
        Template("Shot", mount + "/houdini/temp"),
        Template("Shot", mount + "/maya"),
        Template("Shot", mount + "/maya/caches"),
        Template("Shot", mount + "/maya/caches/arnold"),
        Template("Shot", mount + "/maya/outputScenes"),
        Template("Shot", mount + "/maya/outputScenes/cacheScenes"),
        Template("Shot", mount + "/maya/outputScenes/dynamicScenes"),
        Template("Shot", mount + "/maya/outputScenes/renderScenes"),
        Template("Shot", mount + "/maya/renders"),
        Template("Shot", mount + "/maya/scenes"),
        Template("Shot", mount + "/maya/source"),
        Template("Shot", mount + "/maya/temp"),
        Template("Shot", mount + "/maya/texures"),
        Template("Shot", mount + "/nuke"),
        Template("Shot", mount + "/nuke/renders"),
        Template("Shot", mount + "/nuke/renders/comp"),
        Template("Shot", mount + "/nuke/renders/slapcomp"),
        Template("Shot", mount + "/nuke/renderScripts"),
        Template("Shot", mount + "/nuke/scripts"),
        Template("Shot", mount + "/nuke/temp"),
    ])

    # Shot level auxiliary files
    template = Template(
        "Shot", mount + "/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # FileComponent templates
    mount = (
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx"
    )

    # NukeStudio scene
    templates.append(
        Template(
            ".hrox",
            mount + "/editorial/nukestudio/"
            "{entity.version.task.project.name}_v{entity.version.version}"
            "{entity.file_type}"
        )
    )

    # Nuke scene
    templates.append(
        Template(
            ".nk",
            mount + "/vfx/{entity.version.asset.parent.parent.name}/"
            "{entity.version.asset.parent.name}/nuke/scripts/"
            "{entity.version.asset.parent.parent.name}_"
            "{entity.version.asset.parent.name}_{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )

    # Maya scene
    templates.append(
        Template(
            ".mb",
            mount + "/vfx/{entity.version.asset.parent.parent.name}/"
            "{entity.version.asset.parent.name}/maya/scenes/"
            "{entity.version.asset.parent.parent.name}_"
            "{entity.version.asset.parent.name}_{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )

    # Houdini scene
    templates.append(
        Template(
            ".hip",
            mount + "/vfx/{entity.version.asset.parent.parent.name}/"
            "{entity.version.asset.parent.name}/houdini/"
            "{entity.version.asset.parent.parent.name}_"
            "{entity.version.asset.parent.name}_{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )

    return templates
