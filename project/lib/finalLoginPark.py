from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import sqlite3
import asyncio
import os
import sys
from lib.chronoAPI import Chrono

class Ui(QMainWindow):
    databaseName = "parkDataBase.db"
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('testLoginJav.ui', self) # Load the .ui file
        self.createTable()
        self.setupUi()
        self.show() # Show the GUI
        
    def setupUi(self):
        self.loginButton.clicked.connect(lambda: self.verifyUser(self.userLineField.text(), hash(self.passLineField.text())))
        self.guestButton.clicked.connect(lambda: self.openGuestChrono())
        
    def openGuestChrono(self):
        chrono = Chrono() # Create an instance of our class
        print("Opening...")
        chrono.show()
        print("Done!")
        
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
                c.execute("insert into users (id, username, password) values (0,'admin','" + str(hash("admin")) + "');")   
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
            print ('Incorrect user or password')
        else:
            c.execute("select username from users where username='" + username + "' and password='" + str(hash(password)) + "';")
            data2 = c.fetchall()
            if not data2:
                print ('Incorrect password')
            else:
                print ('found')
                #chrono = QWidget(self)
                chrono = chronoAPI
                chronoWindow = chrono.Window()
                chronoWindow.show()
        conn.commit()
        conn.close()
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application