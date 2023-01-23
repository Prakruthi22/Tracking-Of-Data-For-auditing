from PyQt5 import QtWidgets
from trylog import Ui_Form
import sys
import sqlite3

from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from tryscreen import WelcomeScreen

class mylogapp(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mylogapp,self).__init__()
        self.setupUi(self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.loginfunc)
    def openwindowmain(self):
        wel = WelcomeScreen()
        widget1.addWidget(wel)
        widget1.setCurrentIndex(widget1.currentIndex()+1)

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
                self.pushButton.clicked.connect(self.openwindowmain)
            
            else:
                print("try again")
    

app = QApplication(sys.argv)
welcome = mylogapp()
widget1 = QtWidgets.QStackedWidget()
widget1.addWidget(welcome)
widget1.setFixedHeight(700)
widget1.setFixedWidth(1000)
widget1.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")