import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QFormLayout,QLineEdit,QPushButton,QCheckBox,QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import loadUi
from pathlib import Path

#importar clases Para generar las ventanas
from Subclases.Clase_crear_usuario import Crear_usuario
from Subclases.Clase_editar_usuario import Editar_usuario
from Subclases.Clase_crear_producto import Crear_producto
from Subclases.clase_editar_producto import Editar_producto
from Subclases.Clase_crear_cliente import Crear_cliente
from Subclases.Clase_editar_cliente import Editar_cliente


class Clase_ventana_principal_admin(QMainWindow):   
    def __init__(self,parent = None):
        super(Clase_ventana_principal_admin,self).__init__(parent)
        loadUi(r"admin.ui",self)
        self.setup()
    def setup (self):
        #Usuarios
        self.pb_crear_usuario.clicked.connect(self.conectar_crear_usuario)
        self.pb_editar_usuario.clicked.connect(self.conectar_editar_usuario)#TODO agregar los datos del usuario para identificar que usuario editar
        self.pb_eliminar_usuario.clicked.connect(self.conectar_eliminar_usuario)
        #Clientes
        self.pb_crear_cliente.clicked.connect(self.conectar_crear_cliente)
        self.pb_editar_cliente.clicked.connect(self.conectar_editar_cliente)
        self.pb_eliminar_cliente.clicked.connect(self.conectar_eliminar_cliente)
        self.pb_estadisticas_cliente.clicked.connect(self.conectar_estadisticas_cliente)
        #productos
        self.pb_crear_producto.clicked.connect(self.conectar_crear_producto)
        self.pb_editar_producto.clicked.connect(self.conectar_editar_producto)
        self.pb_eliminar_producto.clicked.connect(self.conectar_eliminar_producto)
        self.pb_ver_estadisticas_producto.clicked.connect(self.conectar_ver_estadisticas_productos)

    #Usuarios
    def conectar_crear_usuario (self):
        self.ventana_crear_usuario = Crear_usuario()
        self.ventana_crear_usuario.exec()

    def conectar_editar_usuario (self):
        self.ventana_editar_usuario = Editar_usuario()
        self.ventana_editar_usuario.exec()

    def conectar_eliminar_usuario (self):
        #TODO
        pass

    #Cliente
    def conectar_crear_cliente (self):
        self.ventana_crear_cliente = Crear_cliente()
        self.ventana_crear_cliente.exec()

    def conectar_editar_cliente (self):
        self.ventana_editar_cliente = Editar_cliente()
        self.ventana_editar_cliente.exec()

    def conectar_eliminar_cliente (self):
        #TODO
        pass

    def conectar_estadisticas_cliente (self):
        #TODO
        pass

    #Productos
    def conectar_crear_producto (self):
        self.ventana_crear_producto = Crear_producto()
        self.ventana_crear_producto.exec()

    def conectar_editar_producto (self):
        self.ventana_editar_producto = Editar_producto()
        self.ventana_editar_producto.exec()

    def conectar_eliminar_producto (self):
        #TODO
        pass

    def conectar_ver_estadisticas_productos (self):
        #TODO
        pass

def main ():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path("styles.qss").read_text())
    ventana = Clase_ventana_principal_admin()
    ventana.show()
    app.exec()

if __name__ =="__main__":
    main()