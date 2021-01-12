from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sqlite3
import asyncio
import os
import sys
from lib.chronoUserAPI import Chrono
from lib.databasemanager import dbMan

class Ui(QWidget):
    databaseName = "parkDataBase.db"
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('LoginUIdef.ui', self) # Load the .ui file
        self.createTable()
        self.setupUi()
        #self.show() # Show the GUI
        
    def setupUi(self):
        pass
        #self.loginButton.clicked.connect(lambda: self.logUser())
        #self.guestButton.clicked.connect(lambda: self.openGuestChrono())
    
    def restorePwd(self):
        self.labelInfo.setText("To restore a user's password, please log-in as administrator.")
        
    def logUser(self):
        resul = self.verifyUser(self.userLineField.text(), self.passLineField.text())
        return resul
        
    def createConnection(self):
        try:
            conn = sqlite3.connect(self.databaseName)
        except Error as e:
            print(e)
        return conn
        
    def createTable(self):
        try:
            open(self.databaseName)
        except IOError:
            open(self.databaseName, "w+")
            conn = self.createConnection()
            c = conn.cursor()
            try:
                c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username varchar(100), password varchar(100));")
                c.execute("insert into users (id, username, password) values (0,'admin','" + "1234" + "');")   
            except sqlite3.DatabaseError as e:
                print(e) 
            conn.commit()                                
            conn.close()
        
    def verifyUser(self, username, password):
        conn = self.createConnection()
        c = conn.cursor()
        c.execute("select username from users where username='" + username + "';")
        data1 = c.fetchall()
        if not data1:
            self.labelInfo.setText("Wrong username and password")
            return None
        else:
            c.execute("select * from users where username='" + str(username) + "' and password='" + str(password) + "';")
            data2 = c.fetchall()
            if not data2:
                self.labelInfo.setText("Wrong password")
                return None
            else:
                return data2[0][0]    #User Found
        conn.commit()
        conn.close()
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application