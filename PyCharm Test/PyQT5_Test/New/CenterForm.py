import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('股东管理系统')
        # 设置窗口的尺寸
        self.resize(1500, 1000)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

        newLeft = (screen.width() - size.width()) / 2
        newRight = (screen.height() - size.height()) / 2

        self.move(newLeft,newRight)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../images/test1.ico'))

    main = CenterForm()

    main.show()

    sys.exit(app.exec_())
