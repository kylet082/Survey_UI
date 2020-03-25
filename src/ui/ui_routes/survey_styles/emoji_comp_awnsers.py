from PyQt5 import QtWidgets, QtCore

from src import ModelInterface
from ui.common import Constants
from ui.components.buttons import Button


class EmojiCompStyle(QtWidgets.QWidget):

    def __init__(self, frame, model: ModelInterface=None):
        super().__init__(frame)
        self.model = model

    def setup(self):
        self.setObjectName("multiple_emoji_page")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(1, 1, 775, 170))
        self.widget.setObjectName("widget")
        self.layout = QtWidgets.QHBoxLayout(self.widget)
        self.layout.setContentsMargins(45, 0, 45, 0)
        self.layout.setSpacing(70)
        self.layout.setObjectName("layout")

        self.happy_btn = Button("happy_btn",self.widget).setBtnText("smily pic") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.expressionless_btn = Button("expressionless_btn", self.widget).setBtnText("mmh pic") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.happy_btn = Button("unhappy_btn", self.widget).setBtnText("unhappy pic") \
            .enabled(True).withStyleSheet(Constants.BUBBLE_BUTTON_STYLESHEET) \
            .addToContainer(self.layout, 0, QtCore.Qt.AlignVCenter).qComp()

