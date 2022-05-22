# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myCloset.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(735, 489)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 160, 161, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_UpdateClothe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_UpdateClothe.setObjectName("btn_UpdateClothe")
        self.verticalLayout.addWidget(self.btn_UpdateClothe)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 380, 671, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(20)
        # table Header
        column_headers = ['의상 이름', '상하의', '재질', '색상', '소매길이']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(540, 80, 160, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_Short = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.btn_Short.setObjectName("btn_Short")
        self.verticalLayout_3.addWidget(self.btn_Short)
        self.btn_Long = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.btn_Long.setObjectName("btn_Long")
        self.verticalLayout_3.addWidget(self.btn_Long)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 59, 56, 12))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 59, 56, 12))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(590, 59, 56, 12))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(360, 80, 160, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_Red = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.btn_Red.setObjectName("btn_Red")
        self.verticalLayout_5.addWidget(self.btn_Red)
        self.btn_Blue = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.btn_Blue.setObjectName("btn_Blue")
        self.verticalLayout_5.addWidget(self.btn_Blue)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(180, 80, 160, 201))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_Wool = QtWidgets.QRadioButton(self.verticalLayoutWidget_6)
        self.btn_Wool.setObjectName("btn_Wool")
        self.verticalLayout_6.addWidget(self.btn_Wool)
        self.btn_Cotton = QtWidgets.QRadioButton(self.verticalLayoutWidget_6)
        self.btn_Cotton.setObjectName("btn_Cotton")
        self.verticalLayout_6.addWidget(self.btn_Cotton)
        self.lineEdit_Name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Name.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 56, 12))
        self.label_6.setObjectName("label_6")
        self.textEdit_state = QtWidgets.QTextEdit(Dialog)
        self.textEdit_state.setGeometry(QtCore.QRect(540, 200, 161, 81))
        self.textEdit_state.setObjectName("textEdit_state")
        self.btn_Back = QtWidgets.QPushButton(Dialog)
        self.btn_Back.setGeometry(QtCore.QRect(590, 10, 109, 23))
        self.btn_Back.setObjectName("btn_Back")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 340, 671, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_SearchName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_SearchName.setObjectName("lineEdit_SearchName")
        self.horizontalLayout.addWidget(self.lineEdit_SearchName)
        self.lineEdit_SearchUpDown = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_SearchUpDown.setObjectName("lineEdit_SearchUpDown")
        self.horizontalLayout.addWidget(self.lineEdit_SearchUpDown)
        self.lineEdit_SearchMaterial = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_SearchMaterial.setObjectName("lineEdit_SearchMaterial")
        self.horizontalLayout.addWidget(self.lineEdit_SearchMaterial)
        self.lineEdit_SearchColor = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_SearchColor.setObjectName("lineEdit_SearchColor")
        self.horizontalLayout.addWidget(self.lineEdit_SearchColor)
        self.lineEdit_SearchSleeve = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_SearchSleeve.setObjectName("lineEdit_SearchSleeve")
        self.horizontalLayout.addWidget(self.lineEdit_SearchSleeve)
        self.btn_Search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_Search.setObjectName("btn_Search")
        self.horizontalLayout.addWidget(self.btn_Search)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 330, 56, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(270, 330, 56, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(380, 330, 56, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(500, 330, 56, 12))
        self.label_10.setObjectName("label_10")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 110, 131, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_Up = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.btn_Up.setObjectName("btn_Up")
        self.verticalLayout_2.addWidget(self.btn_Up)
        self.btn_Down = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.btn_Down.setObjectName("btn_Down")
        self.verticalLayout_2.addWidget(self.btn_Down)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(150, 330, 56, 12))
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        self.btn_UpdateClothe.clicked.connect(Dialog.UpdateClothe) # type: ignore
        self.btn_Search.clicked.connect(Dialog.SearchClothe) # type: ignore
        self.btn_Back.clicked.connect(Dialog.Back) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MyCloset"))
        self.btn_UpdateClothe.setText(_translate("Dialog", "Update Clothe"))
        self.label.setText(_translate("Dialog", "My Closet"))
        self.btn_Short.setText(_translate("Dialog", "반팔"))
        self.btn_Long.setText(_translate("Dialog", "긴팔"))
        self.label_3.setText(_translate("Dialog", "Color"))
        self.label_2.setText(_translate("Dialog", "Material"))
        self.label_4.setText(_translate("Dialog", "Sleeve"))
        self.label_5.setText(_translate("Dialog", "Update Clothe"))
        self.btn_Red.setText(_translate("Dialog", "빨강"))
        self.btn_Blue.setText(_translate("Dialog", "파랑"))
        self.btn_Wool.setText(_translate("Dialog", "울"))
        self.btn_Cotton.setText(_translate("Dialog", "면"))
        self.label_6.setText(_translate("Dialog", "Name"))
        self.btn_Back.setText(_translate("Dialog", "Back"))
        self.btn_Search.setText(_translate("Dialog", "Search Clothe"))
        self.label_7.setText(_translate("Dialog", "Name"))
        self.label_8.setText(_translate("Dialog", "Material"))
        self.label_9.setText(_translate("Dialog", "Color"))
        self.label_10.setText(_translate("Dialog", "Sleeve"))
        self.btn_Up.setText(_translate("Dialog", "상의"))
        self.btn_Down.setText(_translate("Dialog", "하의"))
        self.label_11.setText(_translate("Dialog", "UpDown"))
