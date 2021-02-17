import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RadioDemo(QWidget):
    def __init__(self):
        super(RadioDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')
        layout = QHBoxLayout()
        self.radioBtn1 = QRadioButton('男')
        self.radioBtn1.setChecked(True)
        # self.radioBtn1.toggled.connect(self.sexChoose)
        self.radioBtn1.clicked.connect(self.sexChoose)
        layout.addWidget(self.radioBtn1)
        self.radioBtn2 = QRadioButton('女')
        # self.radioBtn2.toggled.connect(self.sexChoose)
        self.radioBtn2.clicked.connect(self.sexChoose)
        layout.addWidget(self.radioBtn2)

        self.setLayout(layout)

    def sexChoose(self):
        rbtn = self.sender()
        if rbtn == self.radioBtn1:
            print('你的性别是：' + self.radioBtn1.text())

        else:
            print('您的性别是：' + self.radioBtn2.text())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = RadioDemo()
    mainWin.show()
    sys.exit(app.exec_())
