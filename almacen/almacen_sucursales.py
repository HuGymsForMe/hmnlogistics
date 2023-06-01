import os

from clases.sucursales import Sucursal

from almacen.almacen import Almacen

class AlmacenSucursales(Almacen):

    def __init__(self, app):
        self._cod_sucursal_combobox = []
        self._sucursales = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')
        self.CAMPO_COD_SUCURSAL = 0
        self.ANCHO_LISTADO = 100

    class CamposFicheroCsv:
        COD_SUCURSAL = 0
        PROVINCIA = 1
        DIRECCION = 2

        @staticmethod
        def opciones():
            return range(AlmacenSucursales.CamposFicheroCsv.COD_SUCURSAL,
                        AlmacenSucursales.CamposFicheroCsv.DIRECCION+1)

    @property
    def sucursales(self):
        return self._sucursales

    def cargar_datos(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'sucursales.csv'), 'r', 
            encoding='UTF-8') as fichero_sucursales:
                lineas = fichero_sucursales.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_sucursal = datos[self.CamposFicheroCsv.COD_SUCURSAL].strip()
                    provincia = str(datos[self.CamposFicheroCsv.PROVINCIA].strip())
                    direccion = str(datos[self.CamposFicheroCsv.DIRECCION].strip())
                    nueva_sucursal = Sucursal(cod_sucursal, provincia, direccion)
                    self._sucursales.append(nueva_sucursal)
        except IndexError:
            pass

    def add_datos(self, dato_cod_sucursal, dato_provincia, dato_direccion):
        for sucursal in self._sucursales:
            if dato_cod_sucursal == sucursal._cod_sucursal:
                return True
        else:
            nueva_sucursal = Sucursal(cod_sucursal=dato_cod_sucursal, provincia=dato_provincia, direccion=dato_direccion)
            self._sucursales.append(nueva_sucursal)
            return False
    
    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'sucursales.csv'), 'r', encoding="UTF-8") as fichero_sucursales:
                lineas = fichero_sucursales.readlines()
                for linea in lineas:
                    campos = linea.split(";")
                    primer_campo = str(campos[self.CAMPO_COD_SUCURSAL])
                    self._cod_sucursal_combobox.append(primer_campo)
                return self._cod_sucursal_combobox

    def del_datos(self, dato_borrar_sucursal):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'sucursales.csv'), 'r', encoding="UTF-8") as fichero_sucursales:
                lineas = fichero_sucursales.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_borrar_sucursal = str(campos[self.CamposFicheroCsv.COD_SUCURSAL].strip())
                    if dato_borrar_sucursal == campo_dato_borrar_sucursal:
                        self._sucursales.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass

    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'sucursales.csv'), 'w', encoding="UTF-8") as nuevo_csv_sucursales:
            for linea in self._sucursales:
                nuevo_csv_sucursales.write(f"{str(linea)}\n")
