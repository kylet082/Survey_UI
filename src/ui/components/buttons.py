from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton
from ..common import util


class Button(object):

    def __init__(self,name, qtWidget):
        self.btn = QPushButton(qtWidget)
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

    def setToolTip(self, text):
        self.btn.setToolTip(text)
        return self

    def addGeometry(self, x, y, w, h):
        self.btn.setGeometry(QtCore.QRect(x, y, w, h))
        return self

    def addToContainer(self, container, stretch, layout):
        container.addWidget(self.btn,stretch,layout)
        return self

    def qComp(self):
        return self.btn
