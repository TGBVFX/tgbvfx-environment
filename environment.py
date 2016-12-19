import os

from conda_git_deployment import utils


environment = {}

# FTRACK_TEMPLATES_PATH
path = os.path.join(
    os.path.join(
        os.path.join(os.path.dirname(__file__)), "environment",
        "FTRACK_TEMPLATES_PATH"
    ),
)

environment["FTRACK_TEMPLATES_PATH"] = path

utils.write_environment(environment)
