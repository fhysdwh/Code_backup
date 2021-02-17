import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QPushButton


class ExitMainWin(QMainWindow):
    def __init__(self):
        super(ExitMainWin, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('股东管理系统')
        # 设置窗口的尺寸
        self.resize(1500, 1000)
        # 添加按钮
        self.button1 = QPushButton('关闭')
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = ExitMainWin()

    main.show()

    sys.exit(app.exec_())
