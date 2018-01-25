import os
import requests
import zipfile
import subprocess
import stat


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


def on_rm_error(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def main():
    os.environ["CONDA_ATTACHED"] = "True"

    root = os.path.abspath(os.path.join(__file__, ".."))

    # Create build directory
    build_directory = os.path.join(os.path.expanduser("~"), "build")
    if not os.path.exists(build_directory):
        os.makedirs(build_directory)

    # Download conda-git-deployment
    path = os.path.join(build_directory, "deployment.zip")
    download_file(
        "https://github.com/tokejepsen/conda-git-deployment/archive/"
        "relocatable_environments.zip",
        path
    )
    zip_file = zipfile.ZipFile(path)
    zip_file.extractall(build_directory)

    # Rename unzipped content
    os.rename(
        os.path.join(
            build_directory,
            "conda-git-deployment-relocatable_environments"
        ),
        os.path.join(
            build_directory,
            "deployment"
        )
    )

    # Installing the environment
    subprocess.call(
        [
            os.path.join(
                build_directory,
                "deployment",
                "startup.bat"
            ),
            "--environment",
            os.path.join(root, "environment.yml")
        ]
    )

    # Run environment setups
    os.environ["CONDA_SKIP_COMMANDS"] = "True"
    os.environ["CONDA_GIT_REPOSITORY"] = os.path.join(
        build_directory,
        "deployment",
        "repositories",
    )
    subprocess.call(
        [
            os.path.join(
                build_directory,
                "deployment",
                "startup.bat"
            ),
            "&",
            "activate",
            "tgbvfx-environment",
            "&",
            "python",
            os.path.join(
                build_directory,
                "deployment",
                "repositories",
                "tgbvfx-environment",
                "tgbvfx-environment",
                "environment_setup.py"
            )
        ]
    )

    subprocess.call(
        [
            os.path.join(
                build_directory,
                "deployment",
                "startup.bat"
            ),
            "--environment",
            os.path.join(root, "environment.yml"),
            "&",
            "activate",
            "tgbvfx-environment",
            "&",
            "python",
            os.path.join(
                build_directory,
                "deployment",
                "repositories",
                "tgbvfx-environment",
                "ftrack-connect-environment",
                "environment_setup.py"
            )
        ]
    )


if __name__ == "__main__":
    main()
