# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(441, 337)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(260, 120, 111, 25))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_NewAccount = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_NewAccount.setObjectName("btn_NewAccount")
        self.verticalLayout_5.addWidget(self.btn_NewAccount)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 200, 311, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_State = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_State.setObjectName("textEdit_State")
        self.verticalLayout_2.addWidget(self.textEdit_State)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(100, 30, 251, 31))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(260, 90, 111, 25))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_Login = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_Login.setObjectName("btn_Login")
        self.verticalLayout_4.addWidget(self.btn_Login)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 90, 131, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.verticalLayout.addWidget(self.lineEdit_ID)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(60, 90, 31, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(60, 140, 31, 31))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(100, 140, 131, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_PW = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_PW.setObjectName("lineEdit_PW")
        self.verticalLayout_3.addWidget(self.lineEdit_PW)
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        self.btn_Login.clicked.connect(Login.Login) # type: ignore
        self.btn_NewAccount.clicked.connect(Login.CS_CreateAccount) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.btn_NewAccount.setText(_translate("Login", "Create Account"))
        self.label.setText(_translate("Login", "????????? ?????? ??????"))
        self.btn_Login.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "I D"))
        self.label_2.setText(_translate("Login", "PW"))
