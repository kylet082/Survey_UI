from sqlite3 import connect

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

from src import ModelInterface
from ui.components.combo_box import ComboBox
from ui.components.label import Label
from ui.components.text_box import TextBoxEdit, TextEdit

from ui.common import Constants

class CreateNewForm(object):

    def __init__(self,model: ModelInterface, container_frame):
        self.container_frame = container_frame
        self.model = model

    def init_ui(self):
        self.form_frame = QtWidgets.QFrame(self.container_frame)
        self.form_frame.setGeometry(QtCore.QRect(10, 60, 780, 210))
        self.form_frame.setMaximumSize(QtCore.QSize(780, 270))
        self.form_frame.setStyleSheet("background:transparent;")
        self.form_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_frame.setObjectName("form_frame")

        self.form_widget = QtWidgets.QWidget(self.form_frame)
        self.form_widget.setGeometry(QtCore.QRect(10, 0, 760, 210))
        self.form_widget.setObjectName("form_widget")
        self.form_layout = QtWidgets.QFormLayout(self.form_widget)
        self.form_layout.setContentsMargins(85, 0, 150, 0)
        self.form_layout.setObjectName("form_layout")

        self.title_lbl = Label("title_lbl", self.form_widget).setText("Title")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_lbl.qComp())
        self.title_text_box = TextEdit("title_text_box", self.form_widget) \
            .withStyleSheet(Constants.TEXT_EDIT_STYLESHEET) \
            .setToolTip("Give your survey a title")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_text_box.qComp())

        self.descrip_lbl = Label("descrip_lbl", self.form_widget).setText("Description")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.descrip_lbl.qComp())
        self.description_text_box = TextBoxEdit("title_text_box", self.form_widget) \
            .withStyleSheet(Constants.TEXT_EDIT_STYLESHEET) \
            .setToolTip("Description of the survey...")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description_text_box.qComp())

        self.question_lbl = Label("survey_question_lbl", self.form_widget).setText("Survey Question")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.question_lbl.qComp())
        self.suvrey_question_text = TextBoxEdit("survey_question_text_box", self.form_widget) \
            .withStyleSheet(Constants.TEXT_EDIT_STYLESHEET) \
            .setToolTip("Add your survey question here")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.suvrey_question_text.qComp())

        self.survey_type_lbl = Label("survey_type_lbl", self.form_widget).setText("Survey Style")
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.survey_type_lbl.qComp())
        self.comboBox = ComboBox("survey_style_comboBox", self.form_widget) \
            .withStyleSheet(Constants.COMBOBOX_STYLESHEET).setItems(["Bubble Style", "Multiple Emoji", "Binary Emoji"]).qComp()
        self.form_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.__register_listeners()

    def __register_listeners(self):
        self.comboBox.currentTextChanged.connect(self.__combobox_event)

    def set_combox_items_options(self, items: QtWidgets.QStackedWidget):
        self.items = items

    def __combobox_event(self):
        selected = "{}_page".format(self.comboBox.currentText().lower().replace(" ", "_"))
        for i in range(self.items.count()):
            if self.items.widget(i).objectName() == selected:
                self.items.setCurrentIndex(i)
                break
