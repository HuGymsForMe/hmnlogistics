import os
import random
from clases.articulos import Articulo

from almacen.almacen import Almacen

class AlmacenArticulos(Almacen):
    def __init__(self, app):
        self._cod_articulo_combobox = []
        self._articulos = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files') 
    
    class CamposFicheroCsv:
        COD_ARTICULO = 0
        COD_CLIENTE = 1
        NOMBRE = 2
        DESCRIPCION = 3
        CATEGORIA = 4

        @staticmethod
        def opciones():
            return range(AlmacenArticulos.CamposFicheroCsv.COD_ARTICULO,
                        AlmacenArticulos.CamposFicheroCsv.CATEGORIA+1)

    @property
    def articulos(self):
        return self._articulos

    def cargar_datos(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), 'r', 
            encoding='UTF-8') as fichero_articulos:
                lineas = fichero_articulos.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_articulo = datos[self.CamposFicheroCsv.COD_ARTICULO].strip()
                    cod_cliente = datos[self.CamposFicheroCsv.COD_CLIENTE].strip()
                    nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                    descripcion = str(datos[self.CamposFicheroCsv.DESCRIPCION].strip())
                    categoria = str(datos[self.CamposFicheroCsv.CATEGORIA].strip())
                    nuevo_articulo = Articulo(cod_articulo, cod_cliente, nombre, descripcion, categoria)
                    self._articulos.append(nuevo_articulo)
        except IndexError:
            pass


    def add_datos(self, dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria):
        for articulo in self._articulos:
            if dato_cod_articulo == articulo._cod_articulo:
                return True
        else:
            nuevo_articulo = Articulo(cod_articulo=dato_cod_articulo, cod_cliente=dato_cod_cliente, nombre=dato_nombre, descripcion=dato_descripcion, categoria=dato_categoria)
            self._articulos.append(nuevo_articulo)
            return False

    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), 'r', encoding="UTF-8") as fichero_articulos:
            lineas = fichero_articulos.readlines()
            for linea in lineas:
                campos = linea.split(";")
                primer_campo = str(campos[self.CamposFicheroCsv.COD_ARTICULO])
                self._cod_articulo_combobox.append(primer_campo)
            return self._cod_articulo_combobox

    def del_datos(self, dato_borrar_articulo):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), 'r', encoding="UTF-8") as fichero_articulos:
                lineas = fichero_articulos.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_borrar_articulo= str(campos[self.CamposFicheroCsv.COD_ARTICULO].strip())
                    if dato_borrar_articulo == campo_dato_borrar_articulo:
                        self._articulos.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass
    
    '''def del_articulos_por_del_cliente(self, dato_borrar_cliente):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), 'r', encoding="UTF-8") as fichero_articulos:
                lineas = fichero_articulos.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_borrar_cliente = str(campos[self.CAMPO_COD_CLIENTE].strip())
                    if dato_borrar_cliente == campo_dato_borrar_cliente:
                        self._articulos.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass'''

    def del_articulos_por_del_cliente(self, dato_borrar_cliente):
        try:
            for articulo in self._articulos:
                if dato_borrar_cliente == articulo.cod_cliente:
                    self._articulos.pop(contador)
                    return True
                    contador += 1
                return False
        except IndexError:
            pass

    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'articulos.csv'), 'w', encoding="UTF-8") as nuevo_csv_articulos:
            for linea in self._articulos:
                nuevo_csv_articulos.write(f"{str(linea)}\n")