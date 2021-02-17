import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(800, 500)
    window.move(1000, 500)
    window.setWindowTitle('股东管理系统')
    window.show()

    sys.exit(app.exec_())
