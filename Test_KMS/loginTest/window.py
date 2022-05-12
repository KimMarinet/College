from email.mime import base
import sys
from login2 import *
from login2 import Ui_MainWindow #수정부분
from createAccount import Ui_Dialog
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()

    def createNewAccount(self):
        self.hide()
        self.createAccount = secondwindow()
        self.createAccount.exec()
        self.show()     

    def changeWindow(self):
        if isLogin == True:
            self.hide()
            self.createAccount = secondwindow()
            self.createAccount.exec()
            self.show() 

    def changeWindowClothe(self):
        if isLogin == True:
            self.hide()
            self.createAccount = secondwindow()
            self.createAccount.exec()
            self.show() 
    

class secondwindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        self.setupUi(self)
    
    def cancel(self):
        self.close()
        isLogin == False

app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())
