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
        
        brand = self.GetBrand()
        tpye = self.GetType()
        color = self.GetColor()
        sleeves = self.Getsleeves()

        sql = ""

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dressCode', charset='utf8')
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS " + inputID + "ClosetTable (brand char(50), type char(20), color char(50), sleeves char(50))"
        cur.execute(sql)

        sql = "INSERT INTO "+ inputID +"ClosetTable VALUES('"+ brand + "','" + tpye + "','" + color + "','" + sleeves + "')"
        cur.execute(sql)

        conn.commit()
        conn.close()

        self.textEdit_state.append("등록완료")

    def SearchClothe(self):
        inputID = printID()

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dresscode', charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from "+ inputID + "ClosetTable")

        brand = self.lineEdit_SearchName.text()
        type = self.lineEdit_SearchUpDown.text()
        color = self.lineEdit_SearchColor.text()
        sleeves = self.lineEdit_SearchSleeve.text()
        
        self.tableWidget.clearContents()

        i = 0
        while(True):
            row = cur.fetchone()
            if row == None:
                break
            if brand == row[0] or type == row[1] or color == row[2] or sleeves == row[3]:
                if(i < 20):
                    for j in range(4):
                        self.tableWidget.setItem(i,j,QTableWidgetItem(str(row[j])))
                    i += 1

    def Back(self):
        self.close()

    def GetBrand(self):
        brand =""
        if(self.btn_nike.isChecked()):
            brand = self.btn_nike.text()
        elif(self.btn_adidas.isChecked()):
            brand = self.btn_adidas.text()
        else:
            brand = "정보 없음"
        
        return brand

    def GetType(self):
        type =""
        if(self.btn_Up.isChecked()):
            type = self.btn_Up.text()
        elif(self.btn_Down.isChecked()):
            type = self.btn_Down.text()
        elif(self.btn_Out.isChecked()):
            type = self.btn_Out.text()
        else:
            type = "정보 없음"
        
        return type
    
    def GetColor(self):
        color = ""
        if(self.btn_Red.isChecked()):
            color = self.btn_Red.text()
        elif(self.btn_orange.isChecked()):
            color = self.btn_orange.text()
        elif(self.btn_yellow.isChecked()):
            color = self.btn_yellow.text()
        elif(self.btn_green.isChecked()):
            color = self.btn_green.text()
        elif(self.btn_Blue.isChecked()):
            color = self.btn_Blue.text()
        elif(self.btn_indigo.isChecked()):
            color = self.btn_indigo.text()
        elif(self.btn_pupple.isChecked()):
            color = self.btn_pupple.text()
        else:
            color = "정보 없음"
        
        return color

    def Getsleeves(self):
        sleeves = ""
        if(self.btn_Short.isChecked()):
            sleeves = self.btn_Short.text()
        elif(self.btn_Long.isChecked()):
            sleeves = self.btn_Long.text()
        else:
            sleeves = "정보 없음"
        
        return sleeves