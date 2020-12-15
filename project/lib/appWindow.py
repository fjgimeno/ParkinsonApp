from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sqlite3
import os
import sys
from lib.finalLoginPark import Ui
from lib.chronoAPI import Chrono

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi()
        self.show()
    
    '''def __init__(self):
        super(Window, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('mainWindow.ui', self) # Load the .ui file
        self.setupUi()
        self.show() # Show the GUI'''
        
    def toLoginWindow(self):
        login = Ui()
        self.setCentralWidget(login)
        
    def toChronoWindow(self):
        chrono = Chrono()
        self.setCentralWidget(chrono)
        
    def setupUi(self):
        self.setWindowTitle("Parkinson App")
        self.setFixedSize(854, 480)
        toolbar = QToolBar("Toolbar")
        login_action = QAction("To Login", self)
        login_action.setStatusTip("Dev button to open login button")
        login_action.triggered.connect(lambda: self.toLoginWindow())
        toolbar.addAction(login_action)
        chrono_action = QAction("To Chrono", self)
        chrono_action.setStatusTip("Dev button to open chrono button")
        chrono_action.triggered.connect(lambda: self.toChronoWindow())
        toolbar.addAction(chrono_action)
        self.addToolBar(toolbar)
        
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application