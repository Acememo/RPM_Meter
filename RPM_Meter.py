# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPM_Meter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import _thread

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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPM Meter"))
        self.rpmValue.setText(_translate("MainWindow", "TextLabel"))
        self.text_line.setText(_translate("MainWindow", "RPM"))
    
    def updateLabel(self):
        global rpm
        try:            
            while(1):
                self.rpmValue.setText(str(rpm))
                time.sleep(1)
        except KeyboardInterrupt:
            print('Update Thread ended by Keyboard command')
        except Exception as e:
            print(str(e))
        
    def readRPM(self):
        from gpiozero import Button
        global rpm
        try:
            ## inicializacion
            deltaT = 0
            enSlots = 20
            inPIN = 4
            oldT = time.time()        
            pinB = Button(inPIN)
            while(1):
                Button.wait_for_press(pinB)
                deltaT = time.time() - oldT
                oldT = time.time()
                rpm = 60 / ( deltaT * enSlots )
                Button.wait_for_release(pinB)
        except KeyboardInterrupt:
            print('Read Thread ended by Keyboard command')
        except Exception as e:
            print(str(e))

                                

if __name__ == "__main__":
    import sys
    global rpm
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    _thread.start_new_thread(ui.readRPM,())
    _thread.start_new_thread(ui.updateLabel,())
    MainWindow.show()
    sys.exit(app.exec_())
