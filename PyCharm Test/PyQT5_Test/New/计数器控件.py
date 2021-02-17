import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('计数器控件')
        self.resize(200, 50)
        layout = QVBoxLayout()
        self.lb = QLabel('年龄：')
        self.lb.setAlignment(Qt.AlignLeft)
        self.spinb = QSpinBox()
        self.spinb.setValue(22)
        self.spinb.setRange(1, 50)
        self.spinb.setSingleStep(2)
        self.spinb.valueChanged.connect(self.valueChanged)
        layout.addWidget(self.lb)
        layout.addWidget(self.spinb)

        self.setLayout(layout)

    def valueChanged(self):
        value = self.sender().value()
        self.lb.setText('年龄：' + str(value) )




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QSpinBoxDemo()
    mainWin.show()
    sys.exit(app.exec_())
