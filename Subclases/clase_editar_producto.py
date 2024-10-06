from PyQt5.QtWidgets import QDialog,QFormLayout,QLineEdit,QPushButton,QComboBox,QSpinBox

class Editar_producto(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editar Producto")
        self.setGeometry(300, 300, 400, 200)
        # Crear elementos
        layout = QFormLayout()
        self.line_nombre = QLineEdit()
        self.line_descripcion = QLineEdit()
        self.line_precio_unitario = QLineEdit()
        self.spin_recargo = QSpinBox()
        self.combo_unidad_medida = QComboBox()
        self.line_medida = QLineEdit()
        self.line_codigo = QLineEdit()
        # self.line_imagen = QLineEdit() no se a que se refiere con imagen :/

        # Agregar elementos
        layout.addRow("Nombre:", self.line_nombre)
        layout.addRow("descripcion:", self.line_descripcion)
        layout.addRow("precio unitario:", self.line_precio_unitario)
        layout.addRow("recargo:", self.spin_recargo)
        layout.addRow("unidad de medida:", self.combo_unidad_medida)
        layout.addRow("medida:", self.line_medida)
        layout.addRow("codigo:", self.line_codigo)
        
        #agregar opciones al comboBox
        # no se muy bien a que se refiere con unidad de medida asi que invente sobre la marcha
        self.combo_unidad_medida.addItem("Unidades")
        self.combo_unidad_medida.addItem("Kilos")
        self.combo_unidad_medida.addItem("Litros")

        # Botón  guardar usuario
        btn_guardar_editar_producto = QPushButton("Guardar Edicion")
        btn_guardar_editar_producto.clicked.connect(self.guardar_usuario)
        layout.addWidget(btn_guardar_editar_producto)
        self.setLayout(layout)

    def guardar_usuario(self):
        nombre = self.line_nombre.text()
        contrasenia = self.line_descripcion.text()
        grupo = self.line_precio_unitario.text()
        #TODO guardar al presionar el boton la hora actual para registrar la fecha y hora de creacion del usuario

        #TODO corroborar que esten todos los datos presentes y guardar los resultados en la base de datos 
        self.close()  # Cierra la ventana del formulario después de guardar