import os
from clases.empleados import Empleado
from clases.datos_empleados import DatosEmpleado

from almacen.almacen import Almacen

class AlmacenEmpleados(Almacen):
    def __init__(self, app):
        self._empleados = []
        self._datos_empleados = []
        self._dni_combobox = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')

    class CamposFicheroCsv:
        CAMPO_0 = 0
        CAMPO_1 = 1
        CAMPO_2 = 2
        CAMPO_3 = 3
        CAMPO_4 = 4
        CAMPO_5 = 5
        CAMPO_6 = 6
        
        @staticmethod
        def opciones():
            return range(Almacenempleadoss.CamposFicheroCsv.COD_EMPLEADO,
                        Almacenempleadoss.CamposFicheroCsv.OFICIO+1)

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
                    cod_empleado = datos[self.CamposFicheroCsv.CAMPO_0].strip()
                    cod_departamento = str(datos[self.CamposFicheroCsv.CAMPO_1].strip())
                    dni = str(datos[self.CamposFicheroCsv.CAMPO_2].strip())
                    fecha_alta = str(datos[self.CamposFicheroCsv.CAMPO_3].strip())
                    salario = str(datos[self.CamposFicheroCsv.CAMPO_4].strip())
                    telefono = str(datos[self.CamposFicheroCsv.CAMPO_5].strip())
                    oficio = str(datos[self.CamposFicheroCsv.CAMPO_6].strip())
                    nuevo_empleado = Empleado(cod_empleado, cod_departamento, dni, fecha_alta, salario, telefono, oficio)
                    self._empleados.append(nuevo_empleado)

            with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), 'r',
            encoding='UTF-8') as fichero_datos_empleados:
                lineas = fichero_datos_empleados.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    dni = str(datos[self.CamposFicheroCsv.CAMPO_0].strip())
                    nombre = str(datos[self.CamposFicheroCsv.CAMPO_1].strip())
                    apellidos = str(datos[self.CamposFicheroCsv.CAMPO_2].strip())
                    fecha_nac = str(datos[self.CamposFicheroCsv.CAMPO_3].strip())
                    domicilio = str(datos[self.CamposFicheroCsv.CAMPO_4].strip())
                    nuevo_datos_empleado = DatosEmpleado(dni, nombre, apellidos, fecha_nac, domicilio)
                    self._datos_empleados.append(nuevo_datos_empleado)
        except IndexError:
            pass
            

    def add_datos(self, dato_cod_empleado, dato_cod_departamento, dato_dni, dato_fecha_alta, dato_salario,
                  dato_telefono, dato_oficio):
        for empleado in self._empleados:
            if dato_cod_empleado == empleado._cod_empleado:
                return True
        else:
            nuevo_empleado = Empleado(cod_empleado=dato_cod_empleado, cod_departamento=dato_cod_departamento, dni=dato_dni,
            fecha_alta=dato_fecha_alta, salario=dato_salario, telefono=dato_telefono, oficio=dato_oficio)
            self._empleados.append(nuevo_empleado)
            return False

    def add_datos_2(self, dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio):
        for datos_empleados in self._datos_empleados:
            if dato_dni == datos_empleados._dni:
                return True
        else:
            nuevo_datos_empleado = DatosEmpleado(dni=dato_dni, nombre=dato_nombre, apellidos=dato_apellidos,
            fecha_nac=dato_fecha_nac, domicilio=dato_domicilio)
            self._datos_empleados.append(nuevo_datos_empleado)
    
    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), 'r', encoding="UTF-8") as fichero_empleados:
                lineas = fichero_empleados.readlines()
                for linea in lineas:
                    campos = linea.split(";")
                    primer_campo = str(campos[self.CamposFicheroCsv.CAMPO_0])
                    self._dni_combobox.append(primer_campo)
                return self._dni_combobox

    def del_datos(self, dato_dni):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'empleados.csv'), 'r', encoding="UTF-8") as fichero_empleados:
                lineas = fichero_empleados.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_dni= str(campos[self.CamposFicheroCsv.CAMPO_2].strip())
                    if dato_dni == campo_dato_dni:
                        self._empleados.pop(contador)
                    contador += 1
        except IndexError:
            pass
        
    def del_datos_2(self, dato_dni):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), 'r', encoding="UTF-8") as fichero_datos_empleados:
                lineas = fichero_datos_empleados.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_dni= str(campos[self.CamposFicheroCsv.CAMPO_0].strip())
                    if dato_dni == campo_dato_dni:
                        self._datos_empleados.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass

    def del_empleados_por_del_departamento(self, dato_borrar_departamento):
        try:
            contador = 0
            for empleado in self._empleados:
                if dato_borrar_departamento == empleado._cod_departamento:
                    empleado._cod_departamento = 'DEPT000'
                contador += 1
            if contador == (len(self._empleados)-1):
                return False
            else:
                return True
        except IndexError:
            pass
        
    
    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'empleados.csv'), 'w', encoding="UTF-8") as nuevo_csv_empleados:
            for linea in self._empleados:
                nuevo_csv_empleados.write(f"{str(linea)}\n")
    
        with open(os.path.join(self.RUTA_FICHEROS, 'datos_empleados.csv'), 'w', encoding="UTF-8") as nuevo_csv_datos_empleados:
            for linea in self._datos_empleados:
                nuevo_csv_datos_empleados.write(f"{str(linea)}\n")
        
 