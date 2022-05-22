import sys
import pymysql

# UI Import Start
from login import Ui_Login
# UI Import End

from recommandWindow import recommandWindow
from CreateAccountWindow import CreateAccountWindow

from SaveID import *

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Login(QMainWindow, Ui_Login): 
    
    # Initialize
    def __init__(self):
        super(Login, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
    
    # Button
    def Login(self):
        inputID, inputPW = "",""

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dresscode', charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from usertable")

        inputID = self.lineEdit_ID.text()
        inputPW = self.lineEdit_PW.text()

        changeInputID(inputID)
        
        while(True):
            row = cur.fetchone()
            if row == None:
                break
            self.textEdit_State.clear()
            if inputID == row[0] and inputPW == row[1]:
                self.close()
                self.recommand = recommandWindow()
                break
            else:
                self.textEdit_State.append("login fail")
        
    def CS_CreateAccount(self):
        self.close()
        self.recommand = CreateAccountWindow()
        self.recommand.exec()
        self.show()
        
app = QApplication([])
sn = Login()
QApplication.processEvents()
sys.exit(app.exec_())
