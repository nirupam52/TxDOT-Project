# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.navbar = QtWidgets.QFrame(self.centralwidget)
        self.navbar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.navbar.setStyleSheet("background-color: rgb(10, 49, 108);")
        self.navbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar.setObjectName("navbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.navbar)
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_frame = QtWidgets.QFrame(self.navbar)
        self.logo_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logo_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label = QtWidgets.QLabel(self.logo_frame)
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_2.addWidget(self.logo_label)
        self.horizontalLayout.addWidget(self.logo_frame)
        self.title_frame = QtWidgets.QFrame(self.navbar)
        self.title_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title_label = QtWidgets.QLabel(self.title_frame)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";")
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_3.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.title_frame)
        self.line = QtWidgets.QFrame(self.navbar)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.navbar_buttons = QtWidgets.QFrame(self.navbar)
        self.navbar_buttons.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.navbar_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.navbar_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar_buttons.setObjectName("navbar_buttons")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.navbar_buttons)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.OP1 = QtWidgets.QPushButton(self.navbar_buttons)
        self.OP1.setFlat(True)
        self.OP1.setObjectName("OP1")
        self.horizontalLayout_4.addWidget(self.OP1)
        self.OP2 = QtWidgets.QPushButton(self.navbar_buttons)
        self.OP2.setFlat(True)
        self.OP2.setObjectName("OP2")
        self.horizontalLayout_4.addWidget(self.OP2)
        self.OP3 = QtWidgets.QPushButton(self.navbar_buttons)
        self.OP3.setFlat(True)
        self.OP3.setObjectName("OP3")
        self.horizontalLayout_4.addWidget(self.OP3)
        self.OP4 = QtWidgets.QPushButton(self.navbar_buttons)
        self.OP4.setAutoDefault(False)
        self.OP4.setDefault(False)
        self.OP4.setFlat(True)
        self.OP4.setObjectName("OP4")
        self.horizontalLayout_4.addWidget(self.OP4)
        self.horizontalLayout.addWidget(self.navbar_buttons)
        self.verticalLayout.addWidget(self.navbar)
        self.sub_navbar = QtWidgets.QFrame(self.centralwidget)
        self.sub_navbar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sub_navbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11, 56, 124);")
        self.sub_navbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sub_navbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sub_navbar.setObjectName("sub_navbar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.sub_navbar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sub_op_1 = QtWidgets.QPushButton(self.sub_navbar)
        self.sub_op_1.setFlat(True)
        self.sub_op_1.setObjectName("sub_op_1")
        self.horizontalLayout_5.addWidget(self.sub_op_1)
        self.sub_op_2 = QtWidgets.QPushButton(self.sub_navbar)
        self.sub_op_2.setFlat(True)
        self.sub_op_2.setObjectName("sub_op_2")
        self.horizontalLayout_5.addWidget(self.sub_op_2)
        self.sub_op_3 = QtWidgets.QPushButton(self.sub_navbar)
        self.sub_op_3.setFlat(True)
        self.sub_op_3.setObjectName("sub_op_3")
        self.horizontalLayout_5.addWidget(self.sub_op_3)
        self.verticalLayout.addWidget(self.sub_navbar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.ispe_page = QtWidgets.QWidget()
        self.ispe_page.setObjectName("ispe_page")
        self.label = QtWidgets.QLabel(self.ispe_page)
        self.label.setGeometry(QtCore.QRect(330, 230, 231, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.ispe_page)
        self.viewDb_page = QtWidgets.QWidget()
        self.viewDb_page.setObjectName("viewDb_page")
        self.label_2 = QtWidgets.QLabel(self.viewDb_page)
        self.label_2.setGeometry(QtCore.QRect(290, 220, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.viewDb_page)
        self.dbOP_page = QtWidgets.QWidget()
        self.dbOP_page.setObjectName("dbOP_page")
        self.label_3 = QtWidgets.QLabel(self.dbOP_page)
        self.label_3.setGeometry(QtCore.QRect(270, 210, 331, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.dbOP_page)
        self.analytics_page = QtWidgets.QWidget()
        self.analytics_page.setObjectName("analytics_page")
        self.label_4 = QtWidgets.QLabel(self.analytics_page)
        self.label_4.setGeometry(QtCore.QRect(310, 190, 281, 211))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.analytics_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "ISPE TOOL"))
        self.OP1.setText(_translate("MainWindow", "In Service Performance Evaluation"))
        self.OP2.setText(_translate("MainWindow", "View Database"))
        self.OP3.setText(_translate("MainWindow", "Database Operations"))
        self.OP4.setText(_translate("MainWindow", "Analytics"))
        self.sub_op_1.setText(_translate("MainWindow", "OP 1"))
        self.sub_op_2.setText(_translate("MainWindow", "OP 2"))
        self.sub_op_3.setText(_translate("MainWindow", "OP 3"))
        self.label.setText(_translate("MainWindow", "ISPE PAGE "))
        self.label_2.setText(_translate("MainWindow", "DATABSE PAGE"))
        self.label_3.setText(_translate("MainWindow", "DATABASE OPS PAGE"))
        self.label_4.setText(_translate("MainWindow", "ANALYTICS PAGE"))
