from PyQt5 import QtWidgets
from bg1 import Ui_Form
import sys
import sqlite3
from addapp import myadd
from anaapp import myana
from displayapp import mydisplay
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

class myapp(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myapp,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openwindow)
    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = mydisplay()
        self.ui.setupUi(self.window)
        self.window.show()
    

class mydisplay(QtWidgets.QWidget,Ui_Form):
     
     def __init__(self):
        super(mydisplay,self).__init__()
        self.setupUi(self)
   
        
    
 
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
