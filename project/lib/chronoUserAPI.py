# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys, os
from lib.databasemanager import dbMan

class Chrono(QWidget):
    #laptimes values : Minute-Second-Decisecond
    lapTimes = [[0,0,0],[0,0,0],[0,0,0]]
    lapCount = 1
    finishedLap = [False] * 3
    second = 0
    decisecond = 0
    minute = 0
    dni = ""
    result = ""
    # creating flag 
    flag = False
    dbManager = dbMan()

    def __init__(self): 
        super().__init__()
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/res")
        # Importing the UI
        uic.loadUi('ui/CronometreUIdef.ui', self) # Load the .ui file
        # calling method 
        self.UiComponents()   
        # showing all the widgets 
        #self.show() 
        
    def receiveDNI(self, dni):
        self.dni = dni

    # method for widgets 
    def UiComponents(self):
        # add action to the method 
        self.start.pressed.connect(self.Start) 
        # add action to the method 
        self.pause.pressed.connect(self.Pause) 
        # add action to the method 
        self.re_set.pressed.connect(self.Re_set) 
        # Saves results and comments
        self.pushButtonSubmitResults.clicked.connect(lambda: self.save_result())
        # creating a timer object 
        timer = QTimer(self) 
        # adding action to timer 
        timer.timeout.connect(self.showTime) 
        # update the timer every tenth second 
        timer.start(100) 

    # method called by timer 
    def showTime(self):   
        # checking if flag is true 
        if self.flag: 
            if (self.decisecond >= 10):
                self.decisecond = 0
                self.second += 1
                if (self.second >= 60):
                    self.minute += 1
                    self.second = 0
            # incrementing the centiseconder 
            self.decisecond += 1  
        # getting text from centisecond
        if (self.minute < 10):
            minTxt = "0" + str(self.minute)
        else:
            minTxt = str(self.minute)
        if (self.second < 10):
            secTxt = "0" +  str(self.second)
        else:
            secTxt = str(self.second)            
        text = minTxt + ":" +  secTxt  
        # showing text 
        self.label.setText(text)
        if(self.finishedLap[0] == False):            
            self.lap1.setText("Lap1: " + text)
        if(self.finishedLap[1] == False):   
            self.lap2.setText("Lap2: " + text)
        if(self.finishedLap[2] == False):   
            self.lap3.setText("Lap3: " + text)  

    def Start(self): 
        if(self.flag):
            self.lapTimes[self.lapCount - 1][0] = self.minute
            self.lapTimes[self.lapCount - 1][1] = self.second
            self.lapTimes[self.lapCount - 1][2] = self.decisecond
            self.finishedLap[self.lapCount - 1] = True
            self.lapCount += 1
            if (self.lapCount == 3):
                self.start.setText("Stop")
            elif(self.lapCount >= 3):
                #GUARDAR RESULTATAS
                #self.save_result()
                cont = 1
                for res in self.lapTimes:
                    if cont != 3:
                        self.result = self.result + str(res[0]) + ":" + str(res[1]) + ":" + str(res[2]) + ","
                        cont = cont + 1
                    else:
                        self.result = self.result + str(res[0]) + ":" + str(res[1]) + ":" + str(res[2])
                cont = 1
                self.Re_set()
        else:
            self.flag = True

    def Pause(self):   
        # making flag to False 
        self.flag = False

    def Re_set(self):   
        # making flag to false 
        self.start.setText("Start")
        self.flag = False  
        # reseeting the centisecond 
        self.centisecond = 0
        self.decisecond = 0
        self.second = 0
        self.minute = 0
        self.lapCount = 1
        for i in range(3):
            self.finishedLap[i] = False
            self.lapTimes[i][0] = 0
            self.lapTimes[i][1] = 0
            self.lapTimes[i][2] = 0
        # setting text to label 
        self.label.setText("00:00")

    def save_result(self):
        print(self.dni)
        result = ""
        '''cont = 1
        for res in self.lapTimes:
            if cont != 3:
                result = result + str(res[0]) + ":" + str(res[1]) + ":" + str(res[2]) + ","
                cont = cont + 1
            else:
                result = result + str(res[0]) + ":" + str(res[1]) + ":" + str(res[2])'''
        print (self.result)
        self.dbManager.createResult(self.result, self.dni, self.commentBox.toPlainText())