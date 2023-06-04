import unittest

from almacen.almacen_pedidos import AlmacenPedidos

from clases.pedidos import Pedido

class TestAlmacenPedidos(unittest.TestCase):
    def test_add_pedidos(self):
        #CAMBIAMOS EL CÓDIGO DE PEDIDO QUE ES LO QUE DETERMINA LA IGUALDAD DEL PEDIDO
        pedido1 = Pedido("P402", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido2 = Pedido("P432", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido3 = Pedido("P560", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido4 = Pedido("P402", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)

        arraypedidos = [pedido1, pedido2, pedido3]

        self.assertTrue(pedido1 in arraypedidos)
        self.asssertFalse(pedido4 in arraypedidos)

    def test_del_pedidos(self):
        pedido1 = Pedido("P402", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido2 = Pedido("P432", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido3 = Pedido("P560", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        pedido4 = Pedido("P403", "D932", "S302", "2025-09-20", 4, 4.50, 9.99)
        
        pedido_buscado1 = "P402"
        pedido_buscado2 = "P021"

        arraypedido_buscado = [pedido1, pedido2, pedido3, pedido4]
        self.asssertTrue(pedido_buscado1 in arraypedido_buscado)
        self.assertFalse(pedido_buscado2 in arraypedido_buscado)