import os
from clases.empleados import Empleado

from almacen.almacen import Almacen

class AlmacenEmpleados(Almacen):
    def __init__(self, app):
        self._empleados = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')