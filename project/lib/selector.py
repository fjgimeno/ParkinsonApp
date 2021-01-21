from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog
import sys
import os

class Selector(QtWidgets.QDialog):
    file_full_path = ""
    def __init__(self):
        super(Selector, self).__init__() # Call the inherited classes __init__ method
        dialog = QtWidgets.QFileDialog(self)
        dialog.setWindowTitle('Open PNG File')
        dialog.setNameFilter('PNG files (*.png)')
        dialog.setDirectory(QtCore.QDir.currentPath())
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.file_full_path = str(dialog.selectedFiles()[0])
        else:
            return None
        
    def saveImage(self, dni, isFace):
        if (isFace == True):
            os.system("mkdir ../res/patImg/face/" + str(dni))
            os.system("cp " + self.file_full_path + " ../res/patImg/face/" + str(dni) + "/face.png")
            return "patImg/face/" + str(dni) + "/face.png"
        else:
            os.system("mkdir ../res/patImg/body/" + str(dni))
            os.system("cp " + self.file_full_path + " ../res/patImg/body/" + str(dni) + "/body.png")
            return "patImg/body/" + str(dni) + "/body.png"
        