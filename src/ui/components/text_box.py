from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit, QTextEdit
from ..common import util


class TextEdit(object):

    def __init__(self, name, container_frame: QtWidgets.QWidget):
        self.text_box = QLineEdit(container_frame)
        self.text_box.setObjectName(name)

    def withStyleSheet(self, stylesheet):
        self.text_box.setStyleSheet(util.openStyleSheet(stylesheet))
        return self

    def setToolTip(self, text):
        self.text_box.setToolTip(text)
        return self

    def qComp(self):
        return self.text_box


class TextBoxEdit(object):

    def __init__(self,name,  container_frame: QtWidgets.QWidget):
        self.text_box_edit = QTextEdit(container_frame)
        self.text_box_edit.setObjectName(name)

    def withStyleSheet(self, styleSheet):
        self.text_box_edit.setStyleSheet(util.openStyleSheet(styleSheet))
        return self

    def setToolTip(self, text):
        self.text_box_edit.setToolTip(text)
        return self

    def qComp(self):
        return self.text_box_edit
