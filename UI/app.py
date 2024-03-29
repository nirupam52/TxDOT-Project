import sys
sys.path.insert(1,'../')
import os
from PyQt5 import QtWidgets, uic
from designer_files.mainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, QtWidgets.QStackedWidget, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("TxDOT ISPE Tool")
        self.setFixedSize(900,900)
        
        #stacked Widget on main window stuff 
        self.stackedWidget.setCurrentWidget(self.ispe_page)
        self.OP1.clicked.connect(self.showIspePage)
        self.OP2.clicked.connect(self.showViewDbPage)
        self.OP3.clicked.connect(self.showDbopPage)
        self.OP4.clicked.connect(self.showAnalyticsPage)

#functions for navbar buttons 
    def showIspePage(self):
        self.stackedWidget.setCurrentWidget(self.ispe_page)
    def showViewDbPage(self):
        self.stackedWidget.setCurrentWidget(self.viewDb_page)
    def showDbopPage(self):
        self.stackedWidget.setCurrentWidget(self.dbOP_page)
    def showAnalyticsPage(self):
        self.stackedWidget.setCurrentWidget(self.analytics_page)
    
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.show()

app.exec_()
