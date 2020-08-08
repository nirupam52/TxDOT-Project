import sys
sys.path.insert(1,'../')
import os
from PyQt5 import QtWidgets, uic
from designer_files.mainWindow import Ui_MainWindow
from Database.dbOps import query


class MainWindow(QtWidgets.QMainWindow, QtWidgets.QStackedWidget, QtWidgets.QFileDialog, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("TxDOT ISPE Tool")
        
        
        #stacked Widget on main window stuff 
        self.stackedWidget.setCurrentWidget(self.ispe_page)
        self.OP1.clicked.connect(self.showIspePage)
        self.OP2.clicked.connect(self.showViewDbPage)
        self.OP3.clicked.connect(self.showDbopPage)
        self.OP4.clicked.connect(self.showAnalyticsPage)

        self.upload_btn.clicked.connect(self.uploadFile)

#functions for navbar buttons 
    def showIspePage(self):
        self.stackedWidget.setCurrentWidget(self.ispe_page)
    def showViewDbPage(self):
        self.stackedWidget.setCurrentWidget(self.viewDb_page)
        query()
    def showAnalyticsPage(self):
        self.stackedWidget.setCurrentWidget(self.analytics_page)

    #this method inclues upload fucntion from dbOPs and the file selection funnctionality
    def uploadFile(self):
        #option = QtWidgets.QFileDialog.options()
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Select a file","default","Spreadsheet(*.csv)") # make this only csv
        print(file)

    

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.showMaximized()

app.exec_()
