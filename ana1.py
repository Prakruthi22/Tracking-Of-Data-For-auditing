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
       # self.ingraphbtn.clicked.connect(self.graphin)
        self.rawgraphbtn.clicked.connect(self.graphraw)
        self.prodgraphbtn.clicked.connect(self.graphprod)
   


    def graphraw(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(cost*qty),material_year from 'rawmaterials' where material_year='2020'")
        cursor1.execute("select sum(cost*qty),material_year from 'rawmaterials' where material_year='2021'")
        result = cursor.fetchall
        result1 = cursor1.fetchall
        proddetails = []
        year = []
  
        for i in cursor:
            proddetails.append(i[0])
            year.append(i[1])
        for i in cursor1:
            proddetails.append(i[0])
            year.append(i[1])

        print("product details=", proddetails)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,proddetails, color ='maroon',width = 1)

        plt.xlabel("year")
        plt.ylabel("product details")
        plt.title("graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(500,10000)
        plt.show()
    def graphprod(self):
    
        conn = sqlite3.connect('minidatabase.db')
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("select sum(product_price*product_qty),prod_year from 'product' where prod_year='2020'")
        cursor1.execute("select sum(product_price*product_qty),prod_year from 'product' where prod_year='2021'")
        result = cursor.fetchall
        result1 = cursor1.fetchall
        proddetails = []
        year = []
  
        for i in cursor:
            proddetails.append(i[0])
            year.append(i[1])
        for i in cursor1:
            proddetails.append(i[0])
            year.append(i[1])

        print("product details=", proddetails)
        print("year = ", year)
 
  
        fig = plt.figure(figsize = (5, 5))

        plt.bar(year,proddetails, color ='maroon',width = 1)

        plt.xlabel("year")
        plt.ylabel("product details")
        plt.title("graph")
        plt.plot(range(1))
        plt.xlim(2019,2024)
        plt.ylim(500,10000)
        plt.show()
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)
    Form = myana()
    Form.show()
    sys.exit(app.exec_())
