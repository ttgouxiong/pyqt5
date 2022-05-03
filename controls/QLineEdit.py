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

class QLineEditEchomode(QWidget):
    def __init__(self):
        super(QLineEditEchomode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        NoEchoLineEdit = QLineEdit()
        PasswordLineEdit = QLineEdit()
        PasswordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', normalLineEdit)
        formLayout.addRow('NoEcho', NoEchoLineEdit)
        formLayout.addRow('Password', PasswordLineEdit)
        formLayout.addRow('PasswordEchoOnEdit', PasswordEchoOnEditLineEdit)

      # placeholdertext
        normalLineEdit.setPlaceholderText('Normal')
        NoEchoLineEdit.setPlaceholderText('NoEchoLineEdit')
        PasswordLineEdit.setPlaceholderText('PasswordLineEdit')
        PasswordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEditLineEdit')


        normalLineEdit.setEchoMode(QLineEdit.Normal)
        NoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        PasswordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchomode()
    main.show()
    sys.exit(app.exec_())
