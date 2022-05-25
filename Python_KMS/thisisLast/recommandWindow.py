import sys
import pymysql

# UI Import Start
from recommand import Ui_Dialog
# UI Import End

from myClosetWindow import MyClosetWindow
from recommnadCalc import *

from SaveID import *

from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 윈도우별 class
class recommandWindow(QDialog, QWidget, Ui_Dialog): 
    
    def __init__(self):
        super(recommandWindow, self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        temp = int(temps)
        self.lcdTemp.display(temp)
    
    def recommand(self):
        RecommandupClothe = RecommnadUpClothe()
        RecommandDownClothe = RecommnadDownClothe()
        RecommandOutClothe = RecommnadOutClothe()
        self.RecommnadClotheKind(upClotheKind=RecommandupClothe, downClotheKind=RecommandDownClothe, outClotheKind=RecommandOutClothe)       

    def CS_myCloset(self):
        self.close()
        self.myCloset = MyClosetWindow()
        self.myCloset.exec()
        self.show()

    def CS_logOut(self):
        self.close()        

    def RecommnadClotheKind(self, upClotheKind, downClotheKind, outClotheKind):
        _nullClotheInfo = "정보 없음"
        _clotheUp, _clotheDown = "상의", "하의"
        _clotheOut = "겉옷"
        _clotheShort, _clotheLong = "반팔","긴팔"

        inputID = printID()

        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='dlshfl^^7850', db='dresscode', charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from "+ inputID + "ClosetTable")

        self.tableWidget_up.clearContents()

       
        u = 0
        d = 0
        o = 0
        while(True):
            row = cur.fetchone()
            if row == None:
                break

             # 상의
            if upClotheKind == 0 and row[1] == _clotheUp and row[3] == _clotheShort:
                if u < 20:
                    for j in range(4):
                        self.tableWidget_up.setItem(u, j, QTableWidgetItem(str(row[j])))
                u +=1
            elif upClotheKind == 1 and row[1] == _clotheUp and row[3] == _clotheLong:
                if u < 20:
                    for j in range(4):
                        self.tableWidget_up.setItem(u, j, QTableWidgetItem(str(row[j])))
                u +=1
            elif upClotheKind == 3 and row[1] == _clotheUp:
                if row[3] == _clotheShort or row[3] == _clotheLong:
                    if u < 20:
                        for j in range(4):
                            self.tableWidget_up.setItem(u, j, QTableWidgetItem(str(row[j])))
                    u +=1
            else:
                print("Error")

            # 하의
            if downClotheKind == 0 and row[1] == _clotheDown and row[3] == _clotheShort:
                if d < 20:
                    for j in range(4):
                        self.tableWidget_down.setItem(d, j, QTableWidgetItem(str(row[j])))
                d +=1
            elif downClotheKind == 1 and row[1] == _clotheDown and row[3] == _clotheLong:
                if d < 20:
                    for j in range(4):
                        self.tableWidget_down.setItem(d, j, QTableWidgetItem(str(row[j])))
                d +=1
            elif downClotheKind == 3 and row[1] == _clotheDown:
                if row[3] == _clotheShort or row[3] == _clotheLong:
                    if d < 20:
                        for j in range(4):
                            self.tableWidget_down.setItem(d, j, QTableWidgetItem(str(row[j])))
                    d +=1
            else:
                print("Error")
            
            # 겉옷
            if outClotheKind == 0 and row[1] == _clotheOut:
                if o < 20:
                    for j in range(4):
                        self.tableWidget_out.setItem(o, j, QTableWidgetItem(str(row[j])))
                o +=1
            elif outClotheKind == 1 and row[1] == _clotheOut:
                self.tableWidget_out.setItem(0, 0, QTableWidgetItem("겉옷 필요없음"))
            else:
                print("Error")