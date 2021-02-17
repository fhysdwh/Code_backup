import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 400, 1000, 1000)
        self.setWindowTitle('窗口标题')
        self.setWindowIcon(QIcon('../images/test1.ico'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/test1.ico'))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())
