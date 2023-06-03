import os

import mysql.connector
from mysql.connector import errorcode

USER = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
DATABASE = 'hmnlogistics'

def conexion():
    try:
        cnx = mysql.connector.connect(user=USER, password=PASSWORD,
                                    host=HOST,
                                    database=DATABASE)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error de conexión")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("No existe la BBDD")
        else:
            print(err)
    else:
        return cnx