import os
import requests
import zipfile
import tempfile
import subprocess
import shutil
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


def create_deployment(temp_directory):
    root = os.path.abspath(os.path.join(__file__, ".."))

    # Download conda-git-deployment
    path = os.path.join(temp_directory, "deployment.zip")
    download_file(
        "https://github.com/tokejepsen/conda-git-deployment/archive/"
        "relocatable_environments.zip",
        path
    )
    zip_file = zipfile.ZipFile(path)
    zip_file.extractall(temp_directory)

    # Rename unzipped content
    os.rename(
        os.path.join(
            temp_directory,
            "conda-git-deployment-relocatable_environments"
        ),
        os.path.join(
            temp_directory,
            "deployment"
        )
    )

    # Installing the environment
    subprocess.call(
        [
            os.path.join(
                temp_directory,
                "deployment",
                "startup.bat"
            ),
            "--environment",
            os.path.join(root, "environment.yml")
        ]
    )

    # Exporting the deployment
    subprocess.call(
        [
            os.path.join(
                temp_directory,
                "deployment",
                "startup.bat"
            ),
            "--export-deployment",
            "--environment",
            os.path.join(root, "environment.yml")
        ]
    )


def on_rm_error(func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def main():
    os.environ["CONDA_ATTACHED"] = "True"

    # Temporary folder needs to be in user directory to avoid long paths that
    # won't zip
    directory = tempfile.mkdtemp()
    os.rmdir(directory)
    temp_directory = os.path.join(
        os.path.expanduser("~"), os.path.basename(directory)
    )
    os.makedirs(temp_directory)

    try:
        create_deployment(temp_directory)

        shutil.copy(
            os.path.join(
                temp_directory,
                "deployment",
                "deployment.zip"
            ),
            os.path.join(
                os.path.dirname(__file__),
                "deployment.zip"
            )
        )
    except Exception as e:
        print("Creating deployment failed: {0}".format(e))
    finally:
        shutil.rmtree(temp_directory, onerror=on_rm_error)


if __name__ == "__main__":
    main()
