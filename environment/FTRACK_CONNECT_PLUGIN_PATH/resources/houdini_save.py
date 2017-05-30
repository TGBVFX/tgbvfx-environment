import sys

import hou


path = sys.argv[1]

print "Saving workfile to: \"{0}\"".format(path)
hou.hipFile.save(file_name=path)
