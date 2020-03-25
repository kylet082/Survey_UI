from PyQt5 import QtWidgets, QtCore

from model import ModelInterface

from ..components.buttons import Button
from ..common import Constants
from ui.ui_routes.create_new_route.create_new_ui import CreateNewRoute
from .launch_survey_ui import LaunchSurveyRoute
from .survey_history_ui import SurveyHistoryRoute


class MenuRoute(QtWidgets.QWidget):

    def __init__(self, main_window: QtWidgets.QMainWindow, model: ModelInterface, frame: QtWidgets.QFrame):
        super().__init__(frame)
        self.frame = frame
        self.model = model
        self.main_window = main_window

    def set_up(self):
        self.__layout()

        # buttons
        self.create_new_btn = Button("create_new_btn", self).setBtnText("Create New") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.btn_container, 0, QtCore.Qt.AlignVCenter).qComp()

        self.launch_survey_btn = Button("launch_survey_btn", self).setBtnText("Launch Survey") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.btn_container, 0, QtCore.Qt.AlignVCenter).qComp()

        self.survey_history_btn = Button("survey_history_btn", self).setBtnText("Survey History") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.btn_container, 0, QtCore.Qt.AlignVCenter).qComp()

        self.exit_btn = Button("exit_btn", self).setBtnText("Exit") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.btn_container, 0, QtCore.Qt.AlignVCenter).qComp()

        self.register_listeners()

    def __layout(self):
        self.btn_container = QtWidgets.QVBoxLayout(self)
        self.btn_container.setContentsMargins(280, 72, 0, 155)
        self.btn_container.setObjectName("center_btn_container")

    def register_listeners(self):
        self.create_new_btn.clicked.connect(self.create_new_event)
        self.launch_survey_btn.clicked.connect(self.launch_survey_event)
        self.survey_history_btn.clicked.connect(self.survey_history_event)
        self.exit_btn.clicked.connect(self.exit_event)

    def create_new_event(self):
        ui_create_new = CreateNewRoute(self.model, self.frame)
        self.setHidden(True)
        ui_create_new.setup()

    def launch_survey_event(self):
        print("launch")
        ui_launch_survey = LaunchSurveyRoute(self.model, self.frame)
        self.setHidden(True)
        ui_launch_survey.setup()

    def survey_history_event(self):
        print("history")
        ui_survey_history = SurveyHistoryRoute(self.model, self.frame)
        self.setHidden(True)
        ui_survey_history.setup()

    def exit_event(self):
        print("closing")
        QtWidgets.qApp.quit()
