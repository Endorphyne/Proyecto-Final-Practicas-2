# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro_ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_registro(object):
    def setupUi(self, ventana_registro):
        ventana_registro.setObjectName("ventana_registro")
        ventana_registro.setWindowModality(QtCore.Qt.NonModal)
        ventana_registro.resize(525, 247)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventana_registro.sizePolicy().hasHeightForWidth())
        ventana_registro.setSizePolicy(sizePolicy)
        ventana_registro.setMaximumSize(QtCore.QSize(525, 247))
        self.centralwidget = QtWidgets.QWidget(ventana_registro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(525, 247))
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 190, 231, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancelar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.btn_confirmar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.horizontalLayout.addWidget(self.btn_confirmar)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 10, 404, 175))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("font: 14pt \"Calibri\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line_usuario = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_usuario.setObjectName("line_usuario")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_usuario)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.line_correo = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_correo.setObjectName("line_correo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_correo)
        self.line_pass1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_pass1.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.line_pass1.setMaxLength(100)
        self.line_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass1.setObjectName("line_pass1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_pass1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.line_pass2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_pass2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.line_pass2.setMaxLength(100)
        self.line_pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass2.setObjectName("line_pass2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_pass2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setStyleSheet("font: 14pt \"Calibri\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cmBox_admin = QtWidgets.QComboBox(self.layoutWidget1)
        self.cmBox_admin.setObjectName("cmBox_admin")
        self.cmBox_admin.addItem("")
        self.cmBox_admin.addItem("")
        self.cmBox_admin.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cmBox_admin)
        ventana_registro.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventana_registro)
        self.btn_cancelar.clicked.connect(ventana_registro.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ventana_registro)

    def retranslateUi(self, ventana_registro):
        _translate = QtCore.QCoreApplication.translate
        ventana_registro.setWindowTitle(_translate("ventana_registro", "Registrarse"))
        self.btn_cancelar.setText(_translate("ventana_registro", "Cancelar"))
        self.btn_cancelar.setShortcut(_translate("ventana_registro", "Esc"))
        self.btn_confirmar.setText(_translate("ventana_registro", "Confirmar"))
        self.btn_confirmar.setShortcut(_translate("ventana_registro", "Return"))
        self.label.setText(_translate("ventana_registro", "Usuario:"))
        self.label_4.setText(_translate("ventana_registro", "Correo:"))
        self.label_2.setText(_translate("ventana_registro", "Contraseña:"))
        self.label_3.setText(_translate("ventana_registro", "Confirmar Contraseña:"))
        self.label_5.setText(_translate("ventana_registro", "Categoria:"))
        self.cmBox_admin.setItemText(0, _translate("ventana_registro", "Empleado"))
        self.cmBox_admin.setItemText(1, _translate("ventana_registro", "Admin"))
        self.cmBox_admin.setItemText(2, _translate("ventana_registro", "Cliente"))