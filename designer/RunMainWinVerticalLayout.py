import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinVerticalLayout import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())