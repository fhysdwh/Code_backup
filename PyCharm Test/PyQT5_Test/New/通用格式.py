import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('控件演示')
        # self.resize(1920, 1080)
        layout = QVBoxLayout()

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Demo()
    mainWin.show()
    sys.exit(app.exec_())

