from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
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
            self.toUserChronoWindow()
        
    def setupUi(self):
        self.setWindowTitle("Parkinson App")
        #self.setFixedSize(854, 480)
        self.setMinimumSize(854, 480)
        #Setups the menu bar
        self.setupMenuBar()
        self.setObjectName("window")
        self.setStyleSheet("QMainWindow#window {background-image: url(testtiled.png); background-attachment: fixed}; width: auto; height: auto;")
        self.setupButtons()
        self.setCentralWidget(self.loginWidget)
        
    def setupMenuBar(self):
        self.devLoginAction = QAction(self)
        self.devLoginAction.setText("&To login widget")
        self.devLoginAction.triggered.connect(self.toLoginWindow)
        self.devChronoAction = QAction(self)
        self.devChronoAction.setText("&To chrono widget")
        self.devChronoAction.triggered.connect(self.toUserChronoWindow)
        self.devGuestChronoAction = QAction(self)
        self.devGuestChronoAction.setText("&To chrono widget")
        self.devGuestChronoAction.triggered.connect(self.toGuestChronoWindow)
        devMenu = QMenu("&Dev", self)
        menuBar = QMenuBar()
        menuBar.addMenu(devMenu)
        devMenu.addAction(self.devLoginAction)
        devMenu.addAction(self.devChronoAction)
        devMenu.addAction(self.devGuestChronoAction)
        self.setMenuBar(menuBar)

        
    def setupButtons(self):
        self.chronoWidget = Chrono()
        self.loginWidget = Login()
        self.loginWidget.loginButton.clicked.connect(lambda: self.login())
        self.loginWidget.guestButton.clicked.connect(lambda: self.toGuestChronoWindow())
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application