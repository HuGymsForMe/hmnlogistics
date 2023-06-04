import unittest

from clases.distribuidores import Distribuidor

class TestDistribuidor(unittest.TestCase):
    def test_crear(self):
        distribuidor = Distribuidor()
        self.assertEqual(distribuidor._cod_distribuidor, "D493")
        self.assertEqual(distribuidor._nombre, "GLS")

    def test_str(self):
        distribuidor = Distribuidor("D493", "GLS")
        self.assertEqual("D493;GLS", str(distribuidor))