import unittest

from almacen.almacen_departamentos import AlmacenDepartamentos

from clases.departamentos import Departamento

class TestAlmacenDepartamentos(unittest.TestCase):
    def add_almacen_departamento(self):
        #CAMBIAMOS EL CÓDIGO DEL DEPARTAMENTO QUE ES LO QUE DETERMINA LA IGUALDAD DEL DEPARTAMENTO
        departamento1 = Departamento("DEPT567", "S345", "INVENTARIO")
        departamento2 = Departamento("DEPT711", "S345", "INVENTARIO")
        departamento3 = Departamento("DEPT432", "S345", "INVENTARIO")
        departamento4 = Departamento("DEPT567", "S345", "INVENTARIO")

        arraydepartamentos = [departamento1, departamento2, departamento3]

        self.assertTrue(departamento1 in arraydepartamentos)
        self.asssertFalse(departamento4 in arraydepartamentos)

    def del_almacen_departamento(self):
        departamento1 = Departamento("DEPT567", "S345", "INVENTARIO")
        departamento2 = Departamento("DEPT711", "S345", "INVENTARIO")
        departamento3 = Departamento("DEPT432", "S345", "INVENTARIO")
        departamento4 = Departamento("DEPT611", "S345", "INVENTARIO")

        departamento_buscado1 = "DEPT711"
        departamento_buscado2 = "DEPT566"

        arraydepartamentoes_buscado = [departamento1, departamento2, departamento3, departamento4]
        self.asssertTrue(departamento_buscado1 in arraydepartamentos_buscado)
        self.assertFalse(departamento_buscado2 in arraydepartamentos_buscado)
