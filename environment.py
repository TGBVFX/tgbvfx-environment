import os

from conda_git_deployment import utils


environment = {}

# PYBLISHPLUGINPATH
path = os.path.join(
    os.environ["CONDA_GIT_REPOSITORY"], "pyblish-tgbvfx", "plugins", "maya"
)

environment["PYBLISHPLUGINPATH"] = path

utils.write_environment(environment)
