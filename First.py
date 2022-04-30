import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建一个QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400,150)
    # 移动窗口
    w.move(300, 500)

    # 设置窗口的标题
    w.setWindowTitle('第一个基于Pyqt5的桌面应用')
    # 显示窗口

    w.show()

    # 基于程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
