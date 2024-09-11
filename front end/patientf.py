# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_pat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
import re
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Patient(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1114, 822)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head = QtWidgets.QFrame(Form)
        self.head.setMinimumSize(QtCore.QSize(100, 200))
        self.head.setStyleSheet("background-color: rgb(230, 231, 233);")
        self.head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.head)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image = QtWidgets.QFrame(self.head)
        self.image.setEnabled(True)
        self.image.setMinimumSize(QtCore.QSize(200, 0))
        self.image.setTabletTracking(False)
        self.image.setStyleSheet("image: url(:/newPrefix/4200528.png);")
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.horizontalLayout_2.addWidget(self.image)
        self.recherche_patient = QtWidgets.QFrame(self.head)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recherche_patient.sizePolicy().hasHeightForWidth())
        self.recherche_patient.setSizePolicy(sizePolicy)
        self.recherche_patient.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recherche_patient.setFrameShadow(QtWidgets.QFrame.Raised)
        self.recherche_patient.setObjectName("recherche_patient")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.recherche_patient)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titre = QtWidgets.QFrame(self.recherche_patient)
        self.titre.setMinimumSize(QtCore.QSize(0, 50))
        self.titre.setSizeIncrement(QtCore.QSize(50, 50))
        self.titre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titre.setObjectName("titre")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.titre)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nom = QtWidgets.QLabel(self.titre)
        self.nom.setStyleSheet("font: 25 20pt \"Bookman Old Style\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 178, 238);")
        self.nom.setObjectName("nom")
        self.verticalLayout_3.addWidget(self.nom, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.titre, 0, QtCore.Qt.AlignTop)
        self.ajout_recher = QtWidgets.QFrame(self.recherche_patient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ajout_recher.sizePolicy().hasHeightForWidth())
        self.ajout_recher.setSizePolicy(sizePolicy)
        self.ajout_recher.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ajout_recher.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ajout_recher.setObjectName("ajout_recher")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.ajout_recher)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.ajout_recher)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.prenom_edit = QtWidgets.QLineEdit(self.frame)
        self.prenom_edit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.prenom_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.prenom_edit.setObjectName("prenom_edit")
        self.gridLayout_2.addWidget(self.prenom_edit, 3, 0, 1, 1)
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);\n"
"")
        self.date.setObjectName("date")
        self.gridLayout_2.addWidget(self.date, 4, 0, 1, 1)
        self.recherche = QtWidgets.QPushButton(self.frame)
        self.recherche.setStyleSheet("\n"
"color: rgb(0, 178, 238);\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/875623.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recherche.setIcon(icon)
        self.recherche.setIconSize(QtCore.QSize(30, 30))
        self.recherche.setObjectName("recherche")
        self.gridLayout_2.addWidget(self.recherche, 6, 1, 1, 1)
        self.prenom = QtWidgets.QLabel(self.frame)
        self.prenom.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);\n"
