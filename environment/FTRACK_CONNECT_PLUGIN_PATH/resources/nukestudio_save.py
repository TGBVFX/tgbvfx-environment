import sys

import hiero.core


path = sys.argv[1]

print "Saving workfile to: \"{0}\"".format(path)
project = hiero.core.newProject()
project.saveAs(path)
