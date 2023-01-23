from PyQt5 import QtWidgets
from add1 import Ui_Form1
import sys
import sqlite3


class myadd(QtWidgets.QWidget,Ui_Form1):
    def __init__(self):
        super(myadd,self).__init__()
        self.setupUi(self)
        self.incomebtn.clicked.connect(self.addfunc)
        self.prodbtn.clicked.connect(self.prodfunc)
        self.rawbtn.clicked.connect(self.rawfunc)
        self.salbtn.clicked.connect(self.salfunc)
    
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
        
if __name__=="__main__":
    app =QtWidgets.QApplication(sys.argv)
    Form = myadd()
    Form.show()
    sys.exit(app.exec_())