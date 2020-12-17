# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 

class Chrono(QWidget):   
    def __init__(self): 
        super().__init__()   
        # setting title 
        self.setWindowTitle("Python Stop watch")   
        # setting geometry 
        self.setGeometry(100, 100, 400, 500)   
        # calling method 
        self.UiComponents()   
        # showing all the widgets 
        self.show() 

    # method for widgets 
    def UiComponents(self):
        #laptimes values : Minute-Second-Decisecond
        self.lapTimes = [[0,0,0],[0,0,0],[0,0,0]]
        self.lapCount = 1
        self.finishedLap = [False] * 3
        self.second = 0
        self.decisecond = 0
        self.minute = 0
        # creating flag 
        self.flag = False
        # creating a label to show the time 
        self.label = QLabel(self)
        self.lap1 = QLabel(self) 
        self.lap2 = QLabel(self)
        self.lap3 = QLabel(self)
        # setting geometry of label 
        self.label.setGeometry(75, 100, 250, 70)
        self.lap1.setGeometry(75, 175, 250, 20)
        self.lap2.setGeometry(75, 200, 250, 20) 
        self.lap3.setGeometry(75, 225, 250, 20) 
        # adding border to the label 
        self.label.setStyleSheet("border : 4px solid black;") 
        self.lap1.setStyleSheet("border : 2px solid black;") 
        self.lap2.setStyleSheet("border : 2px solid black;") 
        self.lap3.setStyleSheet("border : 2px solid black;") 
        # setting text to the label 
        self.label.setText("00:00") 
        self.lap1.setText("00:00")
        self.lap2.setText("00:00")
        self.lap3.setText("00:00")
        # setting font to the label 
        self.label.setFont(QFont('Arial', 25)) 
        self.lap1.setFont(QFont('Arial', 10)) 
        self.lap2.setFont(QFont('Arial', 10)) 
        self.lap3.setFont(QFont('Arial', 10)) 
        # setting alignment to the text of label 
        self.label.setAlignment(Qt.AlignCenter) 
        self.lap1.setAlignment(Qt.AlignLeft) 
        self.lap2.setAlignment(Qt.AlignLeft) 
        self.lap3.setAlignment(Qt.AlignLeft) 
        # creating start button 
        self.start = QPushButton("Start", self) 
        # setting geometry to the button 
        self.start.setGeometry(125, 250, 150, 40) 
        # add action to the method 
        self.start.pressed.connect(self.Start) 
        # creating pause button 
        pause = QPushButton("Pause", self) 
        # setting geometry to the button 
        pause.setGeometry(125, 300, 150, 40) 
        # add action to the method 
        pause.pressed.connect(self.Pause) 
        # creating reset button 
        re_set = QPushButton("Re-set", self) 
        # setting geometry to the button 
        re_set.setGeometry(125, 350, 150, 40) 
        # add action to the method 
        re_set.pressed.connect(self.Re_set) 
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
        for lap in self.lapTimes:
            print (lap)
        for i in range(3):
            self.lapTimes[i][0] = 0
            self.lapTimes[i][1] = 0
            self.lapTimes[i][2] = 0
        for lap in self.lapTimes:
            print (lap)  
        # setting text to label 
        self.label.setText("00:00")