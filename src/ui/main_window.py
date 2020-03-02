from PyQt5 import QtCore, QtWidgets
from .UiRoutes.menu_route import MenuRoute


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        width = 801
        height = 481
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")

        self.container_frame = QtWidgets.QFrame(self.centralwidget)
        self.container_frame.setGeometry(QtCore.QRect(0, 0, width, height))
        self.container_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_frame.setObjectName("container_frame")

        self.route = MenuRoute("menu_container", self.centralwidget, self.container_frame)
        self.route.set_up()

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def activte_content_widge(self, MainWindow):
        print("active ui")

    def getMenuRoute(self):
        return self.route



