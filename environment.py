import os

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-template"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-locations"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "pythonpath"
    ),
]

# PYBLISHPLUGINPATH
environment["PYBLISHPLUGINPATH"] = [
    os.path.join(root, "environment", "PYBLISHPLUGINPATH", "maya"),
    os.path.join(root, "environment", "PYBLISHPLUGINPATH", "ftrack"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-deadline",
        "pyblish_deadline",
        "plugins"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-ftrack",
        "pyblish_ftrack",
        "plugins"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins",
        "deadline"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins",
        "maya"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins",
        "houdini"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "plugins",
        "ftrack"
    ),
]

# FTRACK_TEMPLATES_PATH
environment["FTRACK_TEMPLATES_PATH"] = [
    os.path.join(root, "environment", "FTRACK_TEMPLATES_PATH")
]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
    os.path.join(root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
]

# FTRACK_LOCATION_PLUGIN_PATH
environment["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(root, "environment", "FTRACK_LOCATION_PLUGIN_PATH"),
]

# FTRACK_LOCATIONS_MODULE
environment["FTRACK_LOCATIONS_MODULE"] = [
    os.environ.get("FTRACK_LOCATIONS_MODULE", "ftrack_template_disk")
]

utils.write_environment(environment)
