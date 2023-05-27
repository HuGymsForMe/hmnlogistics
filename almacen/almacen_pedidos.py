import os
from clases.pedidos import Pedido

from almacen.almacen import Almacen

class AlmacenPedidos(Almacen):
    def __init__(self, app):
        self._pedidos = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')

    class CamposFicheroCsv:
        COD_PEDIDO = 0
        COD_DISTRIBUIDOR = 1
        COD_SUCURSAL = 2
        FECHA_PEDIDO = 3
        CANTIDAD_ARTICULOS = 4
        PESO = 5
        PRECIO = 6
        

        @staticmethod
        def opciones():
            return range(AlmacenPedidos.CamposFicheroCsv.COD_PEDIDO,
                        AlmacenPedidos.CamposFicheroCsv.PRECIO+1)

    def cargar_datos(self):
        try:
            with open(os.path.join(self.RUTA_FICHEROS, 'pedidos.csv'), 'r', 
            encoding='UTF-8') as fichero_pedidos:
                lineas = fichero_pedidos.readlines()
                for linea in lineas:
                    datos = linea.split(';')
                    cod_pedido = datos[self.CamposFicheroCsv.COD_PEDIDO].strip()
                    cod_distribuidor = datos[self.CamposFicheroCsv.COD_DISTRIBUIDOR].strip()
                    cod_sucursal = datos[self.CamposFicheroCsv.COD_SUCURSAL].strip()
                    fecha_pedido = str(datos[self.CamposFicheroCsv.FECHA_PEDIDO].strip())
                    cantidad_articulos = datos[self.CamposFicheroCsv.CANTIDAD_ARTICULOS].strip()
                    peso = datos[self.CamposFicheroCsv.PESO].strip()
                    precio = datos[self.CamposFicheroCsv.PRECIO].strip()
                    nuevo_pedido = Pedido(cod_pedido, cod_distribuidor, cod_sucursal, fecha_pedido, cantidad_articulos, peso, precio)
                    self._pedidos.append(nuevo_pedido)
        except IndexError:
            pass
    
    def add_datos(self, dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, 
    dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio):
        for pedido in self._pedidos:
            if dato_cod_pedido == pedido._cod_pedido:
                return True
        else:
            nuevo_pedido = Pedido(cod_pedido=dato_cod_pedido, cod_distribuidor=dato_cod_distribuidor, cod_sucursal=dato_cod_sucursal,
            fecha_pedido=dato_fecha_pedido, cantidad_articulos=dato_num_articulos, peso=dato_peso, precio=dato_precio)
            self._pedidos.append(nuevo_pedido)
            return False

    def sobreescribir_datos(self):
        with open(os.path.join(self.RUTA_FICHEROS, 'pedidos.csv'), 'w', encoding="UTF-8") as nuevo_csv_pedidos:
            for linea in self._pedidos:
                nuevo_csv_pedidos.write(f"{str(linea)}\n")