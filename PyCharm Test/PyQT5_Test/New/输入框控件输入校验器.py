import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regLineEdit = QLineEdit()

        formLayout.addRow('ID',intLineEdit)
        formLayout.addRow('成绩',doubleLineEdit)
        formLayout.addRow('用户名',regLineEdit)

        intLineEdit.setPlaceholderText('只可以输入整数')
        doubleLineEdit.setPlaceholderText('只可以输入小数')
        regLineEdit.setPlaceholderText('只可以输入字母+数字')

        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(0, 100)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+$')
        regValidator = QRegExpValidator(self)
        regValidator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regLineEdit.setValidator(regValidator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QLineEditValidator()
    mainWin.show()
    sys.exit(app.exec_())
