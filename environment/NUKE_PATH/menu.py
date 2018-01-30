import os
import shutil
import datetime

import nuke


# Setup Global copy/paste
menubar = nuke.menu('Nuke')
menu = menubar.menu('Edit')

path = os.path.join(os.environ["STUDIO_TMP"], "global_nuke_tmp.nk")
menu.addCommand(
    "Global Copy",
    "nuke.nodeCopy(\"{0}\")".format(path),
    "shift+alt+c",
    index=5
)
menu.addCommand(
    "Global Paste",
    "nuke.nodePaste(\"{0}\")".format(path),
    "shift+alt+v",
    index=7
)

# Setup common directories.
nuke.addFavoriteDir("Studio Library", "//10.10.200.18/171000_TGB_Library/Stock")


# Backup Nuke script on save.
def on_script_save():
    source = nuke.root().name()

    if not os.path.exists(source):
        return

    target = os.path.abspath(
        os.path.join(
            source,
            "..",
            "workspace",
            "backup",
            "{0}_{1}.nk".format(
                os.path.basename(os.path.splitext(source)[0]),
                datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            )
        )
    )

    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target))

    shutil.copy(source, target)


nuke.addOnScriptSave(on_script_save)
