import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CheckBoxdemo(QWidget):
    def __init__(self):
        super(CheckBoxdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件')
        layout = QHBoxLayout()
        self.cb1 = QCheckBox('Quantumult X')
        self.cb1.setChecked(True)
        self.cb1.stateChanged.connect(self.cbstatus)
        self.cb2 = QCheckBox('Loon')
        self.cb2.stateChanged.connect(self.cbstatus)
        self.cb3 = QCheckBox('Surge')
        self.cb3.setCheckState(Qt.PartiallyChecked)
        self.cb3.stateChanged.connect(self.cbstatus)


        layout.addWidget(self.cb1)
        layout.addWidget(self.cb2)
        layout.addWidget(self.cb3)
        self.setLayout(layout)

    def cbstatus(self):
        cb1_status = str(self.cb1.text()) + '的状态：' + str(self.cb1.checkState()) + '是否被选中：' + str(self.cb1.isChecked())
        cb2_status = str(self.cb2.text()) + '的状态：' + str(self.cb2.checkState()) + '是否被选中：' + str(self.cb2.isChecked())
        cb3_status = str(self.cb3.text()) + '的状态：' + str(self.cb3.checkState()) + '是否被选中：' + str(self.cb3.isChecked())
        print(cb1_status)
        print(cb2_status)
        print(cb3_status)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CheckBoxdemo()
    mainWin.show()
    sys.exit(app.exec_())
