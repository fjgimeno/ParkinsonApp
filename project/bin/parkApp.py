#This is the main python file for the application.
from PyQt5 import QtWidgets
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.appWindow import Window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
    mainWindow = Window() # Create an instance of our class
    app.exec_() # Start the application
    