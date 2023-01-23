from PyQt5 import QtWidgets
from display1 import Ui_Form
import sys
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


class mydisplay(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mydisplay,self).__init__()
        self.setupUi(self)
        
        
        
        self.incomebtn.clicked.connect(self.incomefunc)
        self.prodbtn.clicked.connect(self.prodfunc)
        
        self.rawbtn.clicked.connect(self.rawfunc)
        self.salbtn.clicked.connect(self.salfunc)
        
        
    def incomefunc(self):
        self.tableWidget.clear()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        query='SELECT * FROM `income`'
        cur.execute(query)
        result=cur.fetchall()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setHorizontalHeaderLabels(['income','month','year'])
        print("hiii i am wrking")
        for row_number,row_data in enumerate (result) :
            self.tableWidget.insertRow(row_number)
            
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()
        
    def prodfunc(self):
        self.tableWidget.clear()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        query='SELECT * FROM `product`'
        cur.execute(query)
        result=cur.fetchall()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setHorizontalHeaderLabels(['Pid','Name','Quantity','Price','Year'])
        
        for row_number,row_data in enumerate (result) :
            self.tableWidget.insertRow(row_number)
            
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()
    def rawfunc(self):
        self.tableWidget.clear()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        query='SELECT * FROM `rawmaterials`'
        cur.execute(query)
        result=cur.fetchall()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setHorizontalHeaderLabels(['Rid','Name','Quantity','Year','Price'])
        for row_number,row_data in enumerate (result) :
            self.tableWidget.insertRow(row_number)
            
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()
    def salfunc(self):
        self.tableWidget.clear()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        query='SELECT * FROM `salary`'
        cur.execute(query)
        result=cur.fetchall()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setHorizontalHeaderLabels(['Eid','Name','Phone No','Salary','Year'])
        for row_number,row_data in enumerate (result) :
            self.tableWidget.insertRow(row_number)
            
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()
        
 
        
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)

    sys.exit(app.exec_())