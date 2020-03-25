from src import ModelInterface
from PyQt5 import QtWidgets, QtCore
from ui.components.buttons import Button
from ui.common import Constants


class ToolBar(object):

    def __init__(self, model: ModelInterface, container_frame: QtWidgets.QWidget):
        self.model = model
        self.container_frame = container_frame

    def init_ui(self):
        self.toolbar_widget = QtWidgets.QWidget(self.container_frame)
        self.toolbar_widget.setGeometry(QtCore.QRect(10, 0, 781, 51))
        self.toolbar_widget.setObjectName("tool_bar_widget")
        self.toolbar_layout = QtWidgets.QHBoxLayout(self.toolbar_widget)
        self.toolbar_layout.setContentsMargins(410, 0, 0, 0)
        self.toolbar_layout.setObjectName("toolbar_layout")

        # buttons
        self.preview_btn = Button("preview_btn", self.container_frame).setBtnText("preview") \
            .enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.toolbar_layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.launch_btn = Button("launch_btn", self.container_frame).setBtnText("launch") \
            .enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.toolbar_layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.save_btn = Button("save_btn", self.container_frame).setBtnText("save") \
            .enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.toolbar_layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.back_btn = Button("back_btn", self.container_frame).setBtnText("back") \
            .enabled(True).withStyleSheet(Constants.BUTTON_STYLESHEET) \
            .addToContainer(self.toolbar_layout, 0, QtCore.Qt.AlignVCenter).qComp()

        self.__register_listeners()

    def __register_listeners(self):
        print("add button events here")