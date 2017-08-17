import os
import platform

import lucidity

from tgbvfx_environment import utils


class Template(lucidity.Template):

    hosts = ["*"]

    def get_parents(self, entity, parents):
        """Recursive iterate to find all parents.

        For AssetVersion where no parent is present, the asset is assumed as
        parent.
        For SequenceComponent and FileComponent where no parent is present, the
        asset version is assumed as parent.
        """

        try:
            parent = entity["parent"]
            if parent:
                parents.append(parent)
                return self.get_parents(parent, parents)
        except KeyError:
            # Assuming its either an AssetVersion or Component.
            valid_types = [
                "SequenceComponent", "FileComponent", "AssetVersion"
            ]
            if entity.entity_type not in valid_types:
                raise ValueError(
                    "Unrecognized entity type: {0}".format(entity.entity_type)
                )

            if entity.entity_type == "AssetVersion":
                parents.append(entity["asset"])
                return self.get_parents(entity["asset"], parents)

            if entity.entity_type == "FileComponent":

                parent = entity["version"]
                # Assuming its in a container, if there are no version.
                if parent:
                    parents.append(entity["version"])
                else:
                    parent = entity["container"]
                    parents.append(entity["container"])
                return self.get_parents(parent, parents)

            if entity.entity_type == "SequenceComponent":
                parents.append(entity["version"])
                return self.get_parents(entity["version"], parents)

        return parents

    def get_entity_type_path(self, entities):
        """Get the entity type path from a list of entities

        The returned path is a list of entity types separated by a path
        separator:
            "[entity_type]/[entity_type]/[entity_type]"
            "Project/Asset/AssetVersion"

        For further uniqueness the file_type data member (extension) is used
        for components. This results in paths like this:
            "Project/Asset/AssetVersion/FileComponent/[file_type]"
            "Project/Asset/AssetVersion/FileComponent/.txt"
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr
            /FileComponent/.exr"
        """

        entity_types = []
        for entity in entities:
            entity_types.append(entity.entity_type)

            try:
                entity_types.append(entity["file_type"])
            except KeyError:
                pass

        return "/".join(entity_types)

    def get_template_name(self, entity):
        """Convenience method for getting the template name

        The template name is generated from the entity's parents, and their
        entity type.
        """

        entities = list(reversed(self.get_parents(entity, [])))
        entities.append(entity)
        return self.get_entity_type_path(entities)

    def ftrack_format(self, entity, host="*"):
        """Formats the template with the supplied entity's data.

        The templates access the entity's data through "entity":
           Template("Project", "{entity.name}")

        The optional "host" is to specify a specific DCCs template.
        """
        if host not in self.hosts:
            raise utils.HostError(
                'Host "{0}" does not match template hosts "{1}"'.format(
                    host, self.hosts
                )
            )

        # Inject the entity into the format data.
        data = {"entity": entity}

        # Format data can only be strings/unicode, so some data members needs
        # to be converted.
        try:
            if data["entity"]["version"]:
                data["entity"]["version"]["version"] = str(
                    entity["version"]["version"]
                ).zfill(3)
        except KeyError:
            pass

        try:
            if data["entity"]["container"]:
                data["entity"]["container"]["version"]["version"] = str(
                    entity["container"]["version"]["version"]
                ).zfill(3)
        except KeyError:
            pass

        try:
            data["entity"]["padding"] = str(entity["padding"])
        except KeyError:
            pass

        return self.format(data)


def register():
    '''Register templates.

    Templates are named according to the entity in the hierarchy,
    they aim to solve paths for.
    For example a template named "Project" is only for paths for the project.
    Nested entity types are specified with a path separator, for example
    "Project/Shot" deals with paths for shots under the project.
    To specify dealing with certain file types, the file types extension is
    added. For example a template named "Project/.nk" deals with Nuke script
    paths under the project.
    It is assumed that asset versions are children of the asset, resulting in a
    path "Project/Asset/AssetVersion".
    '''

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
    shot_templates = []
    mount = (
        "{entity.project.disk." + system_name + "}/{entity.project.root}/"
        "tgbvfx/vfx/{entity.parent.name}/{entity.name}"
    )
    shot_templates.extend([
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
    shot_templates.append(template)

    # Shot level template assignment
    varients = ["Project/Task", "Project/Sequence/Shot"]
    for varient in varients:
        for template in shot_templates:
            temp = Template(varient, template.pattern)
            if hasattr(template, "source"):
                temp.source = template.source
            templates.append(temp)

    # SequenceComponent templates.
    # EXR
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/image/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}/"
        "{entity.version.metadata.instance_name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_"
        "{entity.version.metadata.instance_name}_"
        "v{entity.version.version}.%0{entity.padding}d{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # JPG
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpg",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/image/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}/"
        "{entity.version.metadata.instance_name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_"
        "{entity.version.metadata.instance_name}_"
        "v{entity.version.version}.%0{entity.padding}d{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # JPEG
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpeg",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/image/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}/"
        "{entity.version.metadata.instance_name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_"
        "{entity.version.metadata.instance_name}_"
        "v{entity.version.version}.%0{entity.padding}d{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # FileComponent templates
    # EXR
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr"
        "/FileComponent/.exr",
        "{entity.container.version.task.project.disk." + system_name + "}/"
        "{entity.container.version.task.project.root}/tgbvfx/vfx/_publish/"
        "image/{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}/"
        "{entity.container.version.metadata.instance_name}/"
        "{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}_"
        "{entity.container.version.metadata.instance_name}_"
        "v{entity.container.version.version}.{entity.name}"
        "{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # JPG
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpg"
        "/FileComponent/.jpg",
        "{entity.container.version.task.project.disk." + system_name + "}/"
        "{entity.container.version.task.project.root}/tgbvfx/vfx/_publish/"
        "image/{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}/"
        "{entity.container.version.metadata.instance_name}/"
        "{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}_"
        "{entity.container.version.metadata.instance_name}_"
        "v{entity.container.version.version}.{entity.name}"
        "{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # JPEG
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpeg"
        "/FileComponent/.jpeg",
        "{entity.container.version.task.project.disk." + system_name + "}/"
        "{entity.container.version.task.project.root}/tgbvfx/vfx/_publish/"
        "image/{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}/"
        "{entity.container.version.metadata.instance_name}/"
        "{entity.container.version.asset.parent.parent.name}_"
        "{entity.container.version.asset.parent.name}_"
        "{entity.container.version.metadata.instance_name}_"
        "v{entity.container.version.version}.{entity.name}"
        "{entity.file_type}"
    )
    template.hosts = ["nukestudio", "nuke"]
    templates.append(template)

    # MOV
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mov",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/"
        "movies/{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}/"
        "{entity.version.metadata.instance_name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_"
        "{entity.version.metadata.instance_name}_"
        "v{entity.version.version}"
        "{entity.file_type}"
    )
    template.hosts = ["nukestudio"]
    templates.append(template)

    # GIZMO
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.gizmo",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/"
        "{entity.version.asset.type.short}/"
        "{entity.version.asset.parent.parent.name}/"
        "{entity.version.asset.parent.name}/"
        "{entity.version.task.name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_{entity.version.task.name}_"
        "{entity.name}_v{entity.version.version}{entity.file_type}"
    )
    template.hosts = ["nuke"]
    templates.append(template)

    # NukeStudio scene
    template = Template(
        "Project/Asset/AssetVersion/FileComponent/.hrox",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/editorial/nukestudio/"
        "{entity.version.task.project.name}_v{entity.version.version}"
        "{entity.file_type}"
    )
    template.hosts = ["*", "nukestudio"]
    templates.append(template)

    # Nuke scene
    templates.append(
        Template(
            "Project/Asset/AssetVersion/FileComponent/.nk",
            "{entity.version.task.project.disk." + system_name + "}/"
            "{entity.version.task.project.root}/tgbvfx/vfx/"
            "{entity.version.task.name}/nuke/scripts/"
            "{entity.version.task.name}_v{entity.version.version}"
            "{entity.file_type}"
        )
    )
    template = Template(
        "Backdrop",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/_publish/"
        "{entity.version.asset.type.short}/"
        "{entity.version.asset.parent.parent.name}/"
        "{entity.version.asset.parent.name}/"
        "{entity.version.task.name}/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_{entity.version.task.name}_"
        "{entity.version.metadata.instance_name}_"
        "{entity.name}_v{entity.version.version}{entity.file_type}"
    )
    templates.append(template)
    template = Template(
        "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.nk",
        "{entity.version.task.project.disk." + system_name + "}/"
        "{entity.version.task.project.root}/tgbvfx/vfx/"
        "{entity.version.asset.parent.parent.name}/"
        "{entity.version.asset.parent.name}/nuke/scripts/"
        "{entity.version.asset.parent.parent.name}_"
        "{entity.version.asset.parent.name}_{entity.version.task.name}_"
        "v{entity.version.version}{entity.file_type}"
    )
    template.hosts = ["*", "nukestudio", "nuke"]
    templates.append(template)

    # Maya scene
    templates.append(
        Template(
            "Project/Asset/AssetVersion/FileComponent/.mb",
            "{entity.version.task.project.disk." + system_name + "}/"
            "{entity.version.task.project.root}/tgbvfx/vfx/"
            "{entity.version.task.name}/maya/scenes/"
            "{entity.version.task.name}_v{entity.version.version}"
            "{entity.file_type}"
        )
    )
    templates.append(
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mb",
            "{entity.version.task.project.disk." + system_name + "}/"
            "{entity.version.task.project.root}/tgbvfx/vfx/"
            "{entity.version.task.name}/maya/scenes/"
            "{entity.version.asset.parent.parent.name}_"
            "{entity.version.asset.parent.name}_{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )

    # Houdini scene
    templates.append(
        Template(
            "Project/Asset/AssetVersion/FileComponent/.hip",
            "{entity.version.task.project.disk." + system_name + "}/"
            "{entity.version.task.project.root}/tgbvfx/vfx/"
            "{entity.version.task.name}/houdini/{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )
    templates.append(
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.hip",
            "{entity.version.task.project.disk." + system_name + "}/"
            "{entity.version.task.project.root}/tgbvfx/vfx/"
            "{entity.version.asset.parent.parent.name}/"
            "{entity.version.asset.parent.name}/houdini/"
            "{entity.version.asset.parent.parent.name}_"
            "{entity.version.asset.parent.name}_{entity.version.task.name}_"
            "v{entity.version.version}{entity.file_type}"
        )
    )

    return templates
