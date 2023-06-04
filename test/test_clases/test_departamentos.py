import unittest

from clases.departamentos import Departamento

class TestDepartamento(unittest.TestCase):
    def test_crear(self):
        departamento = Departamento()
        self.assertEqual(departamento._cod_departamento, "DEPT459")
        self.assertEqual(departamento._cod_sucursal, "S602")
        self.assertEqual(departamento._nombre, "INVENTARIO")

    def test_str(self):
        departamento = Departamento("DEPT459", "S602", "INVENTARIO")
        self.assertEqual("DEPT459;S602;INVENTARIO", str(departamento))