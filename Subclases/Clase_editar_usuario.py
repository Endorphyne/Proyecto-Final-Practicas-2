from PyQt5.QtWidgets import QDialog,QFormLayout,QLineEdit,QPushButton,QComboBox

class Editar_usuario(QDialog):
    def __init__(self):#TODO traer los datos del usuario para identificar que usuario es el que se tiene que modificar
        super().__init__()
        self.setWindowTitle("Editar Usuario")
        self.setGeometry(300, 300, 400, 200)
        # Crear elementos
        layout = QFormLayout()
        self.line_nombre = QLineEdit()
        self.line_contrasenia = QLineEdit()
        self.combo_grupo = QComboBox()

        # Agregar elementos
        layout.addRow("Nombre:", self.line_nombre)
        layout.addRow("Contraseña:", self.line_contrasenia)
        layout.addRow("Grupo:", self.combo_grupo)
        
        #agregar opciones al comboBox
        self.combo_grupo.addItem("Admin")
        self.combo_grupo.addItem("Usuario")

        # Botón  guardar usuario
        btn_guardar_edicion_usuario = QPushButton("Guardar Cambios")
        btn_guardar_edicion_usuario.clicked.connect(self.guardar_cambios)
        layout.addWidget(btn_guardar_edicion_usuario)
        self.setLayout(layout)

    def guardar_cambios(self):
        nombre = self.line_nombre.text()
        contrasenia = self.line_contrasenia.text()
        grupo = self.combo_grupo.currentText()

        #TODO guardar los datos en la base de datos
        self.close()  # Cierra la ventana del formulario después de guardar