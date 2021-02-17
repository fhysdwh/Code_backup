import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class QlineEditDemo(QWidget):

    def __init__(self):
        super(QlineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入框案例")

        ledit1 = QLineEdit()
        ledit1.setValidator(QIntValidator())
        ledit1.setMaxLength(6)
        ledit1.setAlignment(Qt.AlignRight)
        ledit1.setFont(QFont('Arial', 20))

        ledit2 = QLineEdit()
        ledit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        ledit3 = QLineEdit()
        ledit3.setEchoMode(QLineEdit.Password)
        ledit3.setAlignment(Qt.AlignCenter)
        ledit3.editingFinished.connect(self.enterPress)

        ledit4 = QLineEdit()
        ledit4.setInputMask('00:00:00;#')
        ledit4.textChanged.connect(self.textChange)

        ledit5 =QLineEdit()
        ledit5.setText('无法修改我')
        ledit5.setReadOnly(True)




        formLayout = QFormLayout()
        formLayout.addRow('1', ledit1)
        formLayout.addRow('2', ledit2)
        formLayout.addRow('3', ledit3)
        formLayout.addRow('4', ledit4)
        formLayout.addRow('5', ledit5)


        self.setLayout(formLayout)

    def textChange(self, text):
        print('输入的内容为' + text)

    def enterPress(self):
        print('已输入内容')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QlineEditDemo()
    mainWin.show()
    sys.exit(app.exec_())
