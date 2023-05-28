import os
from clases.departamentos import Departamento

from almacen.almacen import Almacen

class AlmacenDepartamentos(Almacen):
    def __init__(self, app):
        self._cod_departamento_combobox = []
        self._departamentos = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')

    class CamposFicheroCsv:
        COD_DEPARTAMENTO = 0
        COD_SUCURSAL = 1
        NOMBRE = 2

        @staticmethod
        def opciones():
            return range(AlmacenDistribuidores.CamposFicheroCsv.COD_EMPLEADO,
                        AlmacenDistribuidores.CamposFicheroCsv.NOMBRE+1)

    @property
    def departamentos(self):
        return self._departamentos

    def cargar_datos(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'departamentos.csv'), 'r', 
            encoding='UTF-8') as fichero_departamentos:
                lineas = fichero_departamentos.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_departamento = datos[self.CamposFicheroCsv.COD_DEPARTAMENTO].strip()
                    cod_sucursal = datos[self.CamposFicheroCsv.COD_SUCURSAL].strip()
                    nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                    nuevo_departamento = Departamento(cod_departamento, cod_sucursal, nombre)
                    self._departamentos.append(nuevo_departamento)
        except IndexError:
            pass
    
    def add_datos(self, dato_cod_departamento, dato_cod_sucursal, dato_nombre):
        for departamento in self._departamentos:
            if dato_cod_departamento == departamento._cod_departamento:
                return True
        else:
            nuevo_departamento = Departamento(cod_departamento=dato_cod_departamento, cod_sucursal=dato_cod_sucursal, nombre=dato_nombre)
            self._departamentos.append(nuevo_departamento)
            return False

    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'departamentos.csv'), 'r', encoding="UTF-8") as fichero_departamentos:
                lineas = fichero_departamentos.readlines()
                for linea in lineas:
                    campos = linea.split(";")
                    primer_campo = str(campos[self.CamposFicheroCsv.COD_SUCURSAL])
                    self._cod_departamento_combobox.append(primer_campo)
                return self._cod_departamento_combobox

    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'departamentos.csv'), 'w', encoding="UTF-8") as nuevo_csv_departamentos:
            for linea in self._departamentos:
                nuevo_csv_departamentos.write(f"{str(linea)}\n")