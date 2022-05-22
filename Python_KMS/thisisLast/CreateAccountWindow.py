import sys
import pymysql

# UI Import Start
from CreateAccount import Ui_Dialog
# UI Import End

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class CreateAccountWindow(QDialog, QWidget, Ui_Dialog): 
    
    def __init__(self):
        super(CreateAccountWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
    
    def cancel(self):
        self.close()

    def createAccount(self):
        isAlreayAccount = False
        conn, cur = None, None
        inputNewID, inputNewPW, userName, inputNewPNumber = "","","",""
        sql = ""

        # 라벨 초기화
        self.textEdit_State.clear()
        
        # mySQL -> DB -> Table
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dressCode', charset='utf8')
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS usertable (id char(10), pw char(20), name char(20), PN int)"
        cur.execute(sql)

        # 라벨 입력 변수로 받기
        inputNewID = self.lineEdit_ID.text()
        inputNewPW = self.lineEdit_PW.text()
        userName = self.lineEdit_Name.text()
        inputNewPNumber = self.lineEdit_Phone.text()

        cur.execute("select * from usertable")
        # 같은 계정의 유뮤 확인
        while(True):
            row = cur.fetchone()
            if row == None:
                break
            self.textEdit_State.clear()
            if inputNewID == row[0] :
                self.textEdit_State.append("Create Fail")
                self.textEdit_State.append("Account exist...")
                self.textEdit_State.append("Plz Try Another Account")
                isAlreayAccount = True
                break
            else:
                self.textEdit_State.append("Create Successful")

        # 같은 계정이 없을 경우 계정 생성
        if(isAlreayAccount == False):
            sql = "INSERT INTO usertable VALUES('" + inputNewID + "','" + inputNewPW + "','" + userName + "'," + inputNewPNumber + ")"
            cur.execute(sql)

            sql = "CREATE TABLE IF NOT EXISTS " + inputNewID + "ClosetTable (name char(50), updown char(20), material char(50), color char(50), sleeves char(50))"
            cur.execute(sql)

            conn.commit()
            conn.close()      