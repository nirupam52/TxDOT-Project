import sys
sys.path.insert(1,'../')
import os
from PyQt5 import QtWidgets, uic
from designer_files.mainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("TxDOT ISPE Tool")
        self.setFixedSize(600,600)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
