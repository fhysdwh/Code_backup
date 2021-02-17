import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')
        self.resize(50, 100)
        layout = QVBoxLayout()
        self.btn1 = QPushButton('关于')
        self.btn2 = QPushButton('信息')
        self.btn3 = QPushButton('警告')
        self.btn4 = QPushButton('错误')
        self.btn5 = QPushButton('提问')

        self.btn1.clicked.connect(self.showDialog)
        self.btn2.clicked.connect(self.showDialog)
        self.btn3.clicked.connect(self.showDialog)
        self.btn4.clicked.connect(self.showDialog)
        self.btn5.clicked.connect(self.showDialog)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)

        self.setLayout(layout)

    def showDialog(self):
        title = self.sender().text()

        if title == '关于':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        if title == '信息':
            QMessageBox.information(self,'关于','这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)
        if title == '警告':
            QMessageBox.warning(self,'关于','这是一个警告对话框', QMessageBox.Yes | QMessageBox.No)
        if title == '错误':
            QMessageBox.critical(self,'关于','这是一个错误对话框', QMessageBox.Yes | QMessageBox.No)
        if title == '提问':
            QMessageBox.question(self,'关于','这是一个提问对话框', QMessageBox.Yes | QMessageBox.No)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Demo()
    mainWin.show()
    sys.exit(app.exec_())
