import unittest

from clases.clientes import Cliente

class TestCliente(unittest.TestCase):
    def test_crear(self):
        cliente = Cliente()
        self.assertEqual(cliente._cod_cliente, "C457")
        self.assertEqual(cliente._cod_sucursal, "S034")
        self.assertEqual(cliente._nombre, "ADIDAS")

    def test_str(self):
        cliente = Cliente("C457", "S034", "ADIDAS")
        self.assertEqual("C457;S034;ADIDAS", str(cliente))