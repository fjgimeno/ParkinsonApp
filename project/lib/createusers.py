from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sqlite3
import asyncio
import os
import sys
from lib.databasemanager import dbMan

class CreateUserDialog(QtWidgets.QDialog):
    databaseName = "parkDataBase.db"
    def __init__(self):
        super(CreateUserDialog, self).__init__() # Call the inherited classes __init__ method
        #newUserWidget = QWidget()
        #newUserLayout = 
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('ui/CreateUser.ui', self) # Load the .ui file
        self.setWindowTitle("PEA: New user")
        
    def closeEvent(self, event):
        pass
'''        self.createTable()
        self.setupUi()
        self.show()  Show the GUI
    
    def setupUi(self):
        self.CreateUserCancelButton.clicked.connect(self.restorePwd)
        pass
        self.loginButton.clicked.connect(lambda: self.logUser())
        self.guestButton.clicked.connect(lambda: self.openGuestChrono())
        
app = QtWidgets.QApplication(sys.argv)  Create an instance of QtWidgets.QApplication
window = Ui()  Create an instance of our class
app.exec_()  Start the application '''