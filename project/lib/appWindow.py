from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sqlite3
from PIL import Image
import os
import sys
from lib.finalLoginPark import Ui as Login
from lib.chronoUserAPI import Chrono
from lib.patientsList import patients_list as Patients
from lib.databasemanager import dbMan

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEPARATOR = os.path.sep

class Window(QMainWindow):
    chronoWidget = None
    layChrono = None
    widgetChrono = None
    loginWidget = None
    patientsWidget = None
    user_id = None
    dni = None
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi()
        self.show()
        
    def toPatientListWindow(self):
        self.setupButtons()
        self.patientsWidget.user_id = self.user_id
        self.setCentralWidget(self.patientsWidget)
        
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
        self.dni = self.patientsWidget.comboBoxPatient.currentText().split(":")[0]
        if (self.patientsWidget.comboBoxPatient.currentText() != "Create new Patient"):
            self.setupButtons()
            self.layChrono = QHBoxLayout()
            self.layChrono.addWidget(self.chronoWidget)
            self.widgetChrono = QWidget()
            self.widgetChrono.receiveDNI(self.patientsWidget.comboBoxPatient.currentText().split(":")[0])
            self.widgetChrono.setLayout(self.layChrono)
            self.setCentralWidget(self.widgetChrono)
        
    def login(self):
        self.user_id = self.loginWidget.logUser()
        if self.user_id != None:
            self.toPatientListWindow()
        
    def setupUi(self):
        self.dbManager = dbMan()
        self.dbManager.createTables()
        self.dbManager.createPatient("nom1", "dni1", "test2")
        self.dbManager.createUser("test2", "test2")
        self.dbManager.createResult("","")
        self.setWindowTitle("Parkinson App")
        #self.setFixedSize(854, 480)
        self.setMinimumSize(854, 480)
        #Setups the menu bar
        self.setupMenuBar()
        self.setObjectName("window")
        imgtile = Image.open(APP_PATH + SEPARATOR + "res" + SEPARATOR + "shrek.jpg")
        #self.setStyleSheet("QMainWindow#window {background-image: url(testtiled.png); background-attachment: fixed}; width: auto; height: auto;")
        self.setStyleSheet(imgtile)
        self.setupButtons()
        self.setCentralWidget(self.loginWidget)
        
    def setupMenuBar(self):
        self.aboutAction = QAction(self)
        self.aboutAction.setText("&To about app menu")
        self.aboutAction.triggered.connect(lambda: print("not implemented"))
        self.homeAction = QAction(self)
        self.homeAction.setText("&To home menu")
        self.homeAction.triggered.connect(self.toPatientListWindow)
        helpMenu = QMenu("Help", self)
        appMenu = QMenu("App", self)
        menuBar = QMenuBar()
        menuBar.addMenu(helpMenu)
        menuBar.addMenu(appMenu)
        helpMenu.addAction(self.aboutAction)
        appMenu.addAction(self.homeAction)
        self.setMenuBar(menuBar)
 
    def setupButtons(self):
        self.chronoWidget = Chrono()
        self.loginWidget = Login()
        self.patientsWidget = Patients()
        self.loginWidget.loginButton.clicked.connect(lambda: self.login())
        self.loginWidget.guestButton.clicked.connect(lambda: self.toGuestChronoWindow())
        self.patientsWidget.pushButtonPatient.clicked.connect(lambda : self.patientsWidget.newPatient(self.user_id))
        self.patientsWidget.pushButtonChrono.clicked.connect(lambda: self.toUserChronoWindow())
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application