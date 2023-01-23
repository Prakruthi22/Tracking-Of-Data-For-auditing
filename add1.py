

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 851))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bglabel = QtWidgets.QLabel(self.frame)
        self.bglabel.setGeometry(QtCore.QRect(0, 0, 1001, 851))
        self.bglabel.setStyleSheet("background-color: rgb(207, 255, 245);\n"
"border-radius:20px\n"
"")
        self.bglabel.setObjectName("bglabel")
        self.mainlabel = QtWidgets.QLabel(self.frame)
        self.mainlabel.setGeometry(QtCore.QRect(110, 80, 801, 41))
        self.mainlabel.setStyleSheet("font: 20pt \"Algerian\";")
        self.mainlabel.setObjectName("mainlabel")
        self.incomelabel = QtWidgets.QLabel(self.frame)
        self.incomelabel.setGeometry(QtCore.QRect(20, 160, 331, 21))
        self.incomelabel.setStyleSheet("font: 14pt \"Algerian\";")
        self.incomelabel.setObjectName("incomelabel")
        self.productlabel = QtWidgets.QLabel(self.frame)
        self.productlabel.setGeometry(QtCore.QRect(20, 310, 361, 21))
        self.productlabel.setStyleSheet("font: 14pt \"Algerian\";")
        self.productlabel.setObjectName("productlabel")
        self.rawlabel = QtWidgets.QLabel(self.frame)
        self.rawlabel.setGeometry(QtCore.QRect(20, 470, 481, 21))
        self.rawlabel.setStyleSheet("font: 14pt \"Algerian\";")
        self.rawlabel.setObjectName("rawlabel")
        self.emplabel = QtWidgets.QLabel(self.frame)
        self.emplabel.setGeometry(QtCore.QRect(20, 630, 411, 21))
        self.emplabel.setStyleSheet("font: 14pt \"Algerian\";")
        self.emplabel.setObjectName("emplabel")
        self.income = QtWidgets.QLineEdit(self.frame)
        self.income.setGeometry(QtCore.QRect(70, 220, 150, 30))
        self.income.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.income.setObjectName("income")
        self.month = QtWidgets.QLineEdit(self.frame)
        self.month.setGeometry(QtCore.QRect(280, 220, 150, 30))
        self.month.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.month.setObjectName("month")
        self.year = QtWidgets.QLineEdit(self.frame)
        self.year.setGeometry(QtCore.QRect(460, 220, 150, 30))
        self.year.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.year.setObjectName("year")
        self.prodname = QtWidgets.QLineEdit(self.frame)
        self.prodname.setGeometry(QtCore.QRect(50, 380, 150, 30))
        self.prodname.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.prodname.setObjectName("prodname")
        self.prodquan = QtWidgets.QLineEdit(self.frame)
        self.prodquan.setGeometry(QtCore.QRect(250, 380, 150, 30))
        self.prodquan.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.prodquan.setObjectName("prodquan")
        self.prodprice = QtWidgets.QLineEdit(self.frame)
        self.prodprice.setGeometry(QtCore.QRect(500, 380, 150, 30))
        self.prodprice.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.prodprice.setObjectName("prodprice")
        self.yearproduct = QtWidgets.QLineEdit(self.frame)
        self.yearproduct.setGeometry(QtCore.QRect(700, 380, 150, 30))
        self.yearproduct.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.yearproduct.setObjectName("yearproduct")
        self.rawname = QtWidgets.QLineEdit(self.frame)
        self.rawname.setGeometry(QtCore.QRect(60, 530, 150, 30))
        self.rawname.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.rawname.setObjectName("rawname")
        self.rawprice = QtWidgets.QLineEdit(self.frame)
        self.rawprice.setGeometry(QtCore.QRect(290, 530, 150, 30))
        self.rawprice.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.rawprice.setObjectName("rawprice")
        self.rawquan = QtWidgets.QLineEdit(self.frame)
        self.rawquan.setGeometry(QtCore.QRect(470, 530, 150, 30))
        self.rawquan.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.rawquan.setObjectName("rawquan")
        self.rawyear = QtWidgets.QLineEdit(self.frame)
        self.rawyear.setGeometry(QtCore.QRect(650, 530, 150, 30))
        self.rawyear.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.rawyear.setObjectName("rawyear")
        self.empname = QtWidgets.QLineEdit(self.frame)
        self.empname.setGeometry(QtCore.QRect(60, 670, 150, 30))
        self.empname.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.empname.setObjectName("empname")
        self.phno = QtWidgets.QLineEdit(self.frame)
        self.phno.setGeometry(QtCore.QRect(290, 670, 200, 30))
        self.phno.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;\n"
"")
        self.phno.setObjectName("phno")
        self.empsal = QtWidgets.QLineEdit(self.frame)
        self.empsal.setGeometry(QtCore.QRect(530, 670, 150, 30))
        self.empsal.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.empsal.setObjectName("empsal")
        self.empyear = QtWidgets.QLineEdit(self.frame)
        self.empyear.setGeometry(QtCore.QRect(730, 670, 170, 30))
        self.empyear.setStyleSheet("font: 12pt \"Algerian\";\n"
"border-bottom-color: rgb(14, 18, 72);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"padding-bottom:3px;")
        self.empyear.setObjectName("empyear")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 100, 27))
        self.pushButton.setStyleSheet("font: 10pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        self.incomebtn = QtWidgets.QPushButton(self.frame)
        self.incomebtn.setGeometry(QtCore.QRect(40, 270, 100, 27))
        self.incomebtn.setStyleSheet("font: 10pt \"Algerian\";")
        self.incomebtn.setObjectName("incomebtn")
        self.prodbtn = QtWidgets.QPushButton(self.frame)
        self.prodbtn.setGeometry(QtCore.QRect(40, 420, 100, 27))
        self.prodbtn.setStyleSheet("font: 10pt \"Algerian\";")
        self.prodbtn.setObjectName("prodbtn")
        self.rawbtn = QtWidgets.QPushButton(self.frame)
        self.rawbtn.setGeometry(QtCore.QRect(40, 580, 100, 27))
        self.rawbtn.setStyleSheet("font: 10pt \"Algerian\";")
        self.rawbtn.setObjectName("rawbtn")
        self.salbtn = QtWidgets.QPushButton(self.frame)
        self.salbtn.setGeometry(QtCore.QRect(40, 720, 100, 27))
        self.salbtn.setStyleSheet("font: 10pt \"Algerian\";")
        self.salbtn.setObjectName("salbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bglabel.setText(_translate("Form", "."))
        self.mainlabel.setText(_translate("Form", "PLEASE FILL IN THE  REQUIRED DETAILS"))
        self.incomelabel.setText(_translate("Form", "income details"))
        self.productlabel.setText(_translate("Form", "PRODUCT DETAILS"))
        self.rawlabel.setText(_translate("Form", "Raw materials details"))
        self.emplabel.setText(_translate("Form", "EMPLOYEE SALARY DETAILS"))
        self.income.setText(_translate("Form", "income"))
        self.month.setText(_translate("Form", "MONTH"))
        self.year.setText(_translate("Form", "YEAR"))
        self.prodname.setText(_translate("Form", "name"))
        self.prodquan.setText(_translate("Form", "quantity"))
        self.prodprice.setText(_translate("Form", "price"))
        self.yearproduct.setText(_translate("Form", "year"))
        self.rawname.setText(_translate("Form", "name"))
        self.rawprice.setText(_translate("Form", "PRICE"))
        self.rawquan.setText(_translate("Form", "quantity"))
        self.rawyear.setText(_translate("Form", "year"))
        self.empname.setText(_translate("Form", "name"))
        self.phno.setText(_translate("Form", "phone number"))
        self.empsal.setText(_translate("Form", "salary"))
        self.empyear.setText(_translate("Form", "salary year"))
        self.pushButton.setText(_translate("Form", "back"))
        self.incomebtn.setText(_translate("Form", "submit"))
        self.prodbtn.setText(_translate("Form", "submit"))
        self.rawbtn.setText(_translate("Form", "submit"))
        self.salbtn.setText(_translate("Form", "submit"))
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QWidget()
    uI=Ui_Form1()
    uI.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())