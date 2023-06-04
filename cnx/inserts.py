import os
import mysql.connector

from cnx.conexion import conexion
from datetime import datetime

class Inserts:
    def __init__(self):
        self.cnx = conexion()
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')
        self.DELETE_PREVIO_DEPARTAMENTOS = f"DELETE FROM hmn_departamentos"
        self.DELETE_PREVIO_PEDIDOS = f"DELETE FROM hmn_pedidos;"
        self.DELETE_PREVIO_DISTRIBUIDORES = f"DELETE FROM hmn_distribuidores;"
        self.DELETE_PREVIO_SUCURSALES = f"DELETE FROM hmn_sucursales;"
        self.DELETE_PREVIO_CLIENTES = f"DELETE FROM hmn_clientes;"
        self.DELETE_PREVIO_ARTICULOS = f"DELETE FROM hmn_articulos;"
        self.DELETE_PREVIO_DATOS_EMPLEADOS = f"DELETE FROM hmn_datos_empleados;"
        self.DELETE_PREVIO_EMPLEADOS = f"DELETE FROM hmn_empleados;"
    class ConstantesCampos:
        CAMPO_0 = 0
        CAMPO_1 = 1
        CAMPO_2 = 2
        CAMPO_3 = 3
        CAMPO_4 = 4
        CAMPO_5 = 5
        CAMPO_6 = 6
        
        @staticmethod
        def opciones():
            return range(ConstantesCampos.TELEFONO,
                ConstantesCampos.PAGINA_WEB+1)

    def realizar_deletes(self):
        cursor = self.cnx.cursor()
        cursor.execute(self.DELETE_PREVIO_DATOS_EMPLEADOS)
        cursor.execute(self.DELETE_PREVIO_EMPLEADOS)
        cursor.execute(self.DELETE_PREVIO_DEPARTAMENTOS)
        cursor.execute(self.DELETE_PREVIO_PEDIDOS)
        cursor.execute(self.DELETE_PREVIO_ARTICULOS)
        cursor.execute(self.DELETE_PREVIO_CLIENTES)
        cursor.execute(self.DELETE_PREVIO_SUCURSALES)
        cursor.execute(self.DELETE_PREVIO_DISTRIBUIDORES)
        self.cnx.commit()
        cursor.close()


    def cargar_bbdd_distribuidores(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'distribuidores.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_distribuidor = datos[self.ConstantesCampos.CAMPO_0].strip()
                nombre = datos[self.ConstantesCampos.CAMPO_1].strip()
                inserts_distribuidores = f"INSERT INTO hmn_distribuidores (cod_distribuidor, nombre) VALUES(%s, %s);"
                valores = (cod_distribuidor, nombre)
                cursor.execute(inserts_distribuidores, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_sucursales(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'sucursales.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_sucursal = datos[self.ConstantesCampos.CAMPO_0].strip()
                provincia = datos[self.ConstantesCampos.CAMPO_1].strip()
                direccion = datos[self.ConstantesCampos.CAMPO_2].strip()
                inserts_sucursales = f"INSERT INTO hmn_sucursales (cod_sucursal, provincia, direccion) VALUES(%s, %s, %s);"
                valores = (cod_sucursal, provincia, direccion)
                cursor.execute(inserts_sucursales, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_clientes(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_cliente = datos[self.ConstantesCampos.CAMPO_0].strip()
                cod_sucursal = datos[self.ConstantesCampos.CAMPO_1].strip()
                nombre = datos[self.ConstantesCampos.CAMPO_2].strip()
                inserts_clientes = "INSERT INTO hmn_clientes (cod_cliente, cod_sucursal, nombre) VALUES (%s, %s, %s);"
                valores = (cod_cliente, cod_sucursal, nombre)
                cursor.execute(inserts_clientes, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_articulos(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_articulo = datos[self.ConstantesCampos.CAMPO_0].strip()
                cod_cliente = datos[self.ConstantesCampos.CAMPO_1].strip()
                nombre = datos[self.ConstantesCampos.CAMPO_2].strip()
                descripcion = datos[self.ConstantesCampos.CAMPO_3].strip()
                categoria = datos[self.ConstantesCampos.CAMPO_4].strip()
                inserts_articulos = f"INSERT INTO hmn_articulos (cod_articulo, cod_cliente, nombre, descripcion, categoria) VALUES(%s, %s, %s, %s, %s);"
                valores = (cod_articulo, cod_cliente, nombre, descripcion, categoria)
                cursor.execute(inserts_articulos, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_pedidos(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'pedidos.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_pedido = datos[self.ConstantesCampos.CAMPO_0].strip()
                cod_distribuidor = datos[self.ConstantesCampos.CAMPO_1].strip()
                cod_sucursal = datos[self.ConstantesCampos.CAMPO_2].strip()
                fecha_pedido = datetime.strptime(datos[self.ConstantesCampos.CAMPO_3].strip(), '%Y-%m-%d').date()
                cantidad_articulos = int(datos[self.ConstantesCampos.CAMPO_4].strip())
                peso = float(datos[self.ConstantesCampos.CAMPO_5].strip())
                precio = float(datos[self.ConstantesCampos.CAMPO_6].strip())
                inserts_pedidos = f"INSERT INTO hmn_pedidos (cod_pedido, cod_distribuidor, cod_sucursal, fecha_pedido, cantidad_articulos, \
peso, precio) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                valores = (cod_pedido, cod_distribuidor, cod_sucursal, fecha_pedido, cantidad_articulos, peso, precio)
                cursor.execute(inserts_pedidos, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_departamentos(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'departamentos.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_departamento = datos[self.ConstantesCampos.CAMPO_0].strip()
                cod_sucursal = datos[self.ConstantesCampos.CAMPO_1].strip()
                nombre = datos[self.ConstantesCampos.CAMPO_2].strip()
                inserts_departamentos = f"INSERT INTO hmn_departamentos (cod_departamento, cod_sucursal, nombre) VALUES (%s, %s, %s);"
                valores = (cod_departamento, cod_sucursal, nombre)
                cursor.execute(inserts_departamentos, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_datos_empleados(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                dni = datos[self.ConstantesCampos.CAMPO_0].strip()
                nombre = datos[self.ConstantesCampos.CAMPO_1].strip()
                apellidos = datos[self.ConstantesCampos.CAMPO_2].strip()
                fecha_nac = datetime.strptime(datos[self.ConstantesCampos.CAMPO_3].strip(), '%Y-%m-%d').date()
                domicilio = datos[self.ConstantesCampos.CAMPO_4].strip()
                inserts_datos_empleados = f"INSERT INTO hmn_datos_empleados (dni, nombre, apellidos, fecha_nac, domicilio) VALUES (%s, %s, %s, %s, %s);"
                valores = (dni, nombre, apellidos, fecha_nac, domicilio)
                cursor.execute(inserts_datos_empleados, valores)
                self.cnx.commit()
            cursor.close()

    def cargar_bbdd_empleados(self):
        cursor = self.cnx.cursor()
        with open(os.path.join(self.RUTA_FICHEROS, 'empleados.csv'), encoding='UTF-8') as informacion:
            lineas = informacion.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_empleado = datos[self.ConstantesCampos.CAMPO_0].strip()
                cod_departamento = datos[self.ConstantesCampos.CAMPO_1].strip()
                dni = datos[self.ConstantesCampos.CAMPO_2].strip()
                fecha_alta = datetime.strptime(datos[self.ConstantesCampos.CAMPO_3].strip(), '%Y-%m-%d').date()
                salario = float(datos[self.ConstantesCampos.CAMPO_4].strip())
                telefono = int(datos[self.ConstantesCampos.CAMPO_5].strip())
                inserts_empleados = f"INSERT INTO hmn_empleados (cod_empleado, cod_departamento, dni, fecha_alta, salario, telefono) \
VALUES (%s, %s, %s, %s, %s, %s);"
                valores = (cod_empleado, cod_departamento, dni, fecha_alta, salario, telefono)
                cursor.execute(inserts_empleados, valores)
                self.cnx.commit()
            cursor.close()