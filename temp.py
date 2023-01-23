import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPixmap
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from displayapp import mydisplay



class logapp(QtWidgets.QWidget):
    def __init__(self):
        super(logapp, self).__init__()
        loadUi("trylog.ui",self)
        self.pushButton.clicked.connect(self.loginfunc)
    def openwindow(self):
        wel = WelcomeScreen()
        widget.addWidget(wel)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def loginfunc(self):
        username=self.username_2.text()
        password=self.password.text()
        if len(username)==0 or len(password)==0:
            self.error.setText("Please enter your credentials")
        else:
            conn =sqlite3.connect("minidatabase.db")
            cur = conn.cursor()
            query ='select password from admin where username=\"'+username+'\"'
            cur.execute(query)
            result =cur.fetchone()[0]
            if result == password:
                self.openwindow()
            
            else:
                print("try again")
class WelcomeScreen(QtWidgets.QWidget):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("bg1.ui",self)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1000)
        self.pushButton.clicked.connect(self.openwindowadd)
        self.pushButton_2.clicked.connect(self.openwindowdisplay)
        self.pushButton_4.clicked.connect(self.openwindowana)
        self.pushButton_3.clicked.connect(self.openwindowup)
    def openwindowup(self):
        up = update()
        widget.addWidget(up)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def openwindowadd(self):
        add = myadd()
        widget.addWidget(add)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def openwindowdisplay(self):
        display = displayScreen()
        widget.addWidget(display)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def openwindowana(self):
        ana = myana()
        widget.addWidget(ana)
        widget.setCurrentIndex(widget.currentIndex()+1)
class myadd(QtWidgets.QWidget):
    def __init__(self):
        super(myadd, self).__init__()
        loadUi("add2.ui",self)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1000)
        self.incomebtn.clicked.connect(self.addfunc)
        self.prodbtn.clicked.connect(self.prodfunc)
        self.rawbtn.clicked.connect(self.rawfunc)
        self.salbtn.clicked.connect(self.salfunc)
        self.pushButton.clicked.connect(self.openwindowmain)
    def openwindowmain(self):
        wel = WelcomeScreen()
        widget.addWidget(wel)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def addfunc(self):
        inname=self.income.text()
        inmnth=self.month.text()
        inyear=self.year.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()

        info=[inname,inmnth,inyear]
      
        cur.execute('INSERT INTO `income` (income,month,year) VALUES(?, ?, ?)',info)

        conn.commit()
        conn.close()
    def prodfunc(self):
        print("hii")
        prodname=self.prodname.text()
        prodquan=self.prodquan.text()
        prodprice=self.prodprice.text()
        prodyear=self.yearproduct.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()

        info1=[prodname,prodquan,prodprice,prodyear]
      
        cur.execute('INSERT INTO `product` (product_name,product_qty,product_price,prod_year) VALUES(?, ?, ?, ?)',info1)

        conn.commit()
        conn.close()
    def rawfunc(self):
        matname=self.rawname.text()
        matcost=self.rawprice.text()
        matyear=self.rawyear.text()
        matqty=self.rawquan.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()

        info=[matname,matcost,matyear,matqty]
      
        cur.execute('INSERT INTO `rawmaterials` (materialname,cost,material_year,qty) VALUES(?, ?, ?, ?)',info)

        conn.commit()
        conn.close()
    def salfunc(self):
        empname=self.empname.text()
        empphno=self.phno.text()
        empsal=self.empsal.text()
        empsalyr=self.empyear.text()
        i=self.year.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()

        info=[empname,empphno,empsal,empsalyr]
      
        cur.execute('INSERT INTO `salary` (employeename,phoneno,salary,salary_year) VALUES(?, ?, ?, ?)',info)

        conn.commit()
        conn.close()   

class displayScreen(QtWidgets.QWidget):
    def __init__(self):
        super(displayScreen, self).__init__()
        loadUi("display2.ui",self)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1000)
        self.incomebtn.clicked.connect(self.incomefunc)
        self.prodbtn.clicked.connect(self.prodfunc)
        
        self.rawbtn.clicked.connect(self.rawfunc)
        self.salbtn.clicked.connect(self.salfunc)
        self.pushButton.clicked.connect(self.openwindowmain)
    def openwindowmain(self):
        wel = WelcomeScreen()
        widget.addWidget(wel)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
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
        self.tableWidget.setHorizontalHeaderLabels(['Rid','Name','Quantity','Price','Year'])
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
class myana(QtWidgets.QWidget):
    def __init__(self):
        super(myana, self).__init__()
        loadUi("ana.ui",self)
        widget.setFixedHeight(700)
        widget.setFixedWidth(1000)
        self.ingraphbtn.clicked.connect(self.graphin)
        self.rawgraphbtn.clicked.connect(self.graphraw)
        self.prodgraphbtn.clicked.connect(self.graphprod)
        self.salgraphbtn.clicked.connect(self.graphsal)
        self.backbtn.clicked.connect(self.openwindowmain)
    def openwindowmain(self):
        wel = WelcomeScreen()
        widget.addWidget(wel)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def graphin(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(income),year from 'income' where year='2020'")
        cursor1.execute("select sum(income),year from 'income' where year='2021'")
        result = cursor.fetchall
        result1 = cursor1.fetchall
  
        income = []
        year = []
  
        for i in cursor:
            income.append(i[0])
            year.append(i[1])
        for i in cursor1:
            income.append(i[0])
            year.append(i[1])

        print("income=", income)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,income, color ='green',width = .5)

        plt.xlabel("year")
        plt.ylabel("income")
        plt.title("income graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(10000,2000000)
        plt.show()
    def graphraw(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(cost*qty),material_year from 'rawmaterials' where material_year='2020'")
        cursor1.execute("select sum(cost*qty),material_year from 'rawmaterials' where material_year='2021'")
        result = cursor.fetchall
        result1 = cursor1.fetchall
        rawdetails = []
        year = []
  
        for i in cursor:
            rawdetails.append(i[0])
            year.append(i[1])
        for i in cursor1:
            rawdetails.append(i[0])
            year.append(i[1])

        print("Raw Material details=", rawdetails)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,rawdetails, color ='blue',width = 0.5)

        plt.xlabel("year")
        plt.ylabel("product details")
        plt.title("graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(500,50000)
        plt.show()
    def graphprod(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(product_price*product_qty),prod_year from 'product' where prod_year='2020'")
        cursor1.execute("select sum(product_price*product_qty),prod_year from 'product' where prod_year='2021'")
        
        result = cursor.fetchall
        result1 = cursor1.fetchall
        details = []
        year = []
  
        for i in cursor:
            details.append(i[0])
            year.append(i[1])
        for i in cursor1:
            details.append(i[0])
            year.append(i[1])

        print("Details=", details)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,details, color ='black',width = 0.5)

        plt.xlabel("year")
        plt.ylabel(" details")
        plt.title("graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(10000,1000000)
        plt.show()
    def graphsal(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(salary),salary_year from 'salary' where salary_year='2020'")
        cursor1.execute("select sum(salary),salary_year from 'salary' where salary_year='2021'")
        result = cursor.fetchall
        result1 = cursor1.fetchall
        saldetails = []
        year = []
  
        for i in cursor:
            saldetails.append(i[0])
            year.append(i[1])
        for i in cursor1:
            saldetails.append(i[0])
            year.append(i[1])

        print("Salary details=", saldetails)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,saldetails, color ='maroon',width = 0.5)

        plt.xlabel("year")
        plt.ylabel("salary details")
        plt.title("graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(3000,50000)
        plt.show()
class update(QtWidgets.QWidget):
    def __init__(self):
        super(update, self).__init__()
        loadUi("update.ui",self)
        widget.setFixedWidth(900)
        widget.setFixedHeight(700)
        self.prodsub.clicked.connect(self.prodfunc)
        self.rawsub.clicked.connect(self.rawfunc)
        self.empsub.clicked.connect(self.salfunc)
        self.insub.clicked.connect(self.infunc)
        self.back.clicked.connect(self.openwindowmain)
    def openwindowmain(self):
        wel = WelcomeScreen()
        widget.addWidget(wel)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def infunc(self):
        print("hii")
        
        
        self.tables.clear()
        inid=self.insearch.text()
        conn =sqlite3.connect("minidatabase.db")
        cur = conn.cursor()
        
        cur.execute(f"SELECT * FROM income WHERE inid={inid}")
        results=cur.fetchall()
        
        self.tables.setRowCount(3)
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
        
        self.tables.setRowCount(3)
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


app = QApplication(sys.argv)
welcome = logapp()

widget = QtWidgets.QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(420)
widget.setFixedWidth(500)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")