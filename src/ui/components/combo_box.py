from PyQt5.QtWidgets import QComboBox
from ui.common import util


class ComboBox(object):

    def __init__(self, name, container_frame):
        self.comboBox = QComboBox(container_frame)
        self.comboBox.setObjectName(name)
        self.items = []

    def withStyleSheet(self, path):
        self.comboBox.setStyleSheet(util.openStyleSheet(path))
        return self

    def setItems(self, items):
        self.items = items
        self.comboBox.addItems(items)
        return self

    def qComp(self):
        return self.comboBox