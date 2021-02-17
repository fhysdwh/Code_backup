import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText('<a href="#"> 欢迎使用Python</a>')

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')

        label3.setPixmap(QPixmap('../images/test1.ico'))
        label4.setOpenExternalLinks(True)
        label4.setText('<a href="https://baidu.com">感谢搜索</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle('标签控件')

    def linkHovered(self):
        print('当鼠标划过lable2')

    def linkClicked(self):
        print('当鼠标单击lable4')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
