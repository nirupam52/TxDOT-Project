#this file wil have helper functions for the "Database page" in the app
from PyQt5 import QtWidgets, uic, QtSql, QtCore, Qt
from designer_files.mainWindow import Ui_MainWindow
from Database.dbOps import query,connect,upload_file,table_names


connection = connect()
table = ""
offset = 0
        
class ViewDB(QtWidgets.QFileDialog, QtWidgets.QTableWidget, QtWidgets.QMessageBox, QtWidgets.QInputDialog, QtWidgets.QListWidget):
     #this method inclues upload fucntion from dbOPs and the file selection funnctionality
    
    def uploadFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self,"Select a file","default","Spreadsheet(*.csv)") # make this only csv
        
        if file == ('',''):
            print(file)
            return
        else:
           #file dialog to ask user for table name for the upladed csv
            test = QtWidgets.QInputDialog(self)
            test.resize(400,400)
            tname,ok = test.getText(self,"Input Table Name", "Enter Name of the table")
            
            if ok and tname not in (None,''):
                upload_file(file[0],connection,tname)
            
    
    #function to fetch and set the data in the tableWidget
    def fetch_records(self,value):

        if value == int((self.tableWidget.verticalScrollBar().maximum())*0.6):
            print("max reached")
            global offset
            offset += 30
            cname, res = query("main_database",table,connection,offset_val=offset)
            currPos = self.tableWidget.rowCount()
            for rownum, rowdat in enumerate(res):
                self.tableWidget.insertRow(currPos+rownum-30)
                for colnum, coldat in enumerate(rowdat):
                    self.tableWidget.setItem(currPos+rownum-30,colnum,QtWidgets.QTableWidgetItem(str(coldat)))
        else:
            pass
    
    #function to load a different table into tableWidget
    def change_table(self):
        global offset
        offset = 0
        listview = QtWidgets.QListWidget(self)
        listview.setWindowFlags(QtCore.Qt.Window)
        names = table_names("main_database",connection)
        listview.addItems(names)
        listview.show()
        listview.itemDoubleClicked.connect(self.listview_helper)

     #helper function for change_table
    def listview_helper(self,item):
        tableName = item.text()
        self.showTable(tabName=tableName)
       
    # main function to populate table on viewDb page
    def showTable(self,tabName):
        global table
        table = tabName
        cname, res = query("main_database",tabName,connection)
        self.table = tabName
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(cname))
        self.tableWidget.setHorizontalHeaderLabels(cname)
        
        for rownum, rowdat in enumerate(res):
            self.tableWidget.insertRow(rownum)
            for colnum, coldat in enumerate(rowdat):
                self.tableWidget.setItem(rownum,colnum,QtWidgets.QTableWidgetItem(str(coldat)))        
