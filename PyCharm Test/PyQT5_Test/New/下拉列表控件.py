import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Comboxdemo(QWidget):
    def __init__(self):
        super(Comboxdemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表')
        layout = QVBoxLayout()
        self.lb = QLabel('请选择你使用的软件：')
        self.cb = QComboBox()
        self.cb.addItems(['Quantumult X', 'Surge', 'Loon', 'ShadowRocket'])
        self.cb.setCurrentIndex(1)
        self.cb.currentIndexChanged.connect(self.showStatus)

        self.ledit = QLineEdit()
        self.ledit.setPlaceholderText('请输入要添加的软件名称')

        self.btn = QPushButton('添加')
        self.btn.clicked.connect(self.addItem)


        layout.addWidget(self.lb)
        layout.addWidget(self.cb)
        layout.addWidget(self.ledit)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def showStatus(self):
        for _ in range(self.cb.count()):
            print('选项：' + str(_ + 1) + '\t' + str(self.cb.itemText(_)))
        print('当前选择项为：' + str(self.cb.currentIndex() + 1) + ' - ' + self.cb.currentText())

    def addItem(self):
        newItem = self.ledit.text()
        print(newItem)
        if newItem:
            self.cb.addItem(newItem)
            self.cb.setCurrentIndex(self.cb.count() - 1)
        else:
            print('请先输入要添加的内容！')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Comboxdemo()
    mainWin.show()
    sys.exit(app.exec_())
