from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import os
from lib.databasemanager import dbMan

class patients_list(QWidget):
    dbManager = dbMan()
    user_id = None
    def __init__(self):
        super(patients_list, self).__init__() # Call the inherited classes __init__ method
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        uic.loadUi('PatientsUidef.ui', self) # Load the .ui file
        self.setupUi()
        
    def setupUi(self):
        patient_list = self.dbManager.getPatientsList()
        patient_list.insert(0,"Create new Patient")
        self.comboBoxPatient.clear()
        self.comboBoxPatient.addItems(patient_list)
        self.comboBoxPatient.activated.connect(lambda: self.item_selected())
        #self.pushButtonPatient.clicked.connect(lambda : self.newPatient())#
        #content = self.comboBoxPatient.currentText()

    def item_selected(self):
        if (self.comboBoxPatient.currentText() == "Create new Patient"):#
            self.lineEditName.setText("")
            self.lineEditDNI.setText("")
            self.comboBoxResults.clear()
            self.lineEditName.setReadOnly(False)
            self.lineEditDNI.setReadOnly(False)
        else:
            text = self.comboBoxPatient.currentText()
            lst = self.dbManager.getPatientInfo(text.split(":")[0])
            self.lineEditName.setText(lst[1])
            self.lineEditName.setReadOnly(True)
            self.lineEditDNI.setText(lst[0])
            self.lineEditDNI.setReadOnly(True)
            self.comboBoxResults.clear()
            self.comboBoxResults.addItems(self.dbManager.getResultList(self.lineEditDNI.text()))#
            
    def newPatient(self, user_id):#
        if (self.comboBoxPatient.currentText() != "Create new Patient"):#
            return None
        name = self.lineEditName.text()
        dni = self.lineEditDNI.text()
        user_id = user_id
        self.dbManager.createPatient(name, dni, user_id)
        self.setupUi()
