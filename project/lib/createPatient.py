from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sqlite3
import asyncio
import os
import sys
from lib.databasemanager import dbMan

class Ui(QWidget):
    databaseName = "parkDataBase.db"
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res/ui")
        uic.loadUi('CreatePatient.ui', self) # Load the .ui file
        #self.show() # Show the GUI
        #self.loginButton.clicked.connect(lambda: self.logUser())
        #self.guestButton.clicked.connect(lambda: self.openGuestChrono())
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application
