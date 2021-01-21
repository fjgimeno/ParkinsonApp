from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QDialog
import sys
import os

class Home(QtWidgets.QWidget):
    def __init__(self):
        super(Home, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('ui/homescreen.ui', self) # Load the .ui file
        