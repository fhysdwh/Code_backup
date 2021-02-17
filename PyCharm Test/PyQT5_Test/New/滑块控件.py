import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SliderDemo(QWidget):
    def __init__(self):
        super(SliderDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件')
        self.resize(500, 300)
        layout = QVBoxLayout()

        self.lb = QLabel('滑动调整文字大小')
        self.lb.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(36)
        self.slider.setSingleStep(3)
        self.slider.setValue(15)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.valueChange)

        layout.addWidget(self.lb)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def valueChange(self):
        value = self.slider.value()
        print(value)
        self.lb.setFont(QFont('Arial', value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = SliderDemo()
    mainWin.show()
    sys.exit(app.exec_())