"")
        self.prenom.setObjectName("prenom")
        self.gridLayout_2.addWidget(self.prenom, 2, 0, 1, 1)
        self.nom_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.nom_2.sizePolicy().hasHeightForWidth())
        self.nom_2.setSizePolicy(sizePolicy)
        self.nom_2.setMinimumSize(QtCore.QSize(0, 20))
        self.nom_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.nom_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.nom_2.setObjectName("nom_2")
        self.gridLayout_2.addWidget(self.nom_2, 0, 0, 1, 1)
        self.nom_edit = QtWidgets.QLineEdit(self.frame)
        self.nom_edit.setMaximumSize(QtCore.QSize(200, 16777215)) 
        self.nom_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nom_edit.setObjectName("nom_edit")
        self.gridLayout_2.addWidget(self.nom_edit, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 5, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame)
        self.btn_ajout = QtWidgets.QFrame(self.ajout_recher)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ajout.sizePolicy().hasHeightForWidth())
        self.btn_ajout.setSizePolicy(sizePolicy)
        self.btn_ajout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_ajout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_ajout.setObjectName("btn_ajout")
        self.gridLayout = QtWidgets.QGridLayout(self.btn_ajout)
        self.gridLayout.setObjectName("gridLayout")
        self.email = QtWidgets.QLabel(self.btn_ajout)
        self.email.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 4, 0, 1, 1)
        self.ville_Edit_6 = QtWidgets.QLineEdit(self.btn_ajout)
        self.ville_Edit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ville_Edit_6.setObjectName("ville_Edit_6")
        self.gridLayout.addWidget(self.ville_Edit_6, 5, 2, 1, 1)
        self.mail_Edit_3 = QtWidgets.QLineEdit(self.btn_ajout)
        self.mail_Edit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mail_Edit_3.setObjectName("mail_Edit_3")
        self.gridLayout.addWidget(self.mail_Edit_3, 5, 0, 1, 1)
        self.PRENOM = QtWidgets.QLabel(self.btn_ajout)
        self.PRENOM.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.PRENOM.setObjectName("PRENOM")
        self.gridLayout.addWidget(self.PRENOM, 0, 1, 1, 2)
        self.nomEdit = QtWidgets.QLineEdit(self.btn_ajout)
        self.nomEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nomEdit.setObjectName("nomEdit")
        self.gridLayout.addWidget(self.nomEdit, 1, 0, 1, 1)
        self.telephone = QtWidgets.QLabel(self.btn_ajout)
        self.telephone.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.telephone.setObjectName("telephone")
        self.gridLayout.addWidget(self.telephone, 2, 2, 1, 1)
        self.ville = QtWidgets.QLabel(self.btn_ajout)
        self.ville.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.ville.setObjectName("ville")
        self.gridLayout.addWidget(self.ville, 4, 2, 1, 1)
        self.prenom_Edit_4 = QtWidgets.QLineEdit(self.btn_ajout)
        self.prenom_Edit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prenom_Edit_4.setObjectName("prenom_Edit_4")
        self.gridLayout.addWidget(self.prenom_Edit_4, 1, 2, 1, 1)
        self.date_2 = QtWidgets.QLabel(self.btn_ajout)
        self.date_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.date_2.setObjectName("date_2")
        self.gridLayout.addWidget(self.date_2, 2, 0, 1, 1)
        self.tel_Edit_5 = QtWidgets.QLineEdit(self.btn_ajout)
        self.tel_Edit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tel_Edit_5.setObjectName("tel_Edit_5")
        self.gridLayout.addWidget(self.tel_Edit_5, 3, 2, 1, 1)
        self.nom_3 = QtWidgets.QLabel(self.btn_ajout)
        self.nom_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 178, 238);")
        self.nom_3.setObjectName("nom_3")
        self.gridLayout.addWidget(self.nom_3, 0, 0, 1, 1)
        self.btn_ajout_2 = QtWidgets.QPushButton(self.btn_ajout)
        self.btn_ajout_2.setStyleSheet("\n"
"color: rgb(0, 178, 238);\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/1057240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ajout_2.setIcon(icon1)
        self.btn_ajout_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_ajout_2.setObjectName("btn_ajout_2")
        self.gridLayout.addWidget(self.btn_ajout_2, 6, 2, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.btn_ajout)
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 3, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.btn_ajout)
        self.verticalLayout_2.addWidget(self.ajout_recher)
        self.horizontalLayout_2.addWidget(self.recherche_patient)
        self.verticalLayout.addWidget(self.head)
        self.liste = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liste.sizePolicy().hasHeightForWidth())
        self.liste.setSizePolicy(sizePolicy)
        self.liste.setMinimumSize(QtCore.QSize(500, 500))
        self.liste.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.liste.setFrameShadow(QtWidgets.QFrame.Raised)
        self.liste.setObjectName("liste")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.liste)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableau = QtWidgets.QFrame(self.liste)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableau.sizePolicy().hasHeightForWidth())
        self.tableau.setSizePolicy(sizePolicy)
        self.tableau.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableau.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableau.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableau.setObjectName("tableau")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tableau)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.tableau)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.image_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_2.sizePolicy().hasHeightForWidth())
        self.image_2.setSizePolicy(sizePolicy)
        self.image_2.setMinimumSize(QtCore.QSize(300, 200))
        self.image_2.setStyleSheet("border-image: url(:/newPrefix/84e0b185d97c8d913ffcd3188c2c90fe.jpg);")
        self.image_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_2.setObjectName("image_2")
       
        self.horizontalLayout_4.addWidget(self.image_2)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout.addWidget(self.tableau)
        self.verticalLayout.addWidget(self.liste)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        #connexion avec base de données 


        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donnespatient"
        ) 



    def ajouter_patient(self):
        # Récupérer les informations du patient à partir de l'interface utilisateur
        nom = self.nomEdit.text()
        prenom = self.prenom_Edit_4.text()
        email = self.mail_Edit_3.text()
        date_naissance = self.dateEdit_2.date().toString("yyyy-MM-dd")
        ville = self.ville_Edit_6.text()
        telephone = self.tel_Edit_5.text()

        # Vérifier que le nom et le prénom ne contiennent pas de chiffres
        if re.search(r'\d', nom) or re.search(r'\d', prenom):
            self.message_label.setText("Le nom et le prénom ne doivent pas contenir de chiffres.")
            messageBox = QMessageBox()
            messageBox.setText("Le nom et le prénom ne doivent pas contenir de chiffres.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Vérifier que l'email est valide
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            #self.message_label.setText("L'email n'est pas valide.")
            messageBox = QMessageBox()
            messageBox.setText("L'email n'est pas valide")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        # Vérifier que le numéro de téléphone a 8 chiffres
        if not re.match(r'^\d{8}$', telephone):
            #self.message_label.setText("Le numéro de téléphone doit contenir 8 chiffres.")
            messageBox = QMessageBox()
            messageBox.setText("Le numéro de téléphone doit contenir 8 chiffres")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            return

        
        

        # Créer un curseur pour exécuter des requêtes SQL
        mycursor = self.db.cursor()
         #Vérifier si le patient existe déjà
        sql = "SELECT * FROM patient WHERE nom=%s AND prenom=%s AND date_naissance=%s"
        values = (nom, prenom, date_naissance)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        if result is not None:
            # Le patient existe déjà, afficher un message d'erreur
            messageBox = QMessageBox()
            messageBox.setText("Ce patient existe déjàs")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()
            
            return

        # Exécuter la requête SQL pour ajouter le patient à la base de données
        sql = "INSERT INTO patient (nom, prenom, email, date_naissance, ville, telephone) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, email, date_naissance, ville, telephone)
        mycursor.execute(sql, values)
        self.db.commit()

        # Afficher un message de confirmation
        messageBox = QMessageBox()
        messageBox.setText("Le patient a été ajouté avec succès")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()
        #self.message_label.setText("Le patient a été ajouté avec succès.")

    def afficher_patients(self):
        # Créer un curseur pour exécuter des requêtes SQL
         mycursor = self.db.cursor()

        # Exécuter la requête SQL pour récupérer tous les patients
         mycursor.execute("SELECT * FROM patient ")

        # Récupérer les résultats de la requête
         result = mycursor.fetchall()

        # Afficher les résultats dans le tableWidget
         self.tableWidget.setRowCount(0)
         for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
    
    def rechercher_patient(self):
         #Récupérer les informations de recherche du patient à partir de l'interface utilisateur
        nom = self.nom_edit.text()
        prenom = self.prenom_edit.text()
        date_naissance = self.dateEdit.date().toString("yyyy-MM-dd")

        # Se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="donnespatient"
        )

        # Créer un curseur pour exécuter des requêtes SQL
        mycursor = mydb.cursor()

        # Exécuter la requête SQL pour rechercher les patients correspondants à la recherche
        sql = "SELECT * FROM patient WHERE nom=%s AND prenom=%s AND date_naissance=%s"
        values = (nom, prenom, date_naissance)
        mycursor.execute(sql, values)
        result = mycursor.fetchall()

        # Afficher les résultats dans le tableWidget
        if result:

                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
                # Afficher un message 
                 messageBox = QMessageBox()
                 messageBox.setText("Aucun patient trouvé.")
                 messageBox.setStandardButtons(QMessageBox.Ok)
                 messageBox.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nom.setText(_translate("Form", "LISTE DES PATIENTS"))
        self.date.setText(_translate("Form", "DATE DE NAISSANCE"))
        self.recherche.setText(_translate("Form", "Recherche"))
        self.prenom.setText(_translate("Form", "PRENOM"))
        self.nom_2.setText(_translate("Form", "NOM"))
        self.email.setText(_translate("Form", "email"))
        self.PRENOM.setText(_translate("Form", "PRENOM"))
        self.telephone.setText(_translate("Form", "telephone"))
        self.ville.setText(_translate("Form", "ville"))
        self.date_2.setText(_translate("Form", "DATE DE NAISSANCE"))
        self.nom_3.setText(_translate("Form", "NOM"))
        self.btn_ajout_2.setText(_translate("Form", "Ajouter "))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "NOM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "PRENOM"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Telephone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Ville"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "DATE DE NAISSANCE"))
        self.btn_ajout_2.clicked.connect(self.ajouter_patient)
        self.btn_ajout_2.clicked.connect(self.afficher_patients)
        self.recherche.clicked.connect(self.rechercher_patient)

import icon_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form4 = QtWidgets.QWidget()
    ui4 = Patient()
    ui4.setupUi(Form4)
    Form4.show()
    sys.exit(app.exec_())
