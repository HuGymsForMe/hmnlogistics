import os
from clases.distribuidores import Distribuidor

from almacen.almacen import Almacen

class AlmacenDistribuidores(Almacen):
    def __init__(self, app):
        self._cod_distribuidor_combobox = []
        self._distribuidores = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')

    class CamposFicheroCsv:
        COD_DISTRIBUIDOR = 0
        NOMBRE = 1

        @staticmethod
        def opciones():
            return range(AlmacenDistribuidores.CamposFicheroCsv.COD_DISTRIBUIDOR,
                        AlmacenDistribuidores.CamposFicheroCsv.NOMBRE+1)

    @property
    def distribuidores(self):
        return self._distribuidores
    
    def cargar_datos(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'distribuidores.csv'), 'r', 
            encoding='UTF-8') as fichero_distribuidores:
                lineas = fichero_distribuidores.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_distribuidor = datos[self.CamposFicheroCsv.COD_DISTRIBUIDOR].strip()
                    nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                    nuevo_distribuidor = Distribuidor(cod_distribuidor, nombre)
                    self._distribuidores.append(nuevo_distribuidor)
        except IndexError:
            pass

    def add_datos(self, dato_cod_distribuidor, dato_nombre):
        for distribuidor in self._distribuidores:
            if dato_cod_distribuidor == distribuidor._cod_distribuidor or dato_nombre == distribuidor._nombre:
                return True
        else:
            nuevo_distribuidor = Distribuidor(cod_distribuidor=dato_cod_distribuidor, nombre=dato_nombre)
            self._distribuidores.append(nuevo_distribuidor)
            return False
    
    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'distribuidores.csv'), 'r', encoding="UTF-8") as fichero_distribuidores:
                lineas = fichero_distribuidores.readlines()
                for linea in lineas:
                    campos = linea.split(";")
                    primer_campo = str(campos[self.CamposFicheroCsv.COD_DISTRIBUIDOR])
                    self._cod_distribuidor_combobox.append(primer_campo)
                return self._cod_distribuidor_combobox

    def del_datos(self, dato_borrar_distribuidor):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'distribuidores.csv'), 'r', encoding="UTF-8") as fichero_distribuidores:
                lineas = fichero_distribuidores.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_borrar_distribuidor = str(campos[self.CamposFicheroCsv.COD_DISTRIBUIDOR].strip())
                    if dato_borrar_distribuidor == campo_dato_borrar_distribuidor:
                        self._distribuidores.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass
    
    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'distribuidores.csv'), 'w', encoding="UTF-8") as nuevo_csv_distribuidores:
            for linea in self._distribuidores:
                nuevo_csv_distribuidores.write(f"{str(linea)}\n")
