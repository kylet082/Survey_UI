from PyQt5.QtWidgets import QPushButton

from controller import MenuController
from ..componets.buttons import UIButton
from ..common import Constants

from PyQt5 import QtWidgets, QtCore



class MenuRoute(object):

    def __init__(self,controller : MenuController, name, widget: QtWidgets.QWidget):
        self.name = name
        self.widget = widget
        self.controller = controller


    def set_up(self):

        # layout
        btn_container = QtWidgets.QVBoxLayout(self.widget)
        btn_container.setContentsMargins(280, 72, 0, 155)
        btn_container.setObjectName("center_btn_container")

        # buttons
        self.create_new_btn = UIButton("create_new_btn", self.widget).setBtnText("Create New") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(btn_container, 0, QtCore.Qt.AlignVCenter).build()

        self.launch_survey_btn = UIButton("launch_survey_btn", self.widget).setBtnText("Launch Survey") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(btn_container, 0, QtCore.Qt.AlignVCenter).build()

        self.survey_history_btn = UIButton("survey_history_btn", self.widget).setBtnText("Survey History") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(btn_container, 0, QtCore.Qt.AlignVCenter).build()

        self.exit_btn = UIButton("exit_btn", self.widget).setBtnText("Exit") \
            .withMaxSize(250, 40).enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(btn_container, 0, QtCore.Qt.AlignVCenter).build()

        self.register_listeners()

    def register_listeners(self):
        self.create_new_btn.clicked.connect(self.create_new_event)
        self.launch_survey_btn.clicked.connect(self.launch_survey_event)
        self.survey_history_btn.clicked.connect(self.survey_history_event)
        self.exit_btn.clicked.connect(self.exit_event)


    def create_new_event(self):
        print("create")

    def launch_survey_event(self):
        print("launch")

    def survey_history_event(self):
        print("history")

    def exit_event(self):
        print("closing")
        QtWidgets.qApp.quit()

    def creat_click(self):
        self.widget.setHidden(True)

    def update_route(self):
        self.widget.update()



