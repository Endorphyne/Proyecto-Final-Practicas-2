import sys
from PyQt5 import QtWidgets, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setStyleSheet("background-color: #232743;")  # Fondo general

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setContentsMargins(50, 50, 50, 50)
        self.formLayout.setSpacing(20)

        # Etiqueta Usuario
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setObjectName("label_usuario")
        self.label_usuario.setStyleSheet("color: #D8DBE2; font-size: 14px;")  # Detalles
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_usuario)

        # Campo de texto Usuario
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_usuario.setPlaceholderText("Ingrese su usuario")
        self.lineEdit_usuario.setStyleSheet("""
            background-color: #D8DBE2;  /* Fondo específico */
            color: #232743;  /* Fondo general */
            padding: 5px;
            border: 2px solid #797979;  /* Detalles */
            border-radius: 2.5px;
        """)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_usuario)

        # Etiqueta Contraseña
        self.label_contrasena = QtWidgets.QLabel(self.centralwidget)
        self.label_contrasena.setObjectName("label_contrasena")
        self.label_contrasena.setStyleSheet("color: #D8DBE2; font-size: 14px;")  # Detalles
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_contrasena)

        # Campo de texto Contraseña
        self.lineEdit_contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")
        self.lineEdit_contrasena.setPlaceholderText("Ingrese su contraseña")
        self.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_contrasena.setStyleSheet("""
            background-color: #D8DBE2;  /* Fondo específico */
            color: #232743;  /* Fondo general */
            padding: 5px;
            border: 2px solid #797979;  /* Detalles */
            border-radius: 2.5px;
        """)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_contrasena)

        # Botón de inicio de sesión
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #5E7CE2;  /* Botones */
                color: #ECEFF4; 
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
        """)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.ok_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio de Sesión"))
        self.label_usuario.setText(_translate("MainWindow", "Usuario:"))
        self.label_contrasena.setText(_translate("MainWindow", "Contraseña:"))
        self.ok_btn.setText(_translate("MainWindow", "Ok"))