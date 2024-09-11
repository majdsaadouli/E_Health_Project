from PyQt5 import QtCore, QtGui, QtWidgets
from medecin import Ui_MainWindow
from fiche import Ui_Form
from patientf  import Patient
from donnesper import donnes
import sys

def affichefiche():
    Form.show()

def affiche_patient():
    Form4.show()

def affiche_donnes():
    Form3.show()



## importation et affichage de l'interface medecin##
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.button_fiche.clicked.connect(affichefiche)
ui.button_patient.clicked.connect(affiche_patient)
ui.butt_monprofil.clicked.connect(affiche_donnes)




### importation de l'interface fiche##
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

### importation et affichage de l'interface patient##
Form4 = QtWidgets.QWidget()
ui4 =Patient()
ui4.setupUi(Form4)

###importation de l'interface donnes###
Form3 = QtWidgets.QWidget()
ui3 = donnes()
ui3.setupUi(Form3)





MainWindow.show()
sys.exit(app.exec_())