'''
QLabel控件

setAlignment():  设置文本的对其方式

setIndent(): 设置文本缩进

QLabel常用的信号（事件）：
1、当鼠标划过QLabel控件时触发：linkKovered
2、当鼠标点击Qlabel控件时触发：linkActived

'''


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # 设置窗口的尺寸
        self.resize(400, 300)

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签.</font>')
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序<\a>")


        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')
        # label3.setPixmap(QPixmap("C:\Users\user\Desktop\证件\icon图片"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://www.zhihu.com/'>感谢关注tt狗熊</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('Qlabel')

    def linkHovered(self):
        print('当鼠标划过label2标签触发事件')

    def linkClicked(self):
        print('当鼠标点击label4触发时间')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelDemo()
    main.show()
    sys.exit(app.exec_())


