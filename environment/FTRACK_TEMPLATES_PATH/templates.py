import os
import platform

import ftrack_template


def dictionary_to_paths(dictionary, path="", results=[]):

    for key, value in dictionary.iteritems():

        parent_path = (path + os.sep + key)
        if not path:
            parent_path = key

        if value:
            results.append(parent_path)
            dictionary_to_paths(value, path=parent_path, results=results)
        else:
            results.append(parent_path)

    return results


def register():
    '''Register templates.'''

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    mount = (
        "{#project.disk." + system_name + "}/{#project.root}/{#project.name}"
    )
    task = "{#task.name}"
    tasks = "Tasks/" + task
    assetversion = "{#assetversion.asset.type.short}/v{#assetversion.version}"
    file_component = "{#component.name}{#component.file_type}"
    sequence_component = (
        "{#container.name}/{#container.name}.{#component.name}" +
        "{#component.file_type}"
    )
    assets = "Assets/{#assetbuild.type.name}/{#assetbuild.name}"
    shot = "{#shot.name}"
    shots = "Shots/" + shot
    sequence = "{#sequence.name}"
    sequences = "Sequences/" + sequence
    episode = "{#episode.name}"
    episodes = "Episodes/" + episode

    structure = {
        mount: {
            "work": {
                tasks: {
                    assetversion: {
                        file_component: {},
                        sequence_component: {}
                    }
                },
                assets: {
                    task: {
                        assetversion: {
                            file_component: {},
                            sequence_component: {}
                        }
                    }
                },
                shots: {
                    task: {
                        assetversion: {
                            file_component: {},
                            sequence_component: {}
                        }
                    },
                    assets: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        }
                    },
                },
                sequences: {
                    task: {
                        assetversion: {
                            file_component: {},
                            sequence_component: {}
                        }
                    },
                    assets: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        }
                    },
                    shot: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        },
                        assets: {
                            task: {
                                assetversion: {
                                    file_component: {},
                                    sequence_component: {}
                                }
                            }
                        }
                    }
                },
                episodes: {
                    task: {
                        assetversion: {
                            file_component: {},
                            sequence_component: {}
                        }
                    },
                    assets: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        }
                    },
                    shot: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        },
                        assets: {
                            task: {
                                assetversion: {
                                    file_component: {},
                                    sequence_component: {}
                                }
                            }
                        }
                    },
                    sequence: {
                        task: {
                            assetversion: {
                                file_component: {},
                                sequence_component: {}
                            }
                        },
                        assets: {
                            task: {
                                assetversion: {
                                    file_component: {},
                                    sequence_component: {}
                                }
                            }
                        },
                        shot: {
                            task: {
                                assetversion: {
                                    file_component: {},
                                    sequence_component: {}
                                }
                            },
                            assets: {
                                task: {
                                    assetversion: {
                                        file_component: {},
                                        sequence_component: {}
                                    }
                                }
                            }
                        }
                    },
                }
            }
        }
    }

    templates = []
    for path in dictionary_to_paths(structure):
        templates.append(ftrack_template.Template("template", path))

    return templates
