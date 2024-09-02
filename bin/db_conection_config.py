from ast import parse
from configparser import ConfigParser

def conexion_db(archivo = "config.ini", seccion = "test"):
    '''
    Pasar como datos el archivo o ruta de archivo donde se encuentren las credenciales de la DB, como segundo valor pasar seccion del archivo al que desea conectarse
    '''
    #objeto con data del archivo
    parser = ConfigParser()
    parser.read(archivo)
    #diccionario para almacenar los pares key:value en archivo ej: (host=profe deje de leer los comentarios)
    credenciales = {}

    if parser.has_section(seccion):#comprueba que la seccion recibida exista
        items = parser.items(seccion)
        for item in items:
            credenciales[item[0]] = item[1] #asignacion de los pares de key:value al diccionario
    else:
        #error en caso de no tener seccion deseada
        raise Exception(f'{seccion} No existe en el archivo o esta mal ingresado')
    return credenciales