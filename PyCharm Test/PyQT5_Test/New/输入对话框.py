import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class InputDialogDemo(QWidget):
    def __init__(self):
        super(InputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框控件演示')
        layout = QFormLayout()
        self.ledit1 = QLineEdit()
        self.btn1 = QPushButton('选择')
        self.btn1.clicked.connect(self.chooseLanguage)
        layout.addRow(self.ledit1, self.btn1)
        self.ledit2 = QLineEdit()
        self.btn2 = QPushButton('输入学校')
        self.btn2.clicked.connect(self.inputSchool)
        layout.addRow(self.ledit2, self.btn2)
        self.ledit3 = QLineEdit()
        self.btn3 = QPushButton('输入年龄')
        self.btn3.clicked.connect(self.inputAge)
        layout.addRow(self.ledit3, self.btn3)
        self.setLayout(layout)

    def chooseLanguage(self):
        items = ('C', 'C++', 'Python', 'Java')
        item, ok = QInputDialog.getItem(self, '请选择编程语言','语言列表', items)
        if ok and item:
            self.ledit1.setText(item)

    def inputSchool(self):
        school, ok = QInputDialog.getText(self, '请输入学校名称', '请输入：')
        if school and ok:
            self.ledit2.setText(school)

    def inputAge(self):
        age, ok = QInputDialog.getInt(self, '请输入年龄','请输入：')
        if age and ok:
            self.ledit3.setText(str(age))







if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = InputDialogDemo()
    mainWin.show()
    sys.exit(app.exec_())

