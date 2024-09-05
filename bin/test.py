#TODO Antes de pasar a main cambiar las bases de datos de prueba a las finales
from mysql.connector import MySQLConnection,Error
from db_conection_config import conexion_db
import bcrypt
from datetime import datetime

def comprobar_credenciales(usuario:str,contra:str) -> bool:
    '''
    Obtiene el id del usuario recibido y revisa la contraseña recibida comparandola con la almacenada en la DB y devuelve un valor booleano
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
                    #TODO Crear un popup para que informe al usuario que ingreso mal los datos
                    pass
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
    return flag
def agregar_usuario(usuario:str,contraseña:str,correo:str,grupo:int = 1):
    ''''
    Recibe datos validados previamente para solo subirlos a la DB, no retorna ningun valor
    '''
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    conexion = MySQLConnection(**config_db)
    cursor = conexion.cursor()
    hashpw = bcrypt.hashpw((contraseña.encode('utf-8')),bcrypt.gensalt()).decode('utf-8')
    consultaSQL = "INSERT INTO usuarios (usuario,password,correo,grupo,fecha_creacion,ult_modificacion) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (usuario,hashpw,correo,grupo,datetime.now(),datetime.now())
    try: 
        cursor.execute(consultaSQL,values)
        conexion.commit()
        print("usuario agregado")
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
# agregar_usuario("lautaro","lauta22","lautaroso@gmail.com")
def recuperar_contrasenia(nueva_contrasenia:str,id_usuario:int):
    """
    Remplaza la contraseña vieja de la databse con la nueva contraseña previamente validada como: CORRECTA (es igual en ambos campos), DISTINTA(es diferente a la anterior contraseña), VALORES(posee 4 caracteres numericos, y es de al menos 8 caracteres)
    """
    nueva_contrasenia = bcrypt.hashpw(nueva_contrasenia.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    config_db = conexion_db("bin\config.ini","Proyecto Practicas2")
    conexion = MySQLConnection(**config_db)
    cursor = conexion.cursor()
    consultaSQL=("UPDATE usuarios SET password = %s WHERE usser_id = %s")
    values = (nueva_contrasenia, id_usuario)
    try:
        cursor.execute(consultaSQL,values)
        conexion.commit()
        print("Contrasenia cambiada")
    except Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
#TODO's 
'''
Realizar la conexion logica con las ventanas SQL, Funciones 2 y 3 requieren los datos previos validados antes de pasarlos, ver si mejoraralo.
'''
agregar_usuario("lautaro","peperoni","kici@gmail.com",1)