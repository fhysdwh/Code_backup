from PyQt5.QtWidgets import *
import sys


class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入框控件')
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', normalLineEdit)
        formLayout.addRow('noEcho', noEchoLineEdit)
        formLayout.addRow('password', passwordLineEdit)
        formLayout.addRow('passwordechoonedit', passwordEchoOnEditLineEdit)

        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('noecho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LineEditDemo()
    main.show()
    sys.exit(app.exec_())
