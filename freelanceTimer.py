from __future__ import print_function
import sys
import os
import csv
from PyQt4.QtGui import *
from PyQt4.QtCore import QDate
from freelanceTimerUI import *
from addTimersUI import *


        # Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.running = False
        self.hours = 0
        self.time = 0
        self.ui.actionAdd_Project.triggered.connect(self.addProject)
        self.ui.actionSave_Timers.triggered.connect(self.saveTimers)
        self.ui.pushButton.clicked.connect(self.startStop)
        self.timer = QtCore.QTimer(interval=1000) # miliseconds
        self.timer.timeout.connect(self.on_every_second)
#        with open("timers.csv", 'r') as csvfile:
#            timercsv = csv.reader(csvfile, dialect='excel')
#            for row in timercsv:
                
       
    def addProject(self):
        pass
        
    def saveTimers(self):
        pass

    def startStop(self):
        if self.running == True:
            self.running = False
            self.timer.stop()
            self.ui.pushButton.setText("Start")
            self.ui.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n" + "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 100, 0, 255), stop:1 rgba(0, 255, 0, 255));")
        else:
            self.running = True
            self.timer.start()
            self.ui.pushButton.setText("Stop")
            self.ui.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n" + "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")

    def on_every_second(self):
        if self.running:
            self.time = self.time + 1
            if self.time == 3600:
                self.hours = self.hours + 1
                self.time = 0
            timeString = "%02d:%02d" % divmod(self.time, 60)
            timeString = str(self.hours) + ":" + timeString
            self.ui.label.setText(timeString)
        else:
            pass
            
        
    
def main():
    # Again, this is boilerplate, it's going to be the same on
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
