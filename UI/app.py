import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("TxDOT ISPE Tool")
        self.setFixedSize(600,600)
    #the 4 buttons 
        buttonLayout = QHBoxLayout()
        btn1 = QPushButton("OP1")
        btn2 = QPushButton("OP2")
        btn3 = QPushButton("OP3")
        btn4 = QPushButton("OP4")
        buttonLayout.addWidget(btn1)
        buttonLayout.addWidget(btn2)
        buttonLayout.addWidget(btn3)
        buttonLayout.addWidget(btn4)
        buttonWidget = QWidget()
        buttonWidget.setLayout(buttonLayout)
        
    #button layout and image on top
        mainLayout = QGridLayout()
        logo = QLabel()
        imgPath = os.path.abspath(os.getcwd())
        pixmap = QPixmap(imgPath + '/assets/txdot_logo.jpg')
        logo.setPixmap(pixmap)
        mainLayout.addWidget(logo,0,0)
        mainLayout.addWidget(buttonWidget,1,1)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)


        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
