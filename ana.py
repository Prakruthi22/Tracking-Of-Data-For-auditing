# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys,resana

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(979, 700)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 971, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bg = QtWidgets.QLabel(self.frame)
        self.bg.setGeometry(QtCore.QRect(0, 0, 971, 671))
        self.bg.setStyleSheet("border-image: url(:/images/analysis.jpg);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.mainlabel = QtWidgets.QLabel(self.frame)
        self.mainlabel.setGeometry(QtCore.QRect(30, 70, 871, 111))
        self.mainlabel.setStyleSheet("font: 20pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.mainlabel.setObjectName("mainlabel")
        self.incomelabel = QtWidgets.QLabel(self.frame)
        self.incomelabel.setGeometry(QtCore.QRect(50, 220, 351, 41))
        self.incomelabel.setStyleSheet("font: 14pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.incomelabel.setObjectName("incomelabel")
        self.rawlabel = QtWidgets.QLabel(self.frame)
        self.rawlabel.setGeometry(QtCore.QRect(50, 290, 421, 31))
        self.rawlabel.setStyleSheet("font: 14pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.rawlabel.setObjectName("rawlabel")
        self.prodlabel = QtWidgets.QLabel(self.frame)
        self.prodlabel.setGeometry(QtCore.QRect(50, 360, 381, 31))
        self.prodlabel.setStyleSheet("font: 14pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.prodlabel.setObjectName("prodlabel")
        self.sallabel = QtWidgets.QLabel(self.frame)
        self.sallabel.setGeometry(QtCore.QRect(50, 430, 551, 31))
        self.sallabel.setStyleSheet("font: 14pt \"Algerian\";\n"
"color: rgb(255, 255, 255);")
        self.sallabel.setObjectName("sallabel")
       # self.profitlabel = QtWidgets.QLabel(self.frame)
        #self.profitlabel.setGeometry(QtCore.QRect(50, 500, 391, 41))
        #self.profitlabel.setStyleSheet("font: 14pt \"Algerian\";\n""color: rgb(255, 255, 255);")
        #self.profitlabel.setObjectName("profitlabel")
        self.ingraphbtn = QtWidgets.QPushButton(self.frame)
        self.ingraphbtn.setGeometry(QtCore.QRect(380, 230, 76, 27))
        self.ingraphbtn.setObjectName("ingraphbtn")
        self.rawgraphbtn = QtWidgets.QPushButton(self.frame)
        self.rawgraphbtn.setGeometry(QtCore.QRect(480, 290, 121, 27))
        self.rawgraphbtn.setObjectName("rawgraphbtn")
        self.prodgraphbtn = QtWidgets.QPushButton(self.frame)
        self.prodgraphbtn.setGeometry(QtCore.QRect(390, 360, 76, 27))
        self.prodgraphbtn.setObjectName("prodgraphbtn")
        self.salgraphbtn = QtWidgets.QPushButton(self.frame)
        self.salgraphbtn.setGeometry(QtCore.QRect(550, 430, 76, 27))
        self.salgraphbtn.setObjectName("salgraphbtn")
        #self.profitbtn = QtWidgets.QPushButton(self.frame)
        #self.profitbtn.setGeometry(QtCore.QRect(450, 510, 56, 27))
        #self.profitbtn.setObjectName("profitbtn")
        self.backbtn = QtWidgets.QPushButton(self.frame)
        self.backbtn.setGeometry(QtCore.QRect(20, 20, 76, 27))
        self.backbtn.setStyleSheet("font: 10pt \"Algerian\";")
        self.backbtn.setObjectName("backbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mainlabel.setText(_translate("Form", "ALL YOU\'RE DATA ANALYSIS ARE HERE.\n"
" YOU CAN VIEW YOUR DATA IN THE FORM OF STATISTICS"))
        self.incomelabel.setText(_translate("Form", "INCOME STATISTICS  ->"))
        self.rawlabel.setText(_translate("Form", "RAW MATERIAL \'S STATISTICS ->"))
        self.prodlabel.setText(_translate("Form", "PRODUCT\'S STATISTICS ->"))
        self.sallabel.setText(_translate("Form", "EMPLYOYEE\'S SALARY  STATISTICS ->"))
        #self.profitlabel.setText(_translate("Form", "PROFIT\'S OVER THE YEARS->"))
        self.ingraphbtn.setText(_translate("Form", "Income"))
        self.rawgraphbtn.setText(_translate("Form", "Raw Materials"))
        self.prodgraphbtn.setText(_translate("Form", "Products"))
        self.salgraphbtn.setText(_translate("Form", "Salary"))
        #self.profitbtn.setText(_translate("Form", "Profits"))
        self.backbtn.setText(_translate("Form", "Back"))
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QWidget()
    uI=Ui_Form()
    uI.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
