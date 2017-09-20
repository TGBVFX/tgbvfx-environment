import os
import platform

import lucidity


class Template(lucidity.Template):

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

    def get_valid_templates(self, entity, templates):

        results = []
        template_name = self.get_template_name(entity)
        try:
            template_name = entity["metadata"]["lucidity_template_name"]
        except KeyError:
            pass

        for template in templates:
            if template.name == template_name:
                results.append(template)

        return results

    def format(self, data):

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "AssetVersion":
            version_string = str(data["version"]).zfill(3)
            data["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "FileComponent":
            if data["version"]:
                version_string = str(data["version"]["version"]).zfill(3)
                data["version"]["version"] = version_string
            else:
                version_string = str(
                    data["container"]["version"]["version"]
                ).zfill(3)
                data["container"]["version"]["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "SequenceComponent":
            version_string = str(data["version"]["version"]).zfill(3)
            data["version"]["version"] = version_string

            # "padding" data member needs to be convert from integer to string.
            padding_string = str(data["padding"]).zfill(2)
            data["padding"] = padding_string

        return os.path.abspath(
            super(Template, self).format(data)
        ).replace("\\", "/")


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
    mount = "{disk." + system_name + "}/{root}/tgbvfx"
    templates.extend([
        Template("Project", mount),
        Template("Project", mount + "/editorial"),
        Template("Project", mount + "/editorial/audio"),
        Template("Project", mount + "/editorial/edl"),
        Template("Project", mount + "/editorial/footage"),
        Template("Project", mount + "/editorial/nukestudio"),
        Template("Project", mount + "/editorial/nukestudio/workspace"),
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

    # Project/Task level templates
    templates.extend([
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}"
        ),
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}/nuke"
        ),
        Template(
            "Project/Task",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}/nuke/scripts"
        ),
    ])

    # Project/Sequence level templates
    templates.extend([
        Template(
            "Project/Sequence",
            "{project.disk." + system_name + "}/{project.root}/tgbvfx/vfx/"
            "{name}"
        ),
    ])

    # Project/Sequence/Shot level templates
    mount = (
        "{project.disk." + system_name + "}/{project.root}/"
        "tgbvfx/vfx/{parent.name}/{name}"
    )
    templates.extend([
        Template("Project/Sequence/Shot", mount),
        Template("Project/Sequence/Shot", mount + "/_plates"),
        Template("Project/Sequence/Shot", mount + "/_references"),
        Template("Project/Sequence/Shot", mount + "/houdini"),
        Template("Project/Sequence/Shot", mount + "/houdini/_in"),
        Template("Project/Sequence/Shot", mount + "/houdini/_out"),
        Template("Project/Sequence/Shot", mount + "/houdini/geo"),
        Template("Project/Sequence/Shot", mount + "/houdini/render"),
        Template("Project/Sequence/Shot", mount + "/houdini/temp"),
        Template("Project/Sequence/Shot", mount + "/maya"),
        Template("Project/Sequence/Shot", mount + "/maya/caches"),
        Template("Project/Sequence/Shot", mount + "/maya/caches/arnold"),
        Template("Project/Sequence/Shot", mount + "/maya/outputScenes"),
        Template(
            "Project/Sequence/Shot", mount + "/maya/outputScenes/cacheScenes"
        ),
        Template(
            "Project/Sequence/Shot", mount + "/maya/outputScenes/dynamicScenes"
        ),
        Template(
            "Project/Sequence/Shot", mount + "/maya/outputScenes/renderScenes"
        ),
        Template("Project/Sequence/Shot", mount + "/maya/renders"),
        Template("Project/Sequence/Shot", mount + "/maya/scenes"),
        Template("Project/Sequence/Shot", mount + "/maya/source"),
        Template("Project/Sequence/Shot", mount + "/maya/temp"),
        Template("Project/Sequence/Shot", mount + "/maya/texures"),
        Template("Project/Sequence/Shot", mount + "/nuke"),
        Template("Project/Sequence/Shot", mount + "/nuke/renders"),
        Template("Project/Sequence/Shot", mount + "/nuke/renders/comp"),
        Template("Project/Sequence/Shot", mount + "/nuke/renders/slapcomp"),
        Template("Project/Sequence/Shot", mount + "/nuke/renderScripts"),
        Template("Project/Sequence/Shot", mount + "/nuke/scripts"),
        Template("Project/Sequence/Shot", mount + "/nuke/scripts/workspace"),
        Template("Project/Sequence/Shot", mount + "/nuke/temp"),
    ])

    # Project/Sequence/Shot level auxiliary files
    template = Template(
        "Project/Sequence/Shot", mount + "/maya/workspace.mel"
    )
    template.source = os.path.join(
        os.path.dirname(__file__), "workspace.mel"
    )
    templates.append(template)

    # Project/Sequence/Shot/Asset level templates
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset",
            "{parent.project.disk." + system_name + "}/{parent.project.root}/"
            "tgbvfx/vfx/_publish/{type.short}"
        ),
        Template(
            "Project/Sequence/Shot/Asset",
            "{parent.project.disk." + system_name + "}/{parent.project.root}/"
            "tgbvfx/vfx/_publish/{type.short}/{parent.parent.name}_"
            "{parent.name}"
        ),
    ])

    # Project/Sequence/Shot/Asset/AssetVersion level templates
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion",
            "{asset.parent.project.disk." + system_name + "}/"
            "{asset.parent.project.root}/tgbvfx/vfx/_publish/"
            "{asset.type.short}/{asset.parent.parent.name}_{asset.parent.name}"
            "/{task.name}"
        ),
    ])

    # .exr
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.metadata.instance_name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.exr"
            "/FileComponent/.exr",
            "{container.version.task.project.disk." + system_name + "}/"
            "{container.version.task.project.root}/tgbvfx/vfx/_publish/"
            "{container.version.asset.type.short}/"
            "{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}/"
            "{container.version.metadata.instance_name}/"
            "{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/SequenceComponent/.exr",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}_v{version.version}/"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/SequenceComponent/"
            ".exr",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}_v{version.version}/"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
    ])

    # .dpx
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.dpx",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.metadata.instance_name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/SequenceComponent/.dpx",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}_v{version.version}/"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/SequenceComponent/"
            ".dpx",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}_v{version.version}/"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
    ])

    # .jpg
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpg",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.metadata.instance_name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.metadata.instance_name}_v{version.version}.%{padding}d"
            "{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/SequenceComponent/.jpg"
            "/FileComponent/.jpg",
            "{container.version.task.project.disk." + system_name + "}/"
            "{container.version.task.project.root}/tgbvfx/vfx/_publish/"
            "{container.version.asset.type.short}/"
            "{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}/"
            "{container.version.metadata.instance_name}/"
            "{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        )
    ])

    # .abc
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.metadata.instance_name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}/{version.metadata.instance_name}"
            "_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.abc",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}/{version.metadata.instance_name}"
            "_v{version.version}{file_type}"
        ),
    ])

    # .mov
    templates.append(
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mov",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.metadata.instance_name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.metadata.instance_name}_v{version.version}{file_type}"
        )
    )

    # .gizmo
    templates.extend([
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.task.name}_{name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}/{version.metadata.instance_name}"
            "_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.gizmo",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.type.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.metadata.instance_name}/{version.metadata.instance_name}"
            "_v{version.version}{file_type}"
        ),
    ])

    # .hrox
    templates.append(
        Template(
            "Project/Asset/AssetVersion/FileComponent/.hrox",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/editorial/nukestudio/"
            "{version.task.project.name}_v{version.version}{file_type}"
        )
    )

    # .nk
    templates.extend([
        Template(
            "Project/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/{version.task.name}/nuke/"
            "scripts/{version.task.project.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.parent.name}/{version.asset.parent.name}/"
            "nuke/scripts/{version.task.project.name}_"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "nuke_backdrop",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/_publish/"
            "{version.asset.type.short}/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}/{version.task.name}/"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.task.name}_{version.metadata.instance_name}_{name}_v"
            "{version.version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/nuke"
            "/scripts/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.nk",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/nuke"
            "/scripts/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
    ])

    # .mb
    templates.extend([
        Template(
            "Project/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/{version.task.name}/maya/"
            "scenes/{version.task.project.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/{version.task.name}/maya/"
            "scenes/{version.task.project.name}_"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/maya"
            "/scenes/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.mb",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/maya"
            "/scenes/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
    ])

    # .hip
    templates.extend([
        Template(
            "Project/Asset/AssetVersion/FileComponent/.hip",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/{version.task.name}/"
            "houdini/{version.task.project.name}_{version.task.name}_v"
            "{version.version}{file_type}"
        ),
        Template(
            "Project/Sequence/Shot/Asset/AssetVersion/FileComponent/.hip",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.parent.name}/{version.asset.parent.name}/"
            "houdini/{version.task.project.name}_"
            "{version.asset.parent.parent.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/AssetBuild/Asset/AssetVersion/FileComponent/.hip",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/"
            "houdini/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
        Template(
            "Project/Folder/AssetBuild/Asset/AssetVersion/FileComponent/.hip",
            "{version.task.project.disk." + system_name + "}/"
            "{version.task.project.root}/tgbvfx/vfx/"
            "{version.asset.parent.type.name}/{version.asset.parent.name}/"
            "houdini/{version.task.project.name}_"
            "{version.asset.parent.type.name}_{version.asset.parent.name}_"
            "{version.task.name}_v{version.version}{file_type}"
        ),
    ])

    return templates
