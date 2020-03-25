from PyQt5 import QtWidgets

from model import ModelInterface
from ui.ui_routes.create_new_route.survey_style_preview import SurveyStyle
from ui.ui_routes.create_new_route.toolbar import ToolBar
from ui.ui_routes.create_new_route.create_form import CreateNewForm


class CreateNewRoute(QtWidgets.QWidget):

    def __init__(self, model: ModelInterface, frame: QtWidgets.QFrame):
        super().__init__(frame)
        self.frame = frame
        self.model = model

    def setup(self):
        self.setStyleSheet("background-color:white;")

        toolbar = ToolBar(self.model, self)
        toolbar.setup()

        self.survey_style = SurveyStyle(self.model, self, "preview")
        self.survey_style.setup()

        self.form = CreateNewForm(self.model, self)
        self.form.setup()
        self.form.set_combox_items_options(self.survey_style.getStackedWidget())

        self.show()

