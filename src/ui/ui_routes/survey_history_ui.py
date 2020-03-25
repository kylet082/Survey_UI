from PyQt5 import QtWidgets, QtCore

from model import ModelInterface


class SurveyHistoryRoute(QtWidgets.QWidget):

    def __init__(self, model: ModelInterface, frame: QtWidgets.QFrame):
        super().__init__(frame)
        self.frame = frame
        self.model = model

    def init_ui(self):
        btn_container = QtWidgets.QVBoxLayout(self)
        btn_container.setContentsMargins(280, 72, 0, 155)
        btn_container.setObjectName("center_btn_container")

        self.show()