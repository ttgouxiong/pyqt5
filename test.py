
from PyQt5.QtWidgets import *
import sys
import time

# 定义全局变量后面才能直接获取到值
a = 'd'

class QLineEditEchomode(QWidget):
    def __init__(self):
        super().__init__()

        # 下面这两个需要在类的初始方法这里定义才行，后面调用
        self.normalLineEdit = QLineEdit()
        self.text = '213'

        self.resize(400,100)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formLayout = QFormLayout()
        formLayout.addRow('Normal', self.normalLineEdit)


      # placeholdertext
        self.normalLineEdit.setPlaceholderText('Normal')
        self.normalLineEdit.setEchoMode(QLineEdit.Normal)

        self.setLayout(formLayout)

        # 目前是要有这部分才能获取到值，直接获取的话获取不到
        self.normalLineEdit.editingFinished.connect(self.get_content)


    def get_content(self):
        self.text = self.normalLineEdit.text()
        # 定义全局变量才能改变最上面定义的值
        global a
        a = self.text
        print(self.text)


app = QApplication(sys.argv)
main = QLineEditEchomode()
main.show()
print(2)

# 这里不能直接系统退出，不然获取不到值
app.exec_()


print(f'111{a}')
print('\n\n')
print(a)