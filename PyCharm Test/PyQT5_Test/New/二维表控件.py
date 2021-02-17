import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('二维表控件演示')
        # self.resize(200, 100)
        layout = QVBoxLayout()
        self.tvmodel = QStandardItemModel(4, 4)
        self.tvmodel.setHorizontalHeaderLabels(['ID', '姓名', '年龄', '所属门店'])

        self.tv = QTableView()
        self.tv.setModel(self.tvmodel)

        item10 = QStandardItem('10')
        item11 = QStandardItem('邹小路')
        item12 = QStandardItem('30')
        item13 = QStandardItem('皇冠店')

        self.tvmodel.setItem(0, 0, item10)
        self.tvmodel.setItem(0, 1, item11)
        self.tvmodel.setItem(0, 2, item12)
        self.tvmodel.setItem(0, 3, item13)
        #禁止编辑
        self.tv.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行显示
        self.tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        layout.addWidget(self.tv)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = TableViewDemo()
    mainWin.show()
    sys.exit(app.exec_())

