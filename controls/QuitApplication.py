

import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QWidget, QPushButton

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(400,300)
        self.setWindowTitle('退出应用程序')

        # 添加Button

        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

        # 按钮单机事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('C:\\Users\\user\\Desktop\\证件\\icon图片.ico'))
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())
