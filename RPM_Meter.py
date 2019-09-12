# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPM_Meter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random
#import RPi.GPIO
import time
#from gpiozero import Button

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 238)
        MainWindow.setMinimumSize(QtCore.QSize(519, 238))
        MainWindow.setMaximumSize(QtCore.QSize(519, 238))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rpmValue = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.rpmValue.setFont(font)
        self.rpmValue.setObjectName("rpmValue")
        self.horizontalLayout.addWidget(self.rpmValue)
        self.text_line = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.text_line.setFont(font)
        self.text_line.setObjectName("text_line")
        self.horizontalLayout.addWidget(self.text_line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(1000) # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.readRPM)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPM Meter"))
        self.rpmValue.setText(_translate("MainWindow", "TextLabel"))
        self.text_line.setText(_translate("MainWindow", "RPM"))

    def initGPIO(self):
        inPIN = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(3, GPIO.IN)
        
    def readRPM(self):
        try:        
            ## inicializacion
            deltaT = 0
            enSlots = 20
            oldT = time.time()        
            pinB = Button(inPIN)
            
            while(1):
                Button.wait_for_press(pinB)
                deltaT = time.time() - oldT
                oldT = time.time()
                rpm = 60 / ( deltaT * enSlots )
                ui.rpmValue.setText(str(rpm))
                Button.wait_for_release(pinB)
        except KeyboardInterrupt:
            print('Interrupcion por teclado')
        finally:
            GPIO.cleanup

                                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.initGPIO()       #GPIO config
    ui.qTimer.start()   #starting timer
    sys.exit(app.exec_())
