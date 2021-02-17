import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('股东管理系统')
        # 设置窗口的尺寸
        self.resize(1500, 1000)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../images/test1.ico'))

    main = FirstMainWin()

    main.show()

    sys.exit(app.exec_())
