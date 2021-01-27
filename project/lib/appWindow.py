from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence
import sqlite3
from PIL import Image
import os
import sys
from lib.finalLoginPark import UserLoginDialog as Login
from lib.chronoUserAPI import Chrono
from lib.patientsList import patients_list as Patients
from lib.databasemanager import dbMan
from lib.createusers import CreateUserDialog as CreateUser
from lib.createPatient import Ui as CreatePatient
from lib.selector import Selector
from lib.homeScreen import Home
from lib.showPatientInfo import PatientInfo as patientInfoScreen

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res/ui")
SEPARATOR = os.path.sep

class Window(QMainWindow):
    mainwindow = None
    createuser = None
    chronoWidget = None
    layChrono = None
    widgetChrono = None
    loginWidget = None
    patientsWidget = None
    user_id = None
    dni = None
    admin = False
    homeScreen = None
    patInScreen = None
    fImage = ""
    bImage = ""

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi()
        self.toLoginDialog()
        self.homeScreen = Home()
	
    def toHomeScreen(self):
        if (self.admin == True):
            self.setupMenuBar()
        self.setupButtons()
        self.homeScreen = Home()
        self.setCentralWidget(self.homeScreen)

    def toCreateUserDialog(self):
        self.setupButtons()
        self.createuser.show()
        
    def toCancelCreateUserDialog(self):
        self.createuser.hide()
        self.createuser = None
        
    def toCreatePatientDialog(self):
        self.setupButtons()
        self.setCentralWidget(self.createpatient)
	 
    def toPatientListWindow(self):
        if (self.admin == True):
            self.setupMenuBar()
        self.setupButtons()
        self.patientsWidget.user_id = self.user_id
        self.setCentralWidget(self.patientsWidget)
        
    def toLoginDialog(self):
        if self.loginWidget == None:
            self.admin = False
            self.setupMenuBar()
            self.loginWidget = Login()
            self.loginWidget.loginButton.clicked.connect(lambda: self.login())
            self.loginWidget.guestButton.clicked.connect(lambda: self.toGuestChronoWindow())
            self.loginWidget.show()
        else:
            self.admin = False
        
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
            self.chronoWidget.receiveDNI(self.dni)
            self.setCentralWidget(self.chronoWidget)
        
    def login(self):
        self.user_id = self.loginWidget.logUser()
        if self.user_id != None:
            if self.user_id == 0:
                self.admin = True
            self.toHomeScreen()
            self.loginWidget.hide()
            self.loginWidget = None
            self.showMaximized()

    def toPatientInfoDialog(self):
        self.dni = self.patientsWidget.getActualDni()
        self.patInScreen = patientInfoScreen()
        self.patInScreen.newFPicButton.clicked.connect(lambda: self.selectimage(True))
        self.patInScreen.newBPicButton.clicked.connect(lambda: self.selectimage(False))
        self.patInScreen.fImage = self.fImage
        self.patInScreen.bImage = self.bImage
        self.patInScreen.writePatientInfo(str(self.dni), self.fImage, self.bImage)        
        #self.paiInScreen.dni = str(self.dni)
        #self.patInScreen.saveEditButton.clicked.connect(lambda: self.patInScreen.saveInfo())
        self.patInScreen.show()
        
    def setupUi(self):
        self.dbManager = dbMan()
        self.dbManager.createTables()
        self.setWindowTitle("PEA: Main window")
        self.setMinimumSize(854, 480)
        #Setups the menu bar
        self.setupMenuBar()
        self.setObjectName("window")
        self.setStyleSheet("QMainWindow#window {background-color: rgb(32,32,32); background-image: url('background.jpg'); background-attachment: fixed}; width: auto; height: auto;")
        self.setupButtons()
        
    def setupMenuBar(self):
        self.aboutAction = QAction(self)
        self.aboutAction.setText("&To about app menu")
        self.aboutAction.triggered.connect(lambda: print("not implemented"))
        
        self.extractAction = QAction(self)
        self.extractAction.setText("&To Database extraction app menu")
        self.extractAction.triggered.connect(lambda: print("not implemented"))
        
        self.patiListAction = QAction(self)
        self.patiListAction.setText("&To Patient List app menu")
        self.patiListAction.triggered.connect(self.toPatientListWindow)

        self.homeAction = QAction(self)
        self.homeAction.setText("&To home menu")
        self.homeAction.triggered.connect(self.toHomeScreen)
        
        self.createUserAction = QAction(self)
        self.createUserAction.setText("&Create User")
        self.createUserAction.triggered.connect(self.toCreateUserDialog)
        
        helpMenu = QMenu("Help", self)
        appMenu = QMenu("App", self)
        createUserMenu = QMenu("Create User",self)
        extractorMenu = QMenu("Extract Database",self)
        patientListMenu = QMenu("To Patient List", self)
        
        menuBar = QMenuBar()
        menuBar.addMenu(helpMenu)
        menuBar.addMenu(appMenu)
        menuBar.addMenu(extractorMenu)
        menuBar.addMenu(patientListMenu)
        
        if (self.admin == True):
            menuBar.addMenu(createUserMenu)
            createUserMenu.addAction(self.createUserAction)

        appMenu.addAction(self.homeAction)
        extractorMenu.addAction(self.extractAction)
        patientListMenu.addAction(self.patiListAction)

        self.setMenuBar(menuBar)
 
    def setupButtons(self):
        self.chronoWidget = Chrono()
        self.patientsWidget = Patients()
        self.createuser = CreateUser()
        self.createpatient = CreatePatient()
        self.patientsWidget.pushButtonNewPatient.clicked.connect(lambda : self.toCreatePatientDialog())
        self.patientsWidget.pushButtonChrono.clicked.connect(lambda: self.toUserChronoWindow())
        self.patientsWidget.pushButtonToInfo.clicked.connect(lambda: self.toPatientInfoDialog())
        self.createuser.CreateUserCancelButton.clicked.connect(lambda: self.toCancelCreateUserDialog())
        self.createuser.CreateUserSubmitButton.clicked.connect(lambda: self.submitNewUser())
        self.createpatient.pushButtonPatient.clicked.connect(lambda: self.submitNewPatient())

    def submitNewUser(self):
        username = self.createuser.CreateUseruserLineField.text()
        userpass = self.createuser.CreateUserpassLineField.text()
        self.dbManager.createUser(username,userpass)
        self.createuser.CreateUseruserLineField.setText("")
        self.createuser.CreateUserpassLineField.setText("")
        
    def submitNewPatient(self):
        name = self.createpatient.lineEditName.text()
        sip = self.createpatient.lineEditsip.text()
        surname = self.createpatient.lineEditsurname.text()
        dni = self.createpatient.lineEditDNI.text()
        birth = self.createpatient.lineEditdate_of_birth.text()
        diagnostic = self.createpatient.lineEditdiagnostic_date.text()
        medication = self.createpatient.textEditMedication.toPlainText()
        phone = self.createpatient.lineEditphone.text()
        mail = self.createpatient.lineEditMail.text()
        height = self.createpatient.lineEditHeight.text()
        weight = self.createpatient.lineEditWeight.text()
        gender = self.createpatient.lineEditGender.text()
        phase = self.createpatient.lineEditPhase.text()
        imc = self.createpatient.lineEditImc.text()
        self.dbManager.createPatient(name,dni,self.user_id,sip,surname,birth,diagnostic,medication,phone,mail,height,weight,gender,phase,imc,"","")
        
    def selectimage(self, isFace):
        #dni = self.createpatient.lineEditDNI.text()
        if (self.dni != None and self.dni != ""):
            selector = Selector()
            selector.show()
            if (isFace == True):
                self.fImage = selector.saveImage(self.dni, isFace)
            else:
                self.bImage = selector.saveImage(self.dni, isFace)
            
'''UPDATE PATIENT SET GENDER = 'MASC',DNI = '20202020X' WHERE ID = 6;'''