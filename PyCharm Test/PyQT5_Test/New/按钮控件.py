import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class buttondemo(QWidget):
    def __init__(self):
        super(buttondemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('普通按钮控件')
        layout = QVBoxLayout()

        self.btn1 = QPushButton('按钮1')
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda:self.clickWhichBtn(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('按钮2')
        self.btn2.clicked.connect(self.changeEnable)
        layout.addWidget(self.btn2)

        self.setLayout(layout)

    def clickWhichBtn(self, btn):
        print('您点击的按钮是<'+btn.text()+'>')

    def changeEnable(self):
        if self.btn1.isEnabled():
            self.btn1.setEnabled(False)
        else:
            self.btn1.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = buttondemo()
    mainWin.show()
    sys.exit(app.exec_())
