import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow , QApplication, QWidget
from Ui_helloPyQt5 import Ui_helloPyQt

class 启动_helloPyQt5(QMainWindow,Ui_helloPyQt):
    def __init__(self, parent=None):
        super(启动_helloPyQt5,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    # print(sys.argv)
    myWin=启动_helloPyQt5()
    myWin.show()
    sys.exit(app.exec_())