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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1719, 967)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 1221, 111))
        self.label_2.setStyleSheet("font: 48pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(50, 88, 172);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, -20, 901, 141))
        self.label_3.setStyleSheet("font: 63 22pt \"Yu Gothic UI Semibold\";\n"
"text-decoration: underline;\n"
"font: 63 22pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(72, 115, 148);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 90, 561, 51))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.specialite = QtWidgets.QLabel(Form)
        self.specialite.setGeometry(QtCore.QRect(700, 330, 391, 41))
        self.specialite.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
"color: rgb(152, 147, 148);")
        self.specialite.setObjectName("specialite")
        self.spec = QtWidgets.QComboBox(Form)
        self.spec.setGeometry(QtCore.QRect(940, 320, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spec.setFont(font)
        self.spec.setObjectName("spec")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.spec.addItem("")
        self.inscri = QtWidgets.QPushButton(Form)
        self.inscri.setGeometry(QtCore.QRect(450, 820, 451, 71))
        self.inscri.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.inscri.setObjectName("inscri")
        self.nommed = QtWidgets.QLineEdit(Form)
        self.nommed.setGeometry(QtCore.QRect(90, 310, 511, 71))
        self.nommed.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.nommed.setText("")
        self.nommed.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nommed.setObjectName("nommed")
        self.pre = QtWidgets.QLineEdit(Form)
        self.pre.setGeometry(QtCore.QRect(90, 410, 491, 71))
        self.pre.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.pre.setText("")
        self.pre.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pre.setObjectName("pre")
        self.add = QtWidgets.QLineEdit(Form)
        self.add.setGeometry(QtCore.QRect(90, 520, 401, 71))
        self.add.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.add.setText("")
        self.add.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.add.setObjectName("add")
        self.num = QtWidgets.QLineEdit(Form)
        self.num.setGeometry(QtCore.QRect(80, 660, 401, 71))
        self.num.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.num.setText("")
        self.num.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.num.setObjectName("num")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 900, 1691, 71))
        self.textEdit.setObjectName("textEdit")
        self.email = QtWidgets.QLineEdit(Form)
        self.email.setGeometry(QtCore.QRect(720, 410, 511, 71))
        self.email.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.email.setText("")
        self.email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email.setObjectName("email")
        self.mpasse = QtWidgets.QLineEdit(Form)
        self.mpasse.setGeometry(QtCore.QRect(720, 510, 511, 71))
        self.mpasse.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.mpasse.setText("")
        self.mpasse.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mpasse.setObjectName("mpasse")
        self.pass2 = QtWidgets.QLineEdit(Form)
        self.pass2.setGeometry(QtCore.QRect(720, 620, 511, 71))
        self.pass2.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 0,0);\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px")
        self.pass2.setText("")
        self.pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2.setObjectName("pass2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(1120, -20, 581, 821))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("a949410303d3bd4f744ae6a94bdb0c64140100a9.png"))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(90, 770, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 770, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Formulaire d\'inscription"))
        self.label_3.setText(_translate("Form", "Ordre    National    Des    Médecins"))
        self.label_4.setText(_translate("Form", "Conseil départemental de l\'Ordre des Médecins"))
        self.specialite.setText(_translate("Form", "Spécialité :"))
        self.spec.setItemText(0, _translate("Form", "L’anesthésiologie"))
        self.spec.setItemText(1, _translate("Form", "La chirurgie"))
        self.spec.setItemText(2, _translate("Form", "La cardiologie"))
        self.spec.setItemText(3, _translate("Form", "L’andrologie"))
        self.spec.setItemText(4, _translate("Form", "La dermatologie"))
        self.spec.setItemText(5, _translate("Form", "L’endocrinologie"))
        self.spec.setItemText(6, _translate("Form", "La gastro-entérologie"))
        self.spec.setItemText(7, _translate("Form", "La gériatrie"))
        self.spec.setItemText(8, _translate("Form", "La gynécologie"))
        self.spec.setItemText(9, _translate("Form", "L’hématologie"))
        self.spec.setItemText(10, _translate("Form", "L’hépatologie"))
        self.spec.setItemText(11, _translate("Form", "L’infectiologie"))
        self.spec.setItemText(12, _translate("Form", "La médecine du travail"))
        self.spec.setItemText(13, _translate("Form", "La médecine générale"))
        self.spec.setItemText(14, _translate("Form", "La médecine interne"))
        self.spec.setItemText(15, _translate("Form", "La médecine palliative"))
        self.spec.setItemText(16, _translate("Form", "La néonatologie"))
        self.spec.setItemText(17, _translate("Form", "La néphrologie"))
        self.spec.setItemText(18, _translate("Form", "La neurologie"))
        self.spec.setItemText(19, _translate("Form", "L’odontologie"))
        self.spec.setItemText(20, _translate("Form", "L’oncologie"))
        self.spec.setItemText(21, _translate("Form", "L’ophtalmologie"))
        self.spec.setItemText(22, _translate("Form", "L’orthopédie"))
        self.spec.setItemText(23, _translate("Form", "La pédiatrie"))
        self.spec.setItemText(24, _translate("Form", "La psychiatrie"))
        self.spec.setItemText(25, _translate("Form", "La radiologie"))
        self.spec.setItemText(26, _translate("Form", "La rhumatologie"))
        self.spec.setItemText(27, _translate("Form", "L’urologie"))
        self.inscri.setText(_translate("Form", "Inscription"))
        self.nommed.setPlaceholderText(_translate("Form", "Nom"))
        self.pre.setPlaceholderText(_translate("Form", "Prénom"))
        self.add.setPlaceholderText(_translate("Form", "Adresse"))
        self.num.setPlaceholderText(_translate("Form", "Numéro de Téléphone"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Les informations recueillies font l’objet d’un traitement informatique. Ces informations sont destinées au Conseil de l’Ordre des médecins et au répertoire partagé des professionnels intervenant dans le système de santé (RPPS)1 . Le responsable de ce traitement est le Secrétaire général du Conseil national de l’Ordre des médecins. Conformément à la loi « informatique et libertés » du 6 janvier 1978 modifiée, vous bénéficiez d’un droit d’accès et de rectification aux informations qui vous concernent.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.email.setPlaceholderText(_translate("Form", "Email"))
        self.mpasse.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.pass2.setPlaceholderText(_translate("Form", "Confirmer votre Mot de passe"))
        self.radioButton.setText(_translate("Form", "Femme"))
        self.radioButton_2.setText(_translate("Form", "Homme"))
        self.inscri.clicked.connect(self.inscription_med)


    def inscription_med(self):
        
        email = self.email.text()
        passw1= self.mpasse.text()
        adresse = self.add.text()
        numero_telephone = self.num.text()
        sexe = "Femme" if self.radioButton.isChecked() else "Homme"
        specialite = self.spec.currentText()
       
        nom = self.nommed.text()
        prénom = self.pre.text()
        confirm_password = self.pass2.text()


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
        

        # re.match() est une méthode  de  re utilisée pour rechercher un motif au début d'une chaîne. 
        # Vérification de la validité du mot de passe
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", passw1):
            messageBox = QMessageBox()
            messageBox.setText("Mot de passe invalide. Doit contenir au moins 8 caractères avec au moins une lettre et un chiffre")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Vérification de la correspondance des mots de passe
        if passw1 != confirm_password:
            messageBox = QMessageBox()
            messageBox.setText("Les mots de passe ne correspondent pas")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Hashage du mot de passe
        
         # Hachage du mot de passe avec le sel
        #password = hashlib.sha256((passw1 ).encode('utf-8')).hexdigest()
        
        #hashlib est utilisé pour calculer le hachage SHA-256 d'une chaîne  : un mot de passe (passw1) et une valeur salt.
#La fonction sha256() du module hashlib est appelée avec la chaîne concaténée en entrée. 
# La méthode encode('utf-8') est utilisée 
# pour convertir la chaîne en un objet bytes en utilisant le codage UTF-8, qui est requis par la fonction hashlib.
# L'objet d'octets résultant est ensuite haché à l'aide de SHA-256, et la méthode hexdigest() est appelée sur l'objet de hachage 
# résultant pour obtenir une représentation sous forme de chaîne hexadécimale du hachage.

        

        # Connexion à la base de données
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="texthear"
        )

        mycursor = mydb.cursor()

        # Requête SQL pour insérer les informations d'inscription dans la base de données
        query = "INSERT INTO medecin (email,password,nom,prénom,adresse,numero_telephone,specialite,sexe) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
        values = (email,passw1,nom,prénom,adresse,numero_telephone,specialite,sexe)
        mycursor.execute(query, values)

        # Validation de la transaction et fermeture de la connexion à la base de données
        mydb.commit()
        

        # Affichage d'un message de confirmation d'inscription
        messageBox=QMessageBox()
        messageBox.setText("Inscription réussie")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
            






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    sec= Ui_Form()
    sec.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())




import r_rc
