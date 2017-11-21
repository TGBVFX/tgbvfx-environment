import os
import requests
import subprocess

import psutil

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}


def download_file(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    if os.path.exists(path):
        return True
    else:
        return False


def install_from_url(url, name):

    zip_path = os.path.join(root, "zips")

    if not os.path.exists(zip_path):
        os.makedirs(zip_path)

    path = os.path.join(root, "zips", name + ".zip")

    if not os.path.exists(path):
        download_file(url, path)

    subprocess.call(["pip", "install", path])


# Install python-qt5
try:
    __import__("PyQt5")
except ImportError:
    install_from_url(
        "https://github.com/pyqt/python-qt5/archive/0.3.0.zip", "python-qt5"
    )

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
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-royalrender"),
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
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "create_structure"
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
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "process_review"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "running_jobs"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "status_assign"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "pending_changes"
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
