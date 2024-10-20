import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Clase_ventana import Ui_MainWindow  # Asegúrate de que este es el nombre correcto del archivo convertido
from clase_admin import Ui_admin_mainWindow
from clase_empleado import Ui_empleado_MainWindow
from Clase_ventana_registro import Ui_ventana_registro
import bin.utils as utils

class admin_window(QMainWindow, Ui_admin_mainWindow):
    def __init__(self) -> None:
        super().__init__()  # Llamada correcta a super()
        self.setupUi(self)

class empleado_window(QMainWindow, Ui_empleado_MainWindow):
    def __init__(self) -> None:
        super().__init__()  # Llamada correcta a super()
        self.setupUi(self)


class Clase_login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz
        self.btn_iniciar_sesion.clicked.connect(self.filtro_usuario)  # Conecta el botón con el método filtro_usua
        self.btn_tegistrarse.clicked.connect(self.registro)

    def filtro_usuario(self,) -> None:
        """
        Ejecuta una ventana u otra basándose en el grupo del id_usuario (1:empleado/0:admin)
        """
        id_usuario = utils.obtener_data(self.line_usuario.text())
        grupo = id_usuario[4]
        if grupo == 0:
            self.admin_window = admin_window()
            self.admin_window.show()
            self.close()
        else:
            self.empleado_window = empleado_window()
            self.empleado_window.show()
            self.close()

    def registro(self,) -> None:
        """
        mostrar la venata de registro
        """
        self.registro_window = registro_window()
        self.registro_window.show()
        self.close()

class registro_window(QMainWindow, Ui_ventana_registro):
    #TODO pasar a la aplicacion del admin para registrar usuarios
    def __init__(self) -> None:
        super().__init__()  # Llamada correcta a super()
        self.setupUi(self)
        self.btn_confirmar.clicked.connect(self.slot_usuarios)

    def slot_usuarios(self):
        utils.agregar_usuario(self.validar_datos_registro())
    
    def validar_datos_registro(self):
        try:
            if utils.validador_email(self.line_correo.text()) == True:
                correo = self.line_correo.text()
            else:
                raise ValueError("Correo ingresado no valido")
            print(self.line_usuario.text())
            if utils.validar_usuario(self.line_usuario.text()) == True:
                nombre_usuario = self.line_usuario.text()
            password1 = self.line_pass1.text()
            password2 = self.line_pass2.text()
            if self.cmBox_admin.currentText() == "Cliente":
                grupo = 2
            elif self.cmBox_admin.currentText() == "Empleado":
                grupo = 1
            else:
                grupo = 0
            if password1 != password2:
                raise ValueError("Las contraseñas no coinciden.")
            password = password1
        # mensajes de error para datos mas ingresados
        except ValueError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("Advertencia")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return None

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error en los datos ingresados.")
            msg.setWindowTitle("Advertencia")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return None

        else:
            user = utils.usuario(correo, nombre_usuario, password, grupo)
            return user



if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    window = Clase_login()  # Crea una instancia de la ventana principal
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos
