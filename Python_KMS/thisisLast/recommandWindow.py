import sys
import pymysql

# UI Import Start
from recommand import Ui_Dialog
# UI Import End

from myClosetWindow import MyClosetWindow

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
    
    def recommand(self):
        b=10
        d = printID()
        print(d)

    def CS_myCloset(self):
        self.close()
        self.recommand = MyClosetWindow()
        self.recommand.exec()
        self.show()

    def CS_logOut(self):
        self.close()