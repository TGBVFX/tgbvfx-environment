import os
import psutil

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}

# PATH
# Need to manually add Quicktime for Nuke, cause conda-git-deployment removes
# it from the environment.
environment["PATH"] = ["C:/Program Files (x86)/QuickTime/QTSystem/"]

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
]

# LUCIDITY_TEMPLATE_PATH
environment["LUCIDITY_TEMPLATE_PATH"] = [
    os.path.join(root, "environment", "LUCIDITY_TEMPLATE_PATH"),
]

# solidangle_LICENSE
environment["solidangle_LICENSE"] = ["5053@10.11.0.110"]

# peregrinel_LICENSE
environment["peregrinel_LICENSE"] = ["5053@10.11.0.110"]

# MAYA_VP2_DEVICE_OVERRIDE
environment["MAYA_VP2_DEVICE_OVERRIDE"] = ["VirtualDeviceDx11"]

# MAYA_FORCE_DX_WARP
environment["MAYA_FORCE_DX_WARP"] = ["1"]

# MAYA_MODULE_PATH
environment["MAYA_MODULE_PATH"] = [
    r"\\10.11.0.184\_tgbvfx\_bin\maya\mtoa\1.4.2.2_2017",
    r"\\10.11.0.184\_tgbvfx\_bin\maya\yeti\2.1.14_2017",
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

# ARNOLD_PLUGIN_PATH
environment["ARNOLD_PLUGIN_PATH"] = [
    r"\\10.11.0.184\_tgbvfx\_bin\alshaders\1.0.0rc19-ai4.2.12.2\bin"
]

# MTOA_TEMPLATES_PATH
environment["MTOA_TEMPLATES_PATH"] = [
    r"\\10.11.0.184\_tgbvfx\_bin\alshaders\1.0.0rc19-ai4.2.12.2\ae"
]

# MAYA_CUSTOM_TEMPLATE_PATH
environment["MAYA_CUSTOM_TEMPLATE_PATH"] = [
    r"\\10.11.0.184\_tgbvfx\_bin\alshaders\1.0.0rc19-ai4.2.12.2\aexml"
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

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "houdini"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "create_structure"
    ),
    os.path.join(root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
]

# FTRACK_EVENT_PLUGIN_PATH
environment["FTRACK_EVENT_PLUGIN_PATH"] = [
    os.path.join(root, "environment", "FTRACK_EVENT_PLUGIN_PATH"),
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
