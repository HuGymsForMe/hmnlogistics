import unittest

from clases.pedidos import Pedido

class TestPedido(unittest.TestCase):
    def test_crear(self):
        pedido = Pedido()
        self.assertEqual(pedido._cod_pedido, "P489")
        self.assertEqual(pedido._cod_distribuidor, "D342")
        self.assertEqual(pedido._cod_sucursal, "S034")
        self.assertEqual(pedido._fecha_pedido, "2024-03-17")
        self.assertEqual(pedido._cantidad_articulos, 4)
        self.assertEqual(pedido._peso, 4.50)
        self.assertEqual(pedido._precio, 3.99)

    def test_str(self):
        pedido = Pedido("P489", "D342", "S034", "2024-03-17", 4, 4.50, 3.99)