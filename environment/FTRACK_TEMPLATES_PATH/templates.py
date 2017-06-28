import os
import platform

import ftrack_template


def dictionary_to_paths(data, path="", results=[]):

    for key, value in data.iteritems():

        parent_path = (path + os.sep + key)
        if not path:
            parent_path = key

        if isinstance(value, dict):
            if "isfile" in value:
                temp = ftrack_template.Template("template", parent_path)
                temp.isfile = value["isfile"]
                temp.source = value["source"]
                results.append(temp)
            else:
                temp = ftrack_template.Template("template", parent_path)
                temp.isfile = False
                results.append(temp)
                if value:
                    dictionary_to_paths(
                        value, path=parent_path, results=results
                    )

    return results


def register():
    '''Register templates.'''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    project_structure = {
        "{#project.disk." + system_name + "}/{#project.root}/tgbvfx": {
            "editorial": {
                "audio": {},
                "edl": {},
                "nukestudio": {},
                "omf": {},
                "qt_offline": {},
                "xml": {},
                "aaf": {}
            },
            "io": {
                "client": {
                    "from_client": {},
                    "to_client": {}
                },
                "graphics": {},
                "outsource": {
                    "company": {
                        "from_broncos": {},
                        "to_broncos": {}
                    }
                },
                "references": {},
                "setdata": {
                    "grids": {},
                    "HDRs": {},
                    "measurements": {},
                    "references": {}
                },
                "sourcefootage": {},
                "transcodedfootage": {}
            },
            "preproduction": {
                "moodboards": {},
                "scripts": {},
                "storyboards": {},
                "treatments": {}
            },
            "vfx": {
                "_dev": {
                    "_ASSET_TEMPLATE": {
                        "_references": {},
                        "3dsmax": {},
                        "houdini": {
                            "_in": {},
                            "_out": {},
                            "geo": {},
                            "render": {},
                            "temp": {}
                        },
                        "mari": {},
                        "maya": {
                            "caches": {
                                "arnold": {},
                            },
                            "outputScenes": {
                                "cacheScenes": {},
                                "dynamicScenes": {},
                                "renderScenes": {}
                            },
                            "renders": {},
                            "scenes": {},
                            "source": {},
                            "temp": {},
                            "textures": {},
                            "workspace.mel": {
                                "isfile": True,
                                "source": os.path.join(
                                    os.path.dirname(__file__), "workspace.mel"
                                )
                            },
                        },
                        "nuke": {
                            "renders": {
                                "comp": {},
                                "slapcomp": {}
                            },
                            "renderScripts": {},
                            "scripts": {},
                            "temp": {}
                        }
                    }
                },
                "_publish": {},
                "{#sequence.name}": {
                    "{#shot.name}": {
                        "_references": {},
                        "houdini": {
                            "_in": {},
                            "_out": {},
                            "geo": {},
                            "render": {},
                            "temp": {}
                        },
                        "maya": {
                            "caches": {
                                "arnold": {}
                            },
                            "outputScenes": {
                                "cacheScenes": {},
                                "dynamicScenes": {},
                                "renderScenes": {}
                            },
                            "renders": {},
                            "scenes": {},
                            "source": {},
                            "temp": {},
                            "textures": {},
                            "workspace.mel": {
                                "isfile": True,
                                "source": os.path.join(
                                    os.path.dirname(__file__), "workspace.mel"
                                )
                            }
                        },
                        "nuke": {
                            "renders": {
                                "comp": {},
                                "slapcomp": {}
                            },
                            "renderScripts": {},
                            "scripts": {},
                            "temp": {}
                        }
                    }
                }
            }
        }
    }

    return dictionary_to_paths(project_structure)
