from PyQt5 import QtWidgets
from bg1 import Ui_Form
import sys
import sqlite3
from addapp import myadd
from anaapp import myana
from displayapp import mydisplay
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class update(QtWidgets.QWidget):
    def __init__(self):
        super(update, self).__init__()
        loadUi("update.ui",self)
        
        self.prodsub.clicked.connect(self.prodfunc)
        self.rawsub.clicked.connect(self.rawfunc)
        self.empsub.clicked.connect(self.salfunc)
        self.insub.clicked.connect(self.infunc)
    def infunc(self):
        print("hii")
        
        
        self.tables.clear()
        inid=self.insearch.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM income WHERE inid={inid}")
        results=cur.fetchall()
        
        self.tables.setRowCount(20)
        self.tables.setHorizontalHeaderLabels(['income','month','year'])
        for row_number,row_data in enumerate (results) :
            self.tables.insertRow(row_number)
            
        for column_number,data in enumerate(row_data):
            self.tables.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
            
        
        
        conn.commit()
        conn.close()
    def prodfunc(self):
        print("hii")
        
        
        self.tables.clear()
        pid=self.prodsearch.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM product WHERE product_id={pid}")
        results=cur.fetchall()
        
        self.tables.setRowCount(2)
        self.tables.setHorizontalHeaderLabels(['Pid','Name','Quantity','Price','Year'])
        for row_number,row_data in enumerate (results) :
            self.tables.insertRow(row_number)
            
        for column_number,data in enumerate(row_data):
            self.tables.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
            
        
        
        conn.commit()
        conn.close()
    def rawfunc(self):
        print("hii")
        
        
        self.tables.clear()
        rid=self.rawsearch.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM rawmaterials WHERE rid={rid}")
        results=cur.fetchall()
        
        self.tables.setRowCount(2)
        self.tables.setHorizontalHeaderLabels(['Rid','Name','Quantity','Year','Price'])
        for row_number,row_data in enumerate (results) :
            self.tables.insertRow(row_number)
            
        for column_number,data in enumerate(row_data):
            self.tables.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    def salfunc(self):
        print("hii")
        
        
        self.tables.clear()
        eid=self.empsearch.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM salary WHERE eid={eid}")
        results=cur.fetchall()
        
        self.tables.setRowCount(2)
        self.tables.setHorizontalHeaderLabels(['Eid','Name','Phone No','Salary','Year'])
        for row_number,row_data in enumerate (results) :
            self.tables.insertRow(row_number)
            
        for column_number,data in enumerate(row_data):
            self.tables.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
            
        
        
        conn.commit()
        conn.close()
    def produpfunc(self):
        print("hii")
        prodname=self.prodname.text()
        prodquan=self.prodquan.text()
        prodprice=self.prodprice.text()
        prodyear=self.yearproduct.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()

        info1=[prodname,prodquan,prodprice,prodyear]
      
        cur.execute(f'update product set  ={info1} where id = ')

        conn.commit()
        conn.close()
    
 
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)
    Form = update()
    Form.show()
    sys.exit(app.exec_())
