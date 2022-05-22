import sys
import pymysql

# UI Import Start
from myCloset import Ui_Dialog
# UI Import End

from SaveID import *

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 윈도우별 class
class MyClosetWindow(QDialog, QWidget, Ui_Dialog): 
    
    def __init__(self):
        super(MyClosetWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)

    def UpdateClothe(self):
        self.textEdit_state.clear()
        conn, cur = None, None

        inputID = printID()
        
        clotheName = self.lineEdit_Name.text()
        updown = self.GetUpDown()
        material = self.GetMaterial()
        color = self.GetColor()
        sleeves = self.Getsleeves()

        sql = ""

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dressCode', charset='utf8')
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS " + inputID + "ClosetTable (name char(50), updown char(20), material char(50), color char(50), sleeves char(50))"
        cur.execute(sql)

        sql = "INSERT INTO "+ inputID +"ClosetTable VALUES('"+ clotheName + "','" + updown + "','" + material + "','" + color + "','" + sleeves + "')"
        cur.execute(sql)

        conn.commit()
        conn.close()

        self.textEdit_state.append("등록완료")

    def SearchClothe(self):
        inputID = printID()

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dresscode', charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from "+ inputID + "ClosetTable")

        ClotheName = self.lineEdit_SearchName.text()
        updown = self.lineEdit_SearchUpDown.text()
        material = self.lineEdit_SearchMaterial.text()
        color = self.lineEdit_SearchColor.text()
        sleeves = self.lineEdit_SearchSleeve.text()
        
        self.tableWidget.clearContents()

        i = 0
        while(True):
            row = cur.fetchone()
            if row == None:
                break
            if ClotheName == row[0] or updown == row[1] or material == row[2] or color == row[3] or sleeves == row[4]:
                if(i <= 20):
                    for j in range(5):
                        self.tableWidget.setItem(i,j,QTableWidgetItem(str(row[j])))
                    i += 1

    def Back(self):
        self.close()

    def GetUpDown(self):
        updown =""
        if(self.btn_Up.isChecked()):
            updown = self.btn_Up.text()
        elif(self.btn_Down.isChecked()):
            updown = self.btn_Down.text()
        else:
            updown = "정보 없음"
        
        return updown

    def GetMaterial(self):
        material = ""
        if(self.btn_Cotton.isChecked()):
            material = self.btn_Cotton.text()
        elif(self.btn_Wool.isChecked()):
            material = self.btn_Wool.text()
        else:
            material = "재질 정보 없음"
        
        return material
    
    def GetColor(self):
        color = ""
        if(self.btn_Red.isChecked()):
            color = self.btn_Red.text()
        elif(self.btn_Blue.isChecked()):
            color = self.btn_Blue.text()
        else:
            color = "색상 정보 없음"
        
        return color

    def Getsleeves(self):
        sleeves = ""
        if(self.btn_Short.isChecked()):
            sleeves = self.btn_Short.text()
        elif(self.btn_Long.isChecked()):
            sleeves = self.btn_Long.text()
        else:
            sleeves = "소매 정보 없음"
        
        return sleeves