import sys
from PyQt5 import QtWidgets
from model import ModelInterface
from ui import Ui_MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()

    # model init
    model = ModelInterface()
    model.register()

    ui = Ui_MainWindow(model, mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())