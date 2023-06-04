import unittest

from clases.sucursales import Sucursal

class TestSucursal(unittest.TestCase):
    def test_crear(self):
        sucursal = Sucursal()
        self.assertEqual(sucursal._cod_sucursal, "S344")
        self.assertEqual(sucursal._provincia, "GUADALAJARA")
        self.assertEqual(sucursal._direccion, "PLAZA DE LOS CAÍDOS, 3")

    def test_str(self):
        sucursal = Sucursal("S344", "GUADALAJARA", "PLAZA DE LOS CAÍDOS, 3")
        self.assertEqual("S344;GUADALAJARA;PLAZA DE LOS CAÍDOS, 3", str(sucursal))