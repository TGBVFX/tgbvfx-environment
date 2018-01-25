import os
import subprocess
import shutil


def main():
    os.environ["CONDA_ATTACHED"] = "True"

    build_directory = os.path.join(os.path.expanduser("~"), "build")

    subprocess.call(
        [
            os.path.join(build_directory, "deployment", "startup.bat"),
            "--export-deployment",
            "--environment",
            os.path.abspath(os.path.join(__file__, "..", "environment.yml"))
        ]
    )

    shutil.copy(
        os.path.join(
            build_directory,
            "deployment",
            "deployment.zip"
        ),
        os.path.join(
            os.path.dirname(__file__),
            "deployment.zip"
        )
    )


if __name__ == "__main__":
    main()
