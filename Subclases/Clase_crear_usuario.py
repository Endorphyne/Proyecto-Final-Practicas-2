from PyQt5.QtWidgets import QDialog,QFormLayout,QLineEdit,QPushButton,QComboBox

class Crear_usuario(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crear Usuario")
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
        btn_guardar_crear_usuario = QPushButton("Guardar Usuario")
        btn_guardar_crear_usuario.clicked.connect(self.guardar_usuario)
        layout.addWidget(btn_guardar_crear_usuario)
        self.setLayout(layout)

    def guardar_usuario(self):
        nombre = self.line_nombre.text()
        contrasenia = self.line_contrasenia.text()
        grupo = self.combo_grupo.currentText()
        #TODO guardar al presionar el boton la hora actual para registrar la fecha y hora de creacion del usuario

        #TODO guardar los datos en la base de datos
        self.close()  # Cierra la ventana del formulario después de guardar