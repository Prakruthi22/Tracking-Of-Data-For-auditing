from PyQt5 import QtWidgets
from ana import Ui_Form
import sys
import sqlite3
import numpy as np
import matplotlib.pyplot as plt



class myana(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(myana,self).__init__()
        self.setupUi(self)
        self.ingraphbtn.clicked.connect(self.graphin)
        self.rawgraphbtn.clicked.connect(self.graphraw)
        self.prodgraphbtn.clicked.connect(self.graphprod)
        self.salgraphbtn.clicked.connect(self.graphsal)
        
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
   
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)
    Form = myana()
    Form.show()
    sys.exit(app.exec_())