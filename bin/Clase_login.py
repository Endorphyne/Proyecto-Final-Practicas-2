import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ventana_Login_Usuarios import Ui_MainWindow  # Asegúrate de que este es el nombre correcto del archivo convertido

class Clase_login(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz
        self.ok_btn.clicked.connect(self.mostrar_error)  # Conecta el botón con el método mostrar_error

    def mostrar_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Datos de Usuario y/o Contraseña incorrectos.")
        msg.setWindowTitle("Advertencia")
        msg.setStandardButtons(QMessageBox.Ok)
        # Aplicar estilo personalizado
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #232743;  /* Fondo general */
                color: #797979;  /* Detalles */
                font-size: 14px;
            }
            QMessageBox QLabel {
                color: #D8DBE2;  /* Fondo específico */
            }
            QPushButton {
                background-color: #5E7CE2;  /* Botones */
                color: #ECEFF4; 
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
        """)
        msg.exec()
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    window = Clase_login()  # Crea una instancia de la ventana principal
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos
