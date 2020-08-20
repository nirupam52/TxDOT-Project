import sys
sys.path.insert(1,'../')
import os
from PyQt5 import QtWidgets, uic, QtSql
from designer_files.mainWindow import Ui_MainWindow
from Database.dbOps import query,connect,upload_file
from UI.viewDb import ViewDB


connection = connect()

class MainWindow(QtWidgets.QMainWindow, QtWidgets.QStackedWidget, Ui_MainWindow, ViewDB):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("TxDOT ISPE Tool")
        
        
        #stacked Widget on main window stuff 
        self.stackedWidget.setCurrentWidget(self.ispe_page)
        self.OP1.clicked.connect(self.showIspePage)
        self.OP2.clicked.connect(self.showViewDbPage)
        self.OP4.clicked.connect(self.showAnalyticsPage)

        self.upload_btn.clicked.connect(self.uploadFile)
        self.change_table_btn.clicked.connect(self.change_table)

#functions for navbar buttons 
    def showIspePage(self):
        self.stackedWidget.setCurrentWidget(self.ispe_page)
    def showViewDbPage(self):
        self.stackedWidget.setCurrentWidget(self.viewDb_page)
        self.showTable(tabName="crashes_charges")

        
        
        self.tableWidget.verticalScrollBar().valueChanged.connect(self.fetch_records)
    def showAnalyticsPage(self):
        self.stackedWidget.setCurrentWidget(self.analytics_page)

 
   
        
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = MainWindow()
window.showMaximized()

app.exec_()
