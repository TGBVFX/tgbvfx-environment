import sys

from Qt import QtWidgets, QtCore


class Window(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Pipeline")
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowFlags(
            self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint
        )
        body = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel(
            "Pipeline out of data. Please restart your pipeline."
        )
        body.addWidget(label)

        title = "OK"
        self.button = QtWidgets.QPushButton(title)
        body.addWidget(self.button)

        # Functionality
        self.button.clicked.connect(self.close)


QtWidgets.QApplication(sys.argv)
win = Window()
win.exec_()
