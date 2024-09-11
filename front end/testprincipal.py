from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from prin import Ui_Form as accueil
from loginmed import Ui_Form as medlog
from loginsec import Ui_Form as seclog
import sys





## importation de fenetre accueil principale
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
sec= accueil()
sec.setupUi(Form)