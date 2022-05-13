from PyQt5 import QtWidgets
from test_gui2 import Ui_MainWindow
import sys



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    app.exec_()