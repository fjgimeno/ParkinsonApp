from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtGui import QPixmap
import sys
import os
from lib.databasemanager import dbMan
class PatientInfo(QtWidgets.QDialog):
    dbManager = dbMan()
    fImage = ""
    bImage = ""
    def __init__(self):
        super(PatientInfo, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('ui/PatientUserInfoUIdef.ui', self) # Load the .ui file
        
    def writePatientInfo(self, dni, fImage, bImage):
        self.fImage = fImage
        self.bImage = bImage
        info = self.dbManager.getPatientInfo(dni)
        self.labelName.setText(str(info[3]))#3
        self.labelSurname.setText(str(info[2]))#2
        self.labelDNI.setText(str(info[0]))#0
        self.labelSIP.setText(str(info[1]))#1
        self.labelEmail.setText(str(info[5]))#5
        self.labelPhone.setText(str(info[4]))#4
        self.labelBirthday.setText(str(info[8]))#8
        self.labelSex.setText(str(info[9]))#9
        self.labelHeight.setText(str(info[6]))#6
        self.labelWeight.setText(str(info[7]))#7
        self.labelDiagnosticDate.setText(str(info[10]))#10
        self.labelParkPhase.setText(str(info[11]))#11
        self.labelImc.setText(str(info[12]))#12
        self.labelMedication.setText(str(info[13]))#13
        
        self.saveInfo()
        self.loadPatientImages()

    def saveInfo(self):
        self.dbManager.alterTablePatients(self.labelName.text(), self.labelDNI.text(), self.labelSurname.text(), self.labelBirthday.text(), self.labelDiagnosticDate.text(), self.labelMedication.text(), self.labelPhone.text(), self.labelEmail.text(), self.labelHeight.text(), self.labelWeight.text(), self.labelSex.text(), self.labelParkPhase.text(), self.labelImc.text(), self.fImage, self.bImage)

    def loadPatientImages(self):
        data = self.dbManager.getPatientInfo(self.labelDNI.text())
        if (data[len(data) - 3] != "" and data[len(data) - 3] != None):
            face = QPixmap(data[len(data) - 3])
            smaller_face = face.scaled(241, 221)
            self.labelFacePic.setPixmap(smaller_face)
        else: 
            face = QPixmap('patImg/face/facePlaceholder.png')
            smaller_face = face.scaled(241, 221)
            self.labelFacePic.setPixmap(smaller_face)
            
        if (data[len(data) - 2] != "" and data[len(data) - 2] != None):
            body = QPixmap(data[len(data) - 2])
            smaller_body = body.scaled(271, 401)
            self.labelBodyPic.setPixmap(smaller_body)
        else: 
            body = QPixmap('patImg/body/bodyPlaceholder.png')
            smaller_body = body.scaled(271, 401)
            self.labelBodyPic.setPixmap(smaller_body)

        