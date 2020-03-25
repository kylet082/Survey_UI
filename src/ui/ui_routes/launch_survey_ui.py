from PyQt5 import QtWidgets

from model import ModelInterface


class LaunchSurveyRoute(QtWidgets.QWidget):

    def __init__(self, model: ModelInterface, frame: QtWidgets.QFrame):
        super().__init__(frame)
        self.frame = frame
        self.model = model

    def setup(self):
        btn_container = QtWidgets.QVBoxLayout(self)
        btn_container.setContentsMargins(280, 72, 0, 155)
        btn_container.setObjectName("center_btn_container")

        self.show()