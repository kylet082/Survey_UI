from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel


class Label(object):

    def __init__(self, name, container_frame: QtWidgets.QWidget):
        self.name = name
        self.label = QLabel(container_frame)
        self.label.setObjectName(name)

    def setText(self, text):
        self.label.setText(text)
        return self

    def qComp(self):
        return self.label
