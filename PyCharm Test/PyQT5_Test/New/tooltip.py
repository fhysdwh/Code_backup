import sys

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QHBoxLayout, QWidget


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('控件提示')
        self.btn = QPushButton('提示按钮')
        self.btn.setToolTip('这是一个按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../images/test1.ico'))

    main = TooltipForm()

    main.show()

    sys.exit(app.exec_())
