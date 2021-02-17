import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def onClickButton():
    print('点击按钮')
    print('widget.x()=%d' % widget.x())
    print('widget.y()=%d' % widget.y())
    print('widget.width()=%d' % widget.width())
    print('widget.height()=%d' % widget.height())
    print('widget.g()=%d' % widget.geometry().width())
    print('widget.g()=%d' % widget.geometry().height())
    print('widget.f()=%d' % widget.frameGeometry().width())
    print('widget.f()=%d' % widget.frameGeometry().height())


app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClickButton)
btn.move(24, 52)
widget.resize(800, 400)
widget.move(250, 200)
widget.setWindowTitle('屏幕窗口位置')
widget.show()
sys.exit(app.exec_())
