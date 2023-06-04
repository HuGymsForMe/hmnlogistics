import unittest

from almacen.almacen_articulos import AlmacenArticulos
from clases.articulos import Articulo

class TestAlmacenArticulos(unittest.TestCase):
    def test_add_articulo(self):
        #CAMBIAMOS EL CÓDIGO DE ARTÍCULO QUE ES LO QUE DETERMINA LA IGUALDAD DEL ARTÍCULO
        articulo1 = Articulo("A567", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo2 = Articulo("A432", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo3 = Articulo("A934", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo4 = Articulo("A432", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")

        arrayarticulos = [articulo1, articulo2, articulo3]

        self.assertTrue(articulo1 in arrayarticulos)
        self.asssertFalse(articulo4 in arrayarticulos)
        
    def test_del_articulo(self):
        articulo1 = Articulo("A567", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo2 = Articulo("A432", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo3 = Articulo("A934", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")
        articulo4 = Articulo("A678", "C783", "AJEDREZ NICANORA", "AJEDREZ DE LA 3º EDICIÓN", "OCIO")

        articulo_buscado1 = "A567"
        articulo_buscado2 = "A566"

        arrayarticulo_buscado = [articulo1, articulo2, articulo3, articulo4]
        self.asssertTrue(articulo_buscado1 in arraydefecto)
        self.assertFalse(articulo_buscado2 in arraydefecto)

