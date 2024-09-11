# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fiche.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableView
from PyQt5.QtSql import QSqlTableModel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1424, 870)
        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1461, 881))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.back = QtWidgets.QLabel(self.frame)
        self.back.setGeometry(QtCore.QRect(10, -10, 1491, 911))
        self.back.setText("")
        self.back.setPixmap(QtGui.QPixmap("fiche2.jpg"))
        self.back.setScaledContents(True)
        self.back.setObjectName("back")
        self.frame_coordo = QtWidgets.QFrame(self.frame)
        self.frame_coordo.setGeometry(QtCore.QRect(479, 99, 131, 261))
        self.frame_coordo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_coordo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_coordo.setObjectName("frame_coordo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_coordo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.id_pat = QtWidgets.QLabel(self.frame_coordo)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.id_pat.setFont(font)
        self.id_pat.setStyleSheet("")
        self.id_pat.setTextFormat(QtCore.Qt.PlainText)
        self.id_pat.setObjectName("id_pat")
        self.verticalLayout.addWidget(self.id_pat)
        self.diagnostic = QtWidgets.QLabel(self.frame_coordo)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diagnostic.setFont(font)
        self.diagnostic.setStyleSheet("")
        self.diagnostic.setObjectName("diagnostic")
        self.verticalLayout.addWidget(self.diagnostic)
        self.traitements = QtWidgets.QLabel(self.frame_coordo)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.traitements.setFont(font)
        self.traitements.setStyleSheet("")
        self.traitements.setObjectName("traitements")
        self.verticalLayout.addWidget(self.traitements)
        self.zone_texte = QtWidgets.QFrame(self.frame)
        self.zone_texte.setGeometry(QtCore.QRect(609, 99, 481, 261))
        self.zone_texte.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.zone_texte.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zone_texte.setObjectName("zone_texte")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.zone_texte)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.zone_texte)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.textEdit_3 = QtWidgets.QTextEdit(self.zone_texte)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_2.addWidget(self.textEdit_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.zone_texte)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.frame_bout = QtWidgets.QFrame(self.frame)
        self.frame_bout.setGeometry(QtCore.QRect(780, 360, 311, 81))
        self.frame_bout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bout.setObjectName("frame_bout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_bout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_bout)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(170,255,255);\n"
"font:  10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(238,213,210);\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"font:  10pt \"MS Shell Dlg 2\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("butt_recherche")
        ###evenement bouton rechercher##
        self.pushButton.clicked.connect(self.rechercher_patient)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_bout)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(170,255,255);\n"
"font:  10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(238,213,210);\n"
"border-top-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"font:  10pt \"MS Shell Dlg 2\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("butt_enregistrer")
        ####evenement du bouton enregister####
        self.pushButton_2.clicked.connect(self.enregistrer)
        self.pushButton_2.clicked.connect(self.afficher_patients)
        ###############
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(479, 446, 621, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 619, 399))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar.setGeometry(QtCore.QRect(600, 0, 16, 391))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 380, 601, 16))
        self.horizontalScrollBar.setStyleSheet("")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget.setGeometry(QtCore.QRect(-5, 1, 601, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.id_pat.setText(_translate("Form", "ID PATIENT:"))
        self.diagnostic.setText(_translate("Form", "DIAGNOSTIC:"))
        self.traitements.setText(_translate("Form", "TRAITEMENTS:"))
        self.pushButton.setText(_translate("Form", "RECHERCHER"))
        self.pushButton_2.setText(_translate("Form", "ENREGISTRER"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID_DIAG"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID_PATIENT"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "DIAGNOSTIC"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "TRAITEMENTS"))
    
    
    def enregistrer(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="fichemedicale")
        curseur = con.cursor()
        curseur.execute("insert into fiche(ID_PATIENT,DIAGNOSTIC,TRAITEMENTS) values (%s,%s,%s)",(
            self.textEdit.toPlainText(), ##recuperation de valeur de textedit####
            self.textEdit_3.toPlainText(),
            self.textEdit_2.toPlainText()))
        con.commit()
        con.close()
        msg = QMessageBox()
        msg.setText("Diagnostic enregistré")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def afficher_patients(self):
         ###connexion 
         con = mysql.connector.connect(host="localhost", user="root", password="", database="fichemedicale")
        # Créer un curseur pour exécuter des requêtes SQL
         mycursor = con.cursor()

        # Exécuter la requête SQL pour récupérer tous les patients
         mycursor.execute("SELECT * FROM fiche ")

        # Récupérer les résultats de la requête
         result = mycursor.fetchall()

        # Afficher les résultats dans le tableWidget
         self.tableWidget.setRowCount(0)
         for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    def rechercher_patient(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="fichemedicale")
        cursor = con.cursor()

         #Récupérer les informations de recherche du patient à partir de l'interface utilisateur
        id = self.textEdit.toPlainText()  # Récupérer l'ID du secrétaire depuis l'interface
        query = f"SELECT * FROM fiche WHERE ID_PATIENT = {id}"  # Créer la requête SQL pour récupérer les informations du secrétaire
        cursor.execute(query)  # Exécuter la requête SQL
        result = cursor.fetchall()  # Récupérer le résultat de la requête

        if result: # si le résultat de la requête n'est pas vide
            # afficher les informations du secrétaire sur les labels
            
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        
        else: # si le résultat de la requête est vide
            messageBox = QMessageBox()
            messageBox.setText("Aucun patient trouvé.")
            messageBox.setStandardButtons(QMessageBox.Ok)
            messageBox.exec()

        


    
    




        
        








import resource_fiche_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
