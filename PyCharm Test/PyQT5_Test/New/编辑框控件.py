import sys

from PyQt5.QtWidgets import *


class TestEditDemo(QWidget):
    def __init__(self):
        super(TestEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('编辑框控件')
        self.tEdit1 = QTextEdit()
        self.btn_get = QPushButton('获取内容')
        self.btn_change = QPushButton('HTML格式化')
        self.btn_get.clicked.connect(self.get_text)
        self.btn_change.clicked.connect(self.format_html)
        formLayout = QGridLayout()
        formLayout.addWidget(self.tEdit1, 0, 0, 1, 2)
        formLayout.addWidget(self.btn_get, 1, 0)
        formLayout.addWidget(self.btn_change, 1, 1)
        self.setLayout(formLayout)

    def get_text(self):
        self.msg = self.tEdit1.toPlainText()
        print(self.msg)

    def format_html(self):
        self.tEdit1.setHtml(self.msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TestEditDemo()
    mainWin.show()
    sys.exit(app.exec_())
