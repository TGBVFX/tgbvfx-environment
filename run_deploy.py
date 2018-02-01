import os
from datetime import datetime
import subprocess
import shutil

from github import Github


# Create GitHub release title
g = Github(os.environ["GITHUB_TOKEN"])

repository = None
for repo in g.get_user().get_repos():
    if repo.name == "tgbvfx-environment":
        repository = repo

release_titles = []
for release in repository.get_releases():
    release_titles.append(release.title)

release_version = 1
release_title = ""
while True:
    release_title = "{0}.{1}.{2}.{3}".format(
        datetime.now().year,
        datetime.now().month,
        datetime.now().day,
        release_version
    )
    if release_title in release_titles:
        release_version += 1
    else:
        break

# Build deployment zip
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
        "{0}.zip".format(release_title)
    )
)

# Create GitHub release
print "Creating release \"{0}\"".format(release_title)

release = repository.create_git_tag_and_release(
    release_title,
    "Automatic Deployment",
    release_title,
    "Automatic Deployment",
    repository.get_commits()[0].sha,
    "commit"
)

print "Uploading deployment.zip..."

# Currently a bare try/except because the upload errors out falsely
# https://github.com/PyGithub/PyGithub/issues/693
try:
    release.upload_asset(
        os.path.abspath(
            os.path.join(__file__, "..", "{0}.zip".format(release_title))
        )
    )
except:
    pass
