#this file wil have helper functions for the "Database page" in the app
from PyQt5 import QtWidgets, uic, QtSql
from designer_files.mainWindow import Ui_MainWindow
from Database.dbOps import query,connect,upload_file

class ViewDB(QtWidgets.QFileDialog, QtWidgets.QTableWidget):
     #this method inclues upload fucntion from dbOPs and the file selection funnctionality
    def uploadFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Select a file","default","Spreadsheet(*.csv)") # make this only csv
        if file not in (None,''):
            return
        else:
            upload_file(file[0],connection,"test")
    
    #function to fetch and set the data in the tableWidget
    def fetch_records(self,value):
        if value == self.tableWidget.verticalScrollBar().maximum():
            print("max reached")
            #query()
        else:
            print("max not yet reached")