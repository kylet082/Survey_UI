from PyQt5 import QtCore, QtWidgets
from model import ModelInterface
from .ui_routes.menu_ui import MenuRoute


class Ui_MainWindow(object):

    def __init__(self, model: ModelInterface, main_window: QtWidgets.QMainWindow):
        self.model = model
        self.init_ui(main_window)

    def init_ui(self, MainWindow):
        width = 801
        height = 481

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")

        # container that holds active widgets
        self.container_frame = QtWidgets.QFrame(self.centralwidget)
        self.container_frame.setGeometry(QtCore.QRect(0, 0, width, height))
        self.container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_frame.setObjectName("container_frame")

        self.route = MenuRoute(MainWindow, self.model, self.container_frame)
        self.route.setGeometry(self.container_frame.geometry())
        self.route.setObjectName("widget")
        self.route.init_ui()

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





