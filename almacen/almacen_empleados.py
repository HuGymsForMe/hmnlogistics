import os
from clases.empleados import Empleado
from clases.datos_empleados import DatosEmpleado

from almacen.almacen import Almacen

class AlmacenEmpleados(Almacen):
    def __init__(self, app):
        self._empleados = []
        self._datos_empleados = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')

    class CamposFicheroCsv:
        COD_EMPLEADO = 0
        COD_DEPARTAMENTO = 1
        DNI = 2
        NOMBRE = 3
        APELLIDOS = 4
        FECHA_NAC = 6
        FECHA_ALTA = 7
        SALARIO = 8
        DOMICILIO = 9
        TELEFONO = 10
        OFICIO = 11
        
        @staticmethod
        def opciones():
            return range(AlmacenPedidos.CamposFicheroCsv.COD_EMPLEADO,
                        AlmacenPedidos.CamposFicheroCsv.OFICIO+1)

    @property
    def empleados(self):
        return self._empleados

    @property
    def datos_empleados(self):
        return self._datos_empleados

    def cargar_datos(self):
        try: #SEPARAMOS LAS LISTAS PARA LA NORMALIZACIÓN
            with open(os.path.join(self.RUTA_FICHEROS, 'empleados.csv'), 'r', 
            encoding='UTF-8') as fichero_empleados:
                lineas = fichero_empleados.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_empleado = datos[self.CamposFicheroCsv.COD_EMPLEADO].strip()
                    cod_departamento = str(datos[self.CamposFicheroCsv.COD_DEPARTAMENTO].strip())
                    dni = str(datos[self.CamposFicheroCsv.DNI].strip())
                    fecha_alta = str(datos[self.CamposFicheroCsv.FECHA_ALTA].strip())
                    salario = str(datos[self.CamposFicheroCsv.SALARIO].strip())
                    telefono = str(datos[self.CamposFicheroCsv.TELEFONO].strip())
                    oficio = str(datos[self.CamposFicheroCsv.OFICIO].strip())
                    nuevo_empleado = Empleado(cod_empleado, cod_departamento, dni, fecha_alta, salario, telefono, oficio)
                    self._empleados.append(nuevo_empleado)

            with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), 'r',
            encoding='UTF-8') as fichero_datos_empleados:
                lineas = fichero_datos_empleados.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    dni = str(datos[self.CamposFicheroCsv.DNI].strip())
                    nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                    apellidos = str(datos[self.CamposFicheroCsv.APELLIDOS].strip())
                    fecha_nac = str(datos[self.CamposFicheroCsv.FECHA_NAC].strip())
                    domicilio = str(datos[self.CamposFicheroCsv.DOMICILIO].strip())
                    nuevo_datos_empleado = DatosEmpleado(dni, nombre, apellidos, fecha_nac, domicilio)
                    self._datos_empleados.append(nuevo_empleado)
        except IndexError:
            pass

    '''def add_datos(self, dato_cod_distribuidor, dato_nombre):
        for distribuidor in self._distribuidores:
            if dato_cod_distribuidor == distribuidor._cod_distribuidor or dato_nombre == distribuidor._nombre:
                return True
        else:
            nuevo_distribuidor = Distribuidor(cod_distribuidor=dato_cod_distribuidor, nombre=dato_nombre)
            self._distribuidores.append(nuevo_distribuidor)
            return False'''
        
        
 