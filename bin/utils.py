#TODO Antes de pasar a main cambiar las bases de datos de prueba a las finales
from mysql.connector import MySQLConnection,Error
from db_conection_config import conexion_db
from PyQt5.QtWidgets import QMessageBox
import bcrypt
import re
import session
from datetime import datetime

class usuario:
    """
    Clase que almacena los datos del usuario para uso interno y registro
    """
    def __init__(self,correo:str,usuario:str,password:str,grupo:int) -> None:
        self.correo = correo
        self.usuario = usuario
        self.password = password
        self.grupo = grupo

def comprobar_credenciales(usuario:str,contra:str) -> bool:
    '''
    Obtiene el usuario recibido y revisa la contraseña recibida comparandola con la almacenada en la DB y devuelve un valor booleano
    '''
    flag = False
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    #conexion con la base de datos desempaquetando el config
    conexion = MySQLConnection(**config_db)
    #cursor para ejecutar las consultas SQL
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT usser_id FROM usuarios WHERE usuario = %s",(usuario,))
        resultado = cursor.fetchone()
        if resultado:
            id_usuario = resultado[0]
            #obtener contraseña
            cursor.execute("SELECT password FROM usuarios WHERE usser_id = %s",(id_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                passw_hasheada = resultado[0]
                #validar la contraseña
                if bcrypt.checkpw(contra.encode('utf-8'),passw_hasheada.encode('utf-8')):
                    flag = True
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Datos de Usuario y/o Contraseña incorrectos.")
                    msg.setWindowTitle("Advertencia")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec()
    except Error as err:
        print(f"Error: {err}")
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Datos de Usuario y/o Contraseña incorrectos.")
        msg.setWindowTitle("Advertencia")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    finally:
        cursor.close()
        conexion.close()
    return flag

def agregar_usuario(usuario:usuario) -> None:
    ''''
    Recibe datos validados previamente para solo subirlos a la DB, no retorna ningun valor
    '''
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    conexion = MySQLConnection(**config_db)
    cursor = conexion.cursor()
    hashpw = bcrypt.hashpw((usuario.password.encode('utf-8')),bcrypt.gensalt()).decode('utf-8')
    consultaSQL = "INSERT INTO usuarios (usuario,password,correo,grupo,fecha_creacion,ult_modificacion) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (usuario.usuario,hashpw,usuario.correo,usuario.grupo,datetime.now(),datetime.now())
    try: 
        cursor.execute(consultaSQL,values)
        conexion.commit()
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def obtener_data(usuario:str)->list:
    """"
    Obtiene el id de un usuario en base a un username
    """
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    #conexion con la base de datos desempaquetando el config
    conexion = MySQLConnection(**config_db)
    #cursor para ejecutar las consultas SQL
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s",(usuario,))
        resultado = cursor.fetchone()
        return resultado
    except Error as err:
        print(f"Error: {err}")

def hashear(contra:str)->str:
    return bcrypt.hashpw((contra.encode('utf-8')),bcrypt.gensalt()).decode('utf-8')

#TODO's 
'''
Realizar la conexion logica con las ventanas SQL, Funciones 2 y 3 requieren los datos previos validados antes de pasarlos, ver si mejoraralo.
'''

def validar_usuario(usuario:str) -> bool:
    """
    Levanta un error por cuenta propia y devuelve un booleano
    """
    #coneccion con la DB
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    conexion = MySQLConnection(**config_db)
    cursor = conexion.cursor()
    try:
        #consulta para obtener un valor en caso de que el usuario exista
        cursor.execute("SELECT usuario FROM usuarios WHERE usuario = %s",(usuario,))
        resultado = cursor.fetchone()
        if resultado is None:
            return True
        #return que devuelve true si no existe ya un usuario con ese nombre
        else:
            raise ValueError ("El usuario ya existe")
        
    except ValueError as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(str(e))
        msg.setWindowTitle("Advertencia")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
        return False
    #mensaje de error por si existe el usuario
    except:
        print("Ni idea que se rompio")

def validador_email(email) -> bool:
    """
    Funcion para validar un email (muy basico sin APIs solamente formato), usar el booleano para validar
    """
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email) is not None

def ult_vez_mod(id_usuario:int, accion:str) -> None:
    """
    Funcion que modifica la ultima vez de un usuario y registra su accion
    """
    #TODO implementar logger
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    conexion = MySQLConnection(**config_db)
    cursor = conexion.cursor()
    try: 
        consulta=("UPDATE historial_usuarios SET accion =%s, fecha = %s WHERE id = %s")
        values = (accion,datetime.now(), id_usuario)
        cursor.execute(consulta,values)
        conexion.commit()
    except:
        #TODO implementar logger para errores. 
        pass

def 