import os

import psutil

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}

# PATH
environment["PATH"] = [
    "//10.11.0.184/_tgbvfx/_bin/ffmpeg/v2.7",
    "C:/Program Files (x86)/QuickTime/QTSystem/",
]

# LIBRARY_PATH
environment["LIBRARY_PATH"] = [
    "//10.11.0.184/_tgbvfx/library"
]

# STUDIO_TMP
environment["STUDIO_TMP"] = [
    "//10.11.0.184/_tgbvfx/temp"
]

# solidangle_LICENSE
environment["solidangle_LICENSE"] = [
    "5053@10.11.0.110"
]

# peregrinel_LICENSE
environment["peregrinel_LICENSE"] = [
    "5053@10.11.0.110"
]

# MAYA_VP2_DEVICE_OVERRIDE
environment["MAYA_VP2_DEVICE_OVERRIDE"] = [
    "VirtualDeviceDx11"
]

# MAYA_FORCE_DX_WARP
environment["MAYA_FORCE_DX_WARP"] = [
    "1"
]

# YETI_TMP
environment["YETI_TMP"] = [
    "//10.11.0.184/_tgbvfx/temp"
]

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(root, "environment", "PYTHONPATH"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-nukestudio"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "tgbvfx-pipeline"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "tgbvfx-pipeline",
        "pipeline",
        "maya"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-royalrender"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "filelink"),
]

# LUCIDITY_TEMPLATE_PATH
environment["LUCIDITY_TEMPLATE_PATH"] = [
    os.path.join(root, "environment", "LUCIDITY_TEMPLATE_PATH"),
]

# MAYA_MODULE_PATH
environment["MAYA_MODULE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "tgbvfx-pipeline",
        "pipeline",
        "maya",
        "modules",
        "assetSystem"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "tgbvfx-pipeline",
        "pipeline",
        "maya",
        "modules",
        "sceneGraph"
    ),
]

# XBMLANGPATH
environment["XBMLANGPATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "tgbvfx-pipeline",
        "pipeline",
        "maya",
        "icons"
    )
]

# HIERO_PLUGIN_PATH
environment["HIERO_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nukestudio",
        "pyblish_nukestudio",
        "hiero_plugin_path"
    )
]

# NUKE_PATH
environment["NUKE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(root, "environment", "NUKE_PATH"),
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
