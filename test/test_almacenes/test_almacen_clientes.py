import unittest

from almacen.almacen_clientes import AlmacenClientes

from clases.clientes import Cliente

class TestAlmacenClientes(unittest.TestCase):
    def test_add_cliente(self):
        #CAMBIAMOS EL CÓDIGO DE CLIENTE QUE ES LO QUE DETERMINA LA IGUALDAD DEL CLIENTE
        cliente1 = Cliente("C453", "S456","ADIDAS")
        cliente2 = Cliente("C567", "S456","ADIDAS")
        cliente3 = Cliente("C320", "S456","ADIDAS")
        cliente4 = Cliente("C378", "S456","ADIDAS")

        arrayclientes = [cliente1, cliente2, cliente3]

        self.assertTrue(cliente1 in arrayclientes)
        self.asssertFalse(cliente4 in arrayclientes)

    def test_del_cliente(self):
        cliente1 = Cliente("C453", "S456","ADIDAS")
        cliente2 = Cliente("C567", "S456","ADIDAS")
        cliente3 = Cliente("C320", "S456","ADIDAS")
        cliente4 = Cliente("C360", "S456","ADIDAS")

        cliente_buscado1 = "C567"
        cliente_buscado2 = "C566"

        arraycliente_buscado = [cliente1, cliente2, cliente3, cliente4]
        self.asssertTrue(cliente_buscado1 in arraycliente_buscado)
        self.assertFalse(cliente_buscado2 in arraycliente_buscado)

