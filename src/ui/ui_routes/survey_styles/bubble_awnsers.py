from PyQt5 import QtWidgets, QtCore
from src import ModelInterface
from ui.common import Constants
from ui.components.buttons import Button


class BubbleStyle(QtWidgets.QWidget):

    def __init__(self, frame, model: ModelInterface=None):
        super().__init__(frame)
        self.model = model

    def init_ui(self):
        self.setObjectName("bubble_style_page")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(2, 2, 760, 170))
        self.gridLayoutWidget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(100, 13, 100, 32)
        self.gridLayout.setHorizontalSpacing(100)
        self.gridLayout.setObjectName("gridLayout")

        self.bubble_1 = Button("bubble_1", self.gridLayoutWidget).setBtnText("Awnser 1") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.gridLayout, 0, QtCore.Qt.AlignVCenter).qComp()
        self.gridLayout.addWidget(self.bubble_1, 0, 0, 1, 1)

        self.bubble_2 = Button("bubble_2", self.gridLayoutWidget).setBtnText("Awnser 2") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.gridLayout, 0, QtCore.Qt.AlignVCenter).qComp()
        self.gridLayout.addWidget(self.bubble_2, 0, 1, 1, 1)

        self.bubble_3 = Button("bubble_3", self.gridLayoutWidget).setBtnText("Awnser 3") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.gridLayout, 0, QtCore.Qt.AlignVCenter).qComp()
        self.gridLayout.addWidget(self.bubble_3, 2, 0, 1, 1)

        self.bubble_4 = Button("bubble_4", self.gridLayoutWidget).setBtnText("Awnser 4") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.gridLayout, 0, QtCore.Qt.AlignVCenter).qComp()
        self.gridLayout.addWidget(self.bubble_4, 2, 1, 1, 1)
