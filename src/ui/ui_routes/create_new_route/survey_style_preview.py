from PyQt5 import QtWidgets, QtCore

from src import ModelInterface
from ui.ui_routes.survey_styles.bubble_awnsers import BubbleStyle
from ui.ui_routes.survey_styles.emoji_awnsers import EmojiStyle
from ui.ui_routes.survey_styles.emoji_comp_awnsers import EmojiCompStyle
from ui.common import Constants, util
from ui.components.buttons import Button


class SurveyStyle(object):

    def __init__(self, model: ModelInterface, container_frame: QtWidgets.QFrame, state):
        self.container_frame = container_frame
        self.model = model
        self.state = state

    def setup(self):
        self.survey_type_frame = QtWidgets.QFrame(self.container_frame)
        self.survey_type_frame.setGeometry(QtCore.QRect(10, 290, 780, 180))
        self.survey_type_frame.setStyleSheet(util.openStyleSheet(Constants.WIDGET_STYLESHEET))
        self.survey_type_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.survey_type_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.survey_type_frame.setObjectName("survey_type_frame")
        self.survey_type_stackedWidget = QtWidgets.QStackedWidget(self.survey_type_frame)
        self.survey_type_stackedWidget.setGeometry(QtCore.QRect(0, 0, 780, 180))
        self.survey_type_stackedWidget.setStyleSheet(util.openStyleSheet(Constants.WIDGET_STYLESHEET))
        self.survey_type_stackedWidget.setObjectName("survey_type_stackedWidget")

        self.bubble_page = BubbleStyle(None, self.model)
        self.bubble_page.setup()
        self.edit_btn = Button("edit_btn", self.bubble_page).setBtnText("edit").enabled(True) \
                .withStyleSheet(Constants.BUTTON_STYLESHEET).addGeometry(690,135,80,40)

        self.survey_type_stackedWidget.addWidget(self.bubble_page)

        self.emoji_comp_page = EmojiCompStyle(None, self.model)
        self.emoji_comp_page.setup()

        self.survey_type_stackedWidget.addWidget(self.emoji_comp_page)

        self.emoji_page = EmojiStyle(None, self.model)
        self.emoji_page.setup()
        self.survey_type_stackedWidget.addWidget(self.emoji_page)

        print(self.survey_type_stackedWidget.count())

    def getStackedWidget(self) -> QtWidgets.QStackedWidget:
        return self.survey_type_stackedWidget
