# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secrt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
import pymysql
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1929, 1006)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, -120, 1961, 1231))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 1931, 1081))
        self.label_5.setStyleSheet("background-image: url(:/newPrefix/doctors-with-big-speech-bubble-on-blue-background-medical-internet-consultation-doctor-on-presentati.jpeg);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1220, 560, 481, 61))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(890, 160, 581, 61))
        self.label_8.setStyleSheet("font: 87 28pt \"Arial Black\";\n"
"border-color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.creer = QtWidgets.QPushButton(Form)
        self.creer.setGeometry(QtCore.QRect(1380, 560, 351, 71))
        self.creer.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.creer.setObjectName("creer")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(820, 490, 281, 41))
        self.checkBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.passe = QtWidgets.QLineEdit(Form)
        self.passe.setGeometry(QtCore.QRect(810, 400, 311, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passe.sizePolicy().hasHeightForWidth())
        self.passe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.passe.setFont(font)
        self.passe.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px\n"
"")
        self.passe.setInputMask("")
        self.passe.setText("")
        self.passe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passe.setObjectName("passe")
        self.nom = QtWidgets.QLineEdit(Form)
        self.nom.setGeometry(QtCore.QRect(810, 310, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nom.sizePolicy().hasHeightForWidth())
        self.nom.setSizePolicy(sizePolicy)
        self.nom.setStyleSheet("border :none;\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"padding-bottom:7px\n"
"")
        self.nom.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nom.setInputMask("")
        self.nom.setText("")
        self.nom.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nom.setDragEnabled(False)
        self.nom.setReadOnly(False)
        self.nom.setObjectName("nom")
        self.connecter = QtWidgets.QPushButton(Form)
        self.connecter.setGeometry(QtCore.QRect(790, 570, 351, 61))
        self.connecter.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);")
        self.connecter.setObjectName("connecter")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(810, 680, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><img src=\"doctors-with-big-speech-bubble-on-blue-background-medical-internet-consultation-doctor-on-presentati.jpeg\"/></p></body></html>"))
        self.label_6.setText(_translate("Form", "Ou"))
        self.label_8.setText(_translate("Form", "Connexion Sécretaire"))
        self.creer.setText(_translate("Form", "Créer un compte"))
        self.checkBox_2.setText(_translate("Form", "Garder ma session active"))
        self.passe.setPlaceholderText(_translate("Form", "Mot de passe"))
        self.nom.setPlaceholderText(_translate("Form", "Email"))
        self.connecter.setText(_translate("Form", "Connecter"))
        self.pushButton.setText(_translate("Form", "Mot de Passe oublié ?"))

        self.connecter.clicked.connect(self.connect_medecin)
        self.pushButton.clicked.connect(self.reset_password)

    def connect_medecin(self):
            email = self.nom.text()
            password = self.passe.text()

            mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="texthear"
        )
            mycursor = mydb.cursor()

            query = "SELECT * FROM secretaires WHERE email = %s AND password = %s"
            values = (email, password)
            mycursor.execute(query, values)

            result = mycursor.fetchone()

            if result:
                os.system('python mainh.py')
                messageBox=QMessageBox()
                messageBox.setText("Connexion réussie")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec()
            #
            # QMessageBox.information(self, "Connexion réussie", "Vous êtes connecté en tant que médecin")
            
            else:
                messageBox=QMessageBox()
                messageBox.setText("Erreur de connexion  ,Email ou mot de passe incorrect")
                messageBox.setStandardButtons(QMessageBox.Ok)
                messageBox.exec()

            

    def reset_password(self):
        email = self.nom.text()

        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="texthear"
        )

        mycursor = mydb.cursor()

        query = "SELECT * FROM secretaires WHERE email = %s"
        values = (email,)
        mycursor.execute(query, values)

        result = mycursor.fetchone()

        if result:
            # Envoyer un email pour réinitialiser le mot de passe
            messageBox=QMessageBox()
            messageBox.setText("Mot de passe oublié , Un email de réinitialisation a été envoyé à votre adresse")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            
        else:
            messageBox=QMessageBox()
            messageBox.setText("Erreur , Aucun compte trouvé avec cet email")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()



import l_rc




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    sec= Ui_Form()
    sec.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
