from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sqlite3
import os
import sys
from lib.finalLoginPark import Ui as Login
from lib.chronoAPI import Chrono

class Window(QMainWindow):
    chronoWidget = None
    layChrono = None
    widgetChrono = None
    loginWidget = None
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi()
        self.show()
        
    def toLoginWindow(self):
        self.setupButtons()
        self.setCentralWidget(self.loginWidget)
        
    def toGuestChronoWindow(self):
        self.setupButtons()
        self.layChrono = QHBoxLayout()
        self.layChrono.addWidget(self.chronoWidget)
        self.widgetChrono = QWidget()
        self.widgetChrono.setLayout(self.layChrono)
        self.setCentralWidget(self.widgetChrono)
        
    def toUserChronoWindow(self):
        self.layChrono = QHBoxLayout()
        self.layChrono.addWidget(self.chronoWidget)
        self.widgetChrono = QWidget()
        self.widgetChrono.setLayout(self.layChrono)
        self.setCentralWidget(self.widgetChrono)
        
    def login(self):
        result = self.loginWidget.logUser()
        if result == 0:
            print("Found")
            self.toUserChronoWindow()
        elif result == 1:
            print("Wrong pass")
        else: 
            print("Wrong user and pass") 
        
    def setupUi(self):
        self.setWindowTitle("Parkinson App")
        #self.setFixedSize(854, 480)
        self.setMinimumSize(854, 480)
        toolbar = QToolBar("Toolbar")
        login_action = QAction("To Login", self)
        login_action.setStatusTip("Dev button to open login button")
        login_action.triggered.connect(lambda: self.toLoginWindow())
        toolbar.addAction(login_action)
        chrono_action = QAction("To Guest Chrono", self)
        chrono_action.setStatusTip("Dev button to open chrono button")
        chrono_action.triggered.connect(lambda: self.toGuestChronoWindow())
        self.setupButtons()
        #self.
        toolbar.addAction(chrono_action)
        self.addToolBar(toolbar)
        
    def setupButtons(self):
        self.chronoWidget = Chrono()
        self.loginWidget = Login()
        self.loginWidget.loginButton.clicked.connect(lambda: self.login())
        self.loginWidget.guestButton.clicked.connect(lambda: self.toGuestChronoWindow())
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application