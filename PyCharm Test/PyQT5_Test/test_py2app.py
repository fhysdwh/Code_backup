import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FontColorFileDemo(QWidget):
    def __init__(self):
        super(FontColorFileDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('字体、颜色、文件对话框演示')
        # self.resize(200, 100)
        layout = QVBoxLayout()
        self.imgtip = QLabel('您的头像：')
        self.imglb = QLabel()

        self.texttip = QLabel('个人简介：')
        self.textEdit = QTextEdit()

        layout2 = QHBoxLayout()
        self.imgbtn = QPushButton('选择头像')
        self.imgbtn.clicked.connect(self.setImg)
        self.textbtn = QPushButton('打开个人简介')
        self.textbtn.clicked.connect(self.setText)
        self.fontbtn = QPushButton('选择简介字体')
        self.fontbtn.clicked.connect(self.setTestFont)
        self.colorbtn = QPushButton('选择简介颜色')
        self.colorbtn.clicked.connect(self.setTestColor)
        layout2.addWidget(self.imgbtn)
        layout2.addWidget(self.textbtn)
        layout2.addWidget(self.fontbtn)
        layout2.addWidget(self.colorbtn)

        layout.addWidget(self.imgtip)
        layout.addWidget(self.imglb)
        layout.addWidget(self.texttip)
        layout.addWidget(self.textEdit)
        layout.addLayout(layout2)

        self.setLayout(layout)

    def setImg(self):
        imgname, ok = QFileDialog.getOpenFileName(self, '选择头像', '.', '图片格式(*.jpg *.png)')
        if imgname and ok:
            self.imglb.setPixmap(QPixmap(imgname))

    def setText(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.AnyFile)
        # fd.setFilter(QDir.filter('文本文件(*.txt *.md)'))
        fd.setFilter(QDir.Files)

        if fd.exec():
            filename = fd.selectedFiles()
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def setTestFont(self):
        f, ok = QFontDialog.getFont()
        self.textEdit.setFont(f)

    def setTestColor(self):
        c = QColorDialog.getColor()
        # p = QPalette()
        # p.setColor(QPalette.WindowText, c)
        self.textEdit.setTextColor(c)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = FontColorFileDemo()
    mainWin.show()
    sys.exit(app.exec_())
