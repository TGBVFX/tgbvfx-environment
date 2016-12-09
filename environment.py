import os

from conda_git_deployment import utils


path = os.path.join(
    os.environ["CONDA_GIT_REPOSITORY"], "pyblish-tgbvfx", "plugins", "maya"
)
utils.write_environment({"PYBLISHPLUGINPATH": path})
