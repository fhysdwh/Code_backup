from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys

ui, _ = loadUiType('czbj.ui')


class TestUi(QMainWindow, ui):
    def __int__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def __init__(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TestUi()
    mainWin.show()
    sys.exit(app.exec_())
