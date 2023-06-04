import unittest

from almacen.almacen_distribuidores import AlmacenDistribuidores

from clases.distribuidores import Distribuidor

class TestAlmacenDistribuidor(unittest.TestCase):
    def test_add_distribuidor(self):
        #CAMBIAMOS EL CÓDIGO DEL DISTRIBUIDOR Y EL NOMBRE QUE ES LO QUE DETERMINA LA IGUALDAD DEL DISTRIBUIDOR
        distribuidor1 = Distribuidor("D903", "GLS")
        distribuidor2 = Distribuidor("D450", "NACEX")
        distribuidor3 = Distribuidor("D034", "CORREOS")
        distribuidor4 = Distribuidor("D903", "GLS")

        arraydistribuidores = [distribuidor1, distribuidor2, distribuidor3]

        self.assertTrue(distribuidor1 in arraydistribuidores)
        self.asssertFalse(distribuidor4 in arraydistribuidores)

    def test_del_distribuidor(self):
        distribuidor1 = Distribuidor("D903", "GLS")
        distribuidor2 = Distribuidor("D450", "NACEX")
        distribuidor3 = Distribuidor("D034", "CORREOS")
        distribuidor4 = Distribuidor("D402", "MRW")

        distribuidor_buscado1 = "D903"
        distribuidor_buscado2 = "D566"

        arraydistribuidores_buscado = [distribuidor1, distribuidor2, distribuidor3, distribuidor4]
        self.asssertTrue(distribuidor_buscado1 in arraydistribuidores_buscado)
        self.assertFalse(distribuidor_buscado2 in arraydistribuidores_buscado)
