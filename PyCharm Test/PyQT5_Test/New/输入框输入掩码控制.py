from PyQt5.QtWidgets import *
import sys

class QlineEditMast(QWidget):
    def __init__(self):
        super(QlineEditMast, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('通过掩码控制输入')

        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dataLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dataLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('MAC地址',macLineEdit)
        formLayout.addRow('日期',dataLineEdit)
        formLayout.addRow('序列号',licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QlineEditMast()
    mainWin.show()
    sys.exit(app.exec_())
