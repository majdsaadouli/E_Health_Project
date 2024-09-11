import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from prin import Ui_Form
from loginmed import Ui_Form as medDialog
from inscrimed import Ui_Form as signupDialog2
from inscrisec import Ui_Form as signDialog1
from loginsec import Ui_Form as signDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from patientf  import Patient
#*import main
import sys
#import mainh
class Medecin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Medecin, self).__init__()
        self.ui1 = Ui_Form()
        self.ui1.setupUi(self)
        self.ui1.medecin.clicked.connect(self.connexionmed_afficher)
        self.ui1.secretaire.clicked.connect(self.signup_afficher1)
        


    def connexionmed_afficher(self):
         
        self.connex = QtWidgets.QWidget()
        self.signup = medDialog()
        self.signup.setupUi(self.connex)
        self.signup.compte.clicked.connect(self.sign_afficher)
        #self.signup.connect.clicked.connect(self.affiche_fiche)
        
        self.connex.show() # Affiche la prochaine fenêtre (B)

    #def affiche_fiche(self):
        #main.show()






        
    
    
        

    
    

    
    def sign_afficher(self):
        
        self.sign = QtWidgets.QWidget()
        self.signin = signupDialog2()
        self.signin.setupUi(self.sign)
        self.sign.show() # Affiche la prochaine fenêtre (C)
        


          


    def signup_afficher1(self):
        
        self.sig1 = QtWidgets.QWidget()
        self.signup1 = signDialog()
        self.signup1.setupUi(self.sig1)
        self.signup1.creer.clicked.connect(self.sign_afficher2)
        self.sig1.show() # Affiche la prochaine fenêtre (B1)
    
    

    

    def sign_afficher2(self):
        
        self.sign1 = QtWidgets.QWidget()
        self.signin1 = signDialog1()
        self.signin1.setupUi(self.sign1)
        self.sign1.show() # Affiche la prochaine fenêtre (C1)

     
       







if __name__ == "__main__":
    #QtWidgets.QApplication class is used to create a new GUI application
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Medecin()
    MainWindow.show() # Affiche la fenêtre principale (A)
    sys.exit(app.exec_())

#la méthode app.exec_() est appelée pour démarrer la boucle d'événements de l'application graphique.
