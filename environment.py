import os

import psutil

from conda_git_deployment import utils
import environment_setup


root = os.path.dirname(__file__)
environment = {}


def main():

    # PATH
    environment["PATH"] = [
        os.path.join(root, "zips", "djv-1.1.0-Windows-64", "bin"),
    ]

    # PYTHONPATH
    environment["PYTHONPATH"] = [
        os.path.join(root, "environment", "PYTHONPATH"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"]),  # studiolibrary
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-maya"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-maya",
            "pyblish_maya",
            "pythonpath"
        ),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-nukestudio"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-nukeassist"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "pyblish-royalrender"
        ),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "filelink"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "maya-capture"),
    ]

    # LUCIDITY_TEMPLATE_PATH
    environment["LUCIDITY_TEMPLATE_PATH"] = [
        os.path.join(root, "environment", "LUCIDITY_TEMPLATE_PATH"),
    ]

    # MAYA_SCRIPT_PATH
    environment["MAYA_SCRIPT_PATH"] = [
        os.path.join(root, "environment", "MAYA_SCRIPT_PATH")
    ]

    # XBMLANGPATH
    environment["XBMLANGPATH"] = [
        os.path.join(root, "environment", "XBMLANGPATH")
    ]

    # HIERO_PLUGIN_PATH
    environment["HIERO_PLUGIN_PATH"] = [
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-nukestudio",
            "pyblish_nukestudio",
            "hiero_plugin_path"
        ),
        os.path.join(root, "environment", "HIERO_PLUGIN_PATH")
    ]

    # NUKE_PATH
    environment["NUKE_PATH"] = [
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-nuke",
            "pyblish_nuke",
            "nuke_path"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-nukeassist",
            "pyblish_nukeassist",
            "nuke_path"
        ),
        os.path.join(root, "environment", "NUKE_PATH"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "Cryptomatte",
            "nuke"
        ),
    ]

    # PYBLISH_HOTKEY
    environment["PYBLISH_HOTKEY"] = ["Ctrl+Alt+P"]

    # PYBLISH_QML_MODAL
    environment["PYBLISH_QML_MODAL"] = ["True"]

    # PYBLISH_QML_MODAL
    environment["PYBLISH_ALLOW_DUPLICATE_PLUGIN_NAMES"] = ["True"]

    # REVIEW_PRESETS
    environment["REVIEW_PRESETS"] = [
        os.path.join(root, "environment", "REVIEW_PRESETS"),
    ]

    # FTRACK_CONNECT_PLUGIN_PATH
    environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "houdini"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "create_structure"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "batch_tasks"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "batch_create"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "dynamic_environment"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "process_review"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "running_jobs"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "status_assign"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "pending_changes"
        ),
        os.path.join(root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "pyblish-ftrack",
            "pyblish_ftrack"
        ),
    ]

    # FTRACK_EVENT_PLUGIN_PATH
    environment["FTRACK_EVENT_PLUGIN_PATH"] = [
        os.path.join(root, "environment", "FTRACK_EVENT_PLUGIN_PATH"),
    ]

    # FTRACK_ENVIRONMENTS
    environment["FTRACK_APP_ENVIRONMENTS"] = [
        os.path.join(root, "environment", "FTRACK_APP_ENVIRONMENTS"),
    ]

    # Kill existing ftrack_connects
    for proc in psutil.process_iter():
        try:
            if "ftrack_connect" in proc.cmdline():
                proc.kill()
        except psutil.AccessDenied:
            # Some process does not allow you to get "cmdline()"
            pass

    utils.write_environment(environment)


if __name__ == "__main__":
    environment_setup.install_djv()
    main()
