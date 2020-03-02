from PyQt5.QtWidgets import QPushButton

from ..componets.buttons import UIButton
from ..common import Constants
from PyQt5 import QtWidgets, QtCore

class MenuRoute(object):

    def __init__(self, name, frame, container_frame):
        self.frame = frame
        self.name = name
        self.container_frame = container_frame


    def set_up(self):
        # init frame and qwidget to attach objects
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(self.frame.geometry())
        self.widget.setObjectName("widget")

        # layout
        btn_container = QtWidgets.QVBoxLayout(self.container_frame)
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


    def update_route(self):
        self.widget.update()

    def get_create_new_btn(self):
        return self.create_new_btn

    def get_launch_survey_btn(self):
        return self.launch_survey_btn

    def get_survey_history_btn(self):
        return self.survey_history_btn

    def get_exit_btn(self):
        return self.exit_btn

