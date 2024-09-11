#hashlib est un module en python pour stocker des mots de passe de manière sécurisée.  Lorsqu'un utilisateur entre un mot de passe pour se connecter, le hachage du
# mot de passe entré est comparé au hachage stocké dans la base de données pour vérifier si le mot de passe est correct.

import hashlib
# re: module utilisé pour effectuer des opérations de recherche et  la validation de formats de courriel ou de numéros de téléphone...          
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
#sys interagir avec l'interpréteur Python et l'environnement d'exécution
import sys
import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1626, 912)
        Form.setStyleSheet("background-color: rgb(190, 224, 255);\n"
"background-color: rgb(237, 246, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(470, -40, 681, 191))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/plaque-de-porte-standard-en-plexi-secretariat-medical-.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 1221, 111))
        self.label_2.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(156,221, 242);")
        self.label_2.setObjectName("label_2")
        self.nomsec = QtWidgets.QLineEdit(Form)
        self.nomsec.setGeometry(QtCore.QRect(50, 270, 511, 71))
        self.nomsec.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.nomsec.setText("")
        self.nomsec.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nomsec.setObjectName("nomsec")
        self.prenomsec = QtWidgets.QLineEdit(Form)
        self.prenomsec.setGeometry(QtCore.QRect(50, 390, 511, 71))
        self.prenomsec.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.prenomsec.setText("")
        self.prenomsec.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.prenomsec.setObjectName("prenomsec")
        self.ad = QtWidgets.QLineEdit(Form)
        self.ad.setGeometry(QtCore.QRect(60, 490, 511, 71))
        self.ad.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.ad.setText("")
        self.ad.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ad.setObjectName("ad")
        self.tel = QtWidgets.QLineEdit(Form)
        self.tel.setGeometry(QtCore.QRect(50, 620, 511, 71))
        self.tel.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.tel.setText("")
        self.tel.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tel.setObjectName("tel")
        self.rotation = QtWidgets.QLabel(Form)
        self.rotation.setGeometry(QtCore.QRect(70, 740, 251, 51))
        self.rotation.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(121, 121, 121);\n"
"")
        self.rotation.setObjectName("rotation")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(310, 740, 271, 51))
        self.comboBox.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(1100, 230, 941, 521))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/Logo.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 850, 1351, 91))
        self.label_5.setObjectName("label_5")
        self.inscript = QtWidgets.QPushButton(Form)
        self.inscript.setGeometry(QtCore.QRect(700, 790, 451, 71))
        self.inscript.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 170, 0);")
        self.inscript.setObjectName("inscript")
        self.pas = QtWidgets.QLineEdit(Form)
        self.pas.setGeometry(QtCore.QRect(630, 410, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pas.sizePolicy().hasHeightForWidth())
        self.pas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pas.setFont(font)
        self.pas.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px\n"
"")
        self.pas.setInputMask("")
        self.pas.setText("")
        self.pas.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pas.setObjectName("pas")
        self.pass_1 = QtWidgets.QLineEdit(Form)
        self.pass_1.setGeometry(QtCore.QRect(620, 510, 471, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_1.sizePolicy().hasHeightForWidth())
        self.pass_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pass_1.setFont(font)
        self.pass_1.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px\n"
"")
        self.pass_1.setInputMask("")
        self.pass_1.setText("")
        self.pass_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_1.setObjectName("pass_1")
        self.email1 = QtWidgets.QLineEdit(Form)
        self.email1.setGeometry(QtCore.QRect(630, 270, 511, 71))
        self.email1.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.email1.setText("")
        self.email1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email1.setObjectName("email1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Formulaire d\'inscription"))
        self.nomsec.setPlaceholderText(_translate("Form", "Nom"))
        self.prenomsec.setPlaceholderText(_translate("Form", "Prénom"))
        self.ad.setPlaceholderText(_translate("Form", "Adresse"))
        self.tel.setPlaceholderText(_translate("Form", "Numéro de Téléphone"))
        self.rotation.setText(_translate("Form", "Rotation"))
        self.comboBox.setItemText(0, _translate("Form", "Jour"))
        self.comboBox.setItemText(1, _translate("Form", "Nuit"))
        self.label_5.setText(_translate("Form", "Contact\n"
"Pour plus d’informations sur les traitements de vos données vous pouvez contacter le centre informatique  désigné par Ministre de la Santé  à l’adresse électronique suivante : dpo@ministre.org"))
        self.inscript.setText(_translate("Form", "Inscription"))
        self.pas.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.pass_1.setPlaceholderText(_translate("Form", "confirmer votre mot de passe"))
        self.email1.setPlaceholderText(_translate("Form", "Email"))
        self.inscript.clicked.connect(self.inscription_sec)


    def inscription_sec(self):
        
        email = self.email1.text()
        passw= self.pas.text()
        adresse = self.ad.text()
        numero_telephone = self.tel.text()
        rotation = self.comboBox.currentText()
        nom = self.nomsec.text()
        prénom = self.prenomsec.text()
        confirm_password = self.pass_1.text()



        
        # Vérifier que le nom et le prénom ne contiennent pas de chiffres
        if re.search(r'\d', nom) or re.search(r'\d', prénom):
            #self.message_label.setText("Le nom et le prénom ne doivent pas contenir de chiffres.")
            messageBox = QMessageBox()
            messageBox.setText("Le nom et le prénom ne doivent pas contenir de chiffres.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        

        # Vérifier que le numéro de téléphone a 8 chiffres
        if not re.match(r'^\d{8}$', numero_telephone):
            #self.message_label.setText("Le numéro de téléphone doit contenir 8 chiffres.")
            messageBox = QMessageBox()
            messageBox.setText("Le numéro de téléphone doit contenir 8 chiffres")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return


        
        # Vérification de la validité de l'email
        if "@" not in email:
            messageBox = QMessageBox()
            messageBox.setText("Email invalide")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Vérification de la validité du mot de passe
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", passw):
            messageBox = QMessageBox()
            messageBox.setText("Mot de passe invalide. Doit contenir au moins 8 caractères avec au moins une lettre et un chiffre")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Vérification de la correspondance des mots de passe
        if passw != confirm_password:
            messageBox = QMessageBox()
            messageBox.setText("Les mots de passe ne correspondent pas")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Hashage du mot de passe
        #salt = "cigbm" # Chaîne aléatoire ajoutée au mot de passe pour renforcer la sécurité

         # Hachage du mot de passe avec le sel
        #password = hashlib.sha256((passw + salt).encode('utf-8')).hexdigest()
        
        
        

        # Connexion à la base de données
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="texthear"
        )

        mycursor = mydb.cursor()

        # Requête SQL pour insérer les informations d'inscription dans la base de données
        query = "INSERT INTO secretaires (email,password,adresse,numero_telephone,rotation,nom,prénom) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        values = (email,passw,adresse,numero_telephone,rotation,nom,prénom)
        mycursor.execute(query, values)

        # Validation de la transaction et fermeture de la connexion à la base de données
        mydb.commit()
        

        # Affichage d'un message de confirmation d'inscription
        messageBox=QMessageBox()
        messageBox.setText("Inscription réussie")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()




import sec2_rc
import secreta_rc





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    sec= Ui_Form()
    sec.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




