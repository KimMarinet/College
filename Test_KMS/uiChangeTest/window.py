import sys
from main import Ui_MainWindow #수정부분
from second import U_Dialog
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class kinwriter(QMainWindow, Ui_MainWindow): 
    
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()

    def btn_to_second(self):
        self.hide()
        self.second = secondwindow()
        self.second.exec()
        self.show()
    
    

class secondwindow(QDialog, U_Dialog):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.initUi()
        self.show()
    
    def initUi(self):
        self.setupUi(self)
    
    def btn_to_main(self):
        self.close()

app = QApplication([])
sn = kinwriter()
QApplication.processEvents()
sys.exit(app.exec_())
