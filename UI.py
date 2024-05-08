#from PyQt6 import QtCore, QtGui, QtWidgets
#from PyQt6 import *
#from PyQt6.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
#from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 475)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #####
        self.label_videoframe = QtWidgets.QLabel(self.centralwidget)
        self.label_videoframe.setGeometry(QtCore.QRect(40, 50, 800, 450))##############
        self.label_videoframe.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_videoframe.setText("")
        #####
        self.button_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.button_openfile.setGeometry(QtCore.QRect(380,580, 113, 32))
        self.button_openfile.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_openfile.setObjectName("button_openfile")
        #####
        self.label_framecnt = QtWidgets.QLabel(self.centralwidget)
        self.label_framecnt.setGeometry(QtCore.QRect(700, 495, 171, 21))
        self.label_framecnt.setObjectName("label_framecnt")
        #####
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(380, 520, 113, 32))
        self.button_play.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_play.setObjectName("button_play")
        #####
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(40, 520, 113, 32))
        self.button_stop.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_stop.setObjectName("button_stop")
        #####
        self.label_filepath = QtWidgets.QLabel(self.centralwidget)
        self.label_filepath.setGeometry(QtCore.QRect(40, 790, 841, 41))
        self.label_filepath.setObjectName("label_filepath")
        #####
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setGeometry(QtCore.QRect(700, 520, 113, 32))
        self.button_pause.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "gridline-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_pause.setObjectName("button_pause")
        #####
        self.button_procesar_caras = QtWidgets.QPushButton(self.centralwidget)
        self.button_procesar_caras.setGeometry(QtCore.QRect(700, 580, 113, 32))
        self.button_procesar_caras.setStyleSheet("border-color: rgb(255, 255, 127);\n"
        "background-color: rgb(255, 255, 127);\n"
        "\n"
        "selection-background-color: rgb(255, 255, 172);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";")
        self.button_procesar_caras.setObjectName("button_procesar_caras")

        #self.label_videoframe.setObjectName("label_videoframe")
        self.button_adelantar = QtWidgets.QPushButton(self.centralwidget)
        self.button_adelantar.setGeometry(QtCore.QRect(40, 580, 113, 32))
        self.button_adelantar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_adelantar.setObjectName("button_adelantar")

        
        #####
        self.button_volver_inic = QtWidgets.QPushButton(self.centralwidget)
        self.button_volver_inic.setGeometry(QtCore.QRect(40, 10, 113, 32))
        self.button_volver_inic.setStyleSheet("border-color: rgb(0, 0, 0);\n"
        "border-top-color: rgb(0, 0, 0);\n"
        "border-bottom-color: rgb(0, 0, 0);\n"
        "font: 700 9pt \"Segoe UI\";\n"
        "border-right-color: rgb(0, 0, 0);")
        self.button_volver_inic.setObjectName("button_volver_inic")
        #####
        

        ###################
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reproductor de video"))
        self.button_adelantar.setText(_translate("MainWindow", "Adelantar 10s"))
        self.label_framecnt.setText(_translate("MainWindow", "current_frame/total_frame"))
        self.button_play.setText(_translate("MainWindow", "Play"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.label_filepath.setText(_translate("MainWindow", "file path:"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
        self.button_volver_inic.setText(_translate("MainWindow", "Volver al inicio"))
        self.button_procesar_caras.setText(_translate("MainWindow", "Procesar rostros"))


        self.button_openfile.setText(_translate("MainWindow", "Open file"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())