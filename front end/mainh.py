from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from menu import Ui_MainWindow
from patientf import Patient as patientDialog
from profil import Ui_MainWindow as profilDialog 
from calendrier import Ui_Form as calendrierDialog
import sys
#slots 
def profil_afficher():
    profil.show()

def patient_afficher():
    patient.show()
def calendrier_afficher():
    calendrier.show()
def deconnexion():
    import os
    os.system('python mainprincipale.py')

#fenetre principale
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#creation de la boite profil 
profil = QtWidgets.QMainWindow()
uiprofil = profilDialog()
uiprofil.setupUi(profil)

#Création de la boite de dialogue calendrier
calendrier = QtWidgets.QWidget()
uicalendrier = calendrierDialog()
uicalendrier.setupUi(calendrier)

#Création de la boite de dialogue patient 
patient = QtWidgets.QWidget()
uipatient = patientDialog()
uipatient.setupUi(patient)

MainWindow.show()
#les bouttons clickés
ui.profil.clicked.connect(lambda:profil_afficher())
ui.profil_2.clicked.connect(lambda:profil_afficher())
ui.calendrier.clicked.connect(lambda:calendrier_afficher())
ui.profil.clicked.connect(lambda:profil_afficher())
ui.patient.clicked.connect(lambda:patient_afficher())
ui.exit.clicked.connect(deconnexion)
#cross
ui.cross.clicked.connect(lambda: exit())
sys.exit(app.exec_())