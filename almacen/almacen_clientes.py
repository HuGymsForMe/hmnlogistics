import os
from clases.clientes import Cliente

from almacen.almacen import Almacen

class AlmacenClientes(Almacen):
    def __init__(self, app):
        self._cod_cliente_combobox = []
        self._clientes = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')
        self.CAMPO_COD_CLIENTE = 0

    class CamposFicheroCsv:
        COD_CLIENTE = 0
        COD_SUCURSAL = 1
        NOMBRE = 2

        @staticmethod
        def opciones():
            return range(AlmacenClientes.CamposFicheroCsv.COD_CLIENTE,
                        AlmacenClientes.CamposFicheroCsv.NOMBRE+1)

    @property
    def clientes(self):
        return self._clientes

    def cargar_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', 
        encoding='UTF-8') as fichero_clientes:
            lineas = fichero_clientes.readlines()
            for linea in lineas:
                datos = linea.split(';')
                cod_cliente = datos[self.CamposFicheroCsv.COD_CLIENTE].strip()
                cod_sucursal = datos[self.CamposFicheroCsv.COD_SUCURSAL].strip()
                nombre = str(datos[self.CamposFicheroCsv.NOMBRE].strip())
                nuevo_cliente = Cliente(cod_cliente, cod_sucursal, nombre)
                self._clientes.append(nuevo_cliente)

    def add_datos(self, dato_cod_cliente, dato_cod_sucursal, dato_nombre):
        for cliente in self._clientes:
            if dato_cod_cliente == cliente._cod_cliente or dato_nombre == cliente._nombre:
                return True
        else:
            nuevo_cliente = Cliente(cod_cliente=dato_cod_cliente, cod_sucursal=dato_cod_sucursal, nombre=dato_nombre)
            self._clientes.append(nuevo_cliente)
            return False

    def generar_combobox(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
                lineas = fichero_clientes.readlines()
                for linea in lineas:
                    campos = linea.split(";")
                    primer_campo = str(campos[self.CAMPO_COD_CLIENTE])
                    self._cod_cliente_combobox.append(primer_campo)
                return self._cod_cliente_combobox

    def del_datos(self, dato_borrar_cliente):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'r', encoding="UTF-8") as fichero_clientes:
                lineas = fichero_clientes.readlines()
                contador = 0
                for linea in lineas:
                    campos = str(linea).split(';')
                    campo_dato_borrar_cliente = str(campos[self.CAMPO_COD_CLIENTE].strip())
                    if dato_borrar_cliente == campo_dato_borrar_cliente:
                        self._clientes.pop(contador)
                        return True
                    contador += 1
                return False
        except IndexError:
            pass

    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'clientes.csv'), 'w', encoding="UTF-8") as nuevo_csv_clientes:
            for linea in self._clientes:
                nuevo_csv_clientes.write(f"{str(linea)}\n")


