import unittest

from almacen.almacen_sucursales import AlmacenSucursales

from clases.sucursales import Sucursal

class TestAlmacenSucursales(unittest.TestCase):
    def test_add_sucursal(self):
        #CAMBIAMOS EL CÓDIGO DE LA SUCURSAL Y EL NOMBRE QUE ES LO QUE DETERMINA LA IGUALDAD DE LA SUCURSAL
        sucursal1 = Sucursal("S302", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal2 = Sucursal("S356", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal3 = Sucursal("S782", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal4 = Sucursal("S302", "GUADALAJARA", "CALLE EL OLIVO, 12")

        arraysucursales = [sucursal1, sucursal2, sucursal3]

        self.assertTrue(sucursal1 in arraysucursales)
        self.asssertFalse(sucursal4 in arraysucursales)

    def test_del_sucursal(self):
        sucursal1 = Sucursal("S302", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal2 = Sucursal("S356", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal3 = Sucursal("S782", "GUADALAJARA", "CALLE EL OLIVO, 12")
        sucursal4 = Sucursal("S453", "GUADALAJARA", "CALLE EL OLIVO, 12")

        sucursal_buscado1 = "D903"
        sucursal_buscado2 = "D566"

        arraysucursales_buscado = [sucursal1, sucursal2, sucursal3, sucursal4]
        self.asssertTrue(sucursal_buscado1 in arraysucursales_buscado)
        self.assertFalse(sucursal_buscado2 in arraysucursales_buscado)