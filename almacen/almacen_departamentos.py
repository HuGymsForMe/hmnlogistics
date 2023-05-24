import os
from clases.departamentos import Departamento

from almacen.almacen import Almacen

class AlmacenDepartamentos(Almacen):
    def __init__(self, app):
        self._departamentos = []
        self._app = app
        self.RUTA_FICHEROS = os.path.abspath('../hmnlogistics/files')