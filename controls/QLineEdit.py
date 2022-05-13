'''
QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode（回显模式）

支持4种回显模式

1、Normal
2、NoEcho
3、Password
4、PasswordEchoOnEdit

'''


from PyQt5.QtWidgets import *
import sys
import time

class QLineEditEchomode(QWidget):
    def __init__(self):
        super(QLineEditEchomode, self).__init__()
        self.normalLineEdit = QLineEdit()
        self.text = '213'
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        NoEchoLineEdit = QLineEdit()
        PasswordLineEdit = QLineEdit()
        PasswordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', self.normalLineEdit)
        formLayout.addRow('NoEcho', NoEchoLineEdit)
        formLayout.addRow('Password', PasswordLineEdit)
        formLayout.addRow('PasswordEchoOnEdit', PasswordEchoOnEditLineEdit)

      # placeholdertext
        self.normalLineEdit.setPlaceholderText('Normal')
        NoEchoLineEdit.setPlaceholderText('NoEchoLineEdit')
        PasswordLineEdit.setPlaceholderText('PasswordLineEdit')
        PasswordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEditLineEdit')


        self.normalLineEdit.setEchoMode(QLineEdit.Normal)
        NoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        PasswordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)
        self.normalLineEdit.editingFinished.connect(self.get_content)


    def get_content(self):
        print(self.normalLineEdit.text())
        self.text = self.normalLineEdit.text()
        print(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchomode()
    main.show()
    print(main.text)
    sys.exit(app.exec_())