from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton

from ..common import util


class UIButton(object):

    def __init__(self,name, QtWidget):
        self.btn = QPushButton(QtWidget)
        self.btn.setObjectName(name)

    def withStyleSheet(self, path):
        self.btn.setStyleSheet(util.openStyleSheet(path))
        return self

    def withMaxSize(self, width, height):
        self.btn.setMaximumSize(QtCore.QSize(width, height))
        return self

    def enabled(self, isEnabled):
        self.btn.setEnabled(isEnabled)
        return self

    def applydefaults(self):
        self.btn.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn.setBaseSize(QtCore.QSize(0, 0))
        return self

    def setBtnText(self,text):
        self.btn.setText(text)
        return self

    def setToolTip(self):
        print("adding tool tip")

    def addToContainer(self, container : QtWidgets.QVBoxLayout,stretch, layout):
        container.addWidget(self.btn,stretch,layout)
        return self

    def build(self):
        return self.btn
