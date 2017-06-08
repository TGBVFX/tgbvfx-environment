try:
    import pyblish_qml.settings as ps
except ImportError:
    pass
else:
    # Setting pyblish_qml window size bigger
    ps.WindowSize = (700, 600)
