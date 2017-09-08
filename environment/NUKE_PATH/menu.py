import os

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
nuke.addFavoriteDir("Studio Library", "//10.11.0.184/171000_TGB_Library/Stock")
