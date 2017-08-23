import os

import nuke


menubar = nuke.menu('Nuke')
menu = menubar.menu('Edit')

path = os.path.join(os.environ["STUDIO_TMP"], "global_nuke_tmp.nk")
menu.addCommand(
    "Global Copy",
    "nuke.nodeCopy(\"{0}\")".format(path),
    "ctrl+shift+c",
    index=5
)
menu.addCommand(
    "Global Paste",
    "nuke.nodePaste(\"{0}\")".format(path),
    "ctrl+shift+v",
    index=7
)
