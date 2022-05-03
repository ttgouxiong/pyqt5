import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton

def onClick():
    print('1')
    print(f'widget.x() = {widget.x()}')  # 窗口横坐标
    print(f'widget.y() = {widget.y()}')  # 窗口纵坐标
    print(f'widget.width() = {widget.width()}')  # 工作区宽度
    print(f'widget.height() = {widget.height()}')  # 工作区高度

    print('1')
    print(f'widget.geometry().x() = {widget.geometry().x()}')  # 工作区横坐标
    print(f'widget.geometry().y() = {widget.geometry().y()}')  # 工作区纵坐标
    print(f'widget.geometry().width() = {widget.geometry().width()}')  # 工作区宽度
    print(f'widget.geometry().height() = {widget.geometry().height()}')  # 工作区高度

    print('1')
    print(f'widget.frameGeometry().x() = {widget.frameGeometry().x()}')  # 窗口横坐标
    print(f'widget.frameGeometry().y() = {widget.frameGeometry().y()}')  # 窗口纵坐标
    print(f'widget.frameGeometry().width() = {widget.frameGeometry().width()}')  # 窗口宽度
    print(f'widget.frameGeometry().height() = {widget.frameGeometry().height()}')  # 窗口高度


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick)

btn.move(24,52)
widget.resize(300,240)

widget.move(250, 200)

widget.setWindowTitle('屏幕坐标系')

# widget.move()

widget.show()

sys.exit(app.exec_())