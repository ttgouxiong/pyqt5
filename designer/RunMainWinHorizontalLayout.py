import sys
import MainWinHorizontalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 先创建一个程序
    app = QApplication(sys.argv)
    # 创建一个主窗口
    mainMindow = QMainWindow()
    ui = MainWinHorizontalLayout.Ui_MainWindow()
    # 向主窗口上添加控件
    ui.setupUi(mainMindow)
    mainMindow.show()
    sys.exit(app.exec_())