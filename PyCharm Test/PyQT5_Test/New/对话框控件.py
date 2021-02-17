import sys

from PyQt5.QtWidgets import *


class QDialogDemo(QWidget):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框案例')
        self.resize(500, 300)
        self.btn = QPushButton('点我！', self)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dl = QDialog()
        btn = QPushButton('关闭', dl)
        btn.clicked.connect(dl.close)
        dl.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())
