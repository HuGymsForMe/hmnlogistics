import unittest

from clases.articulos import Articulo

class TestArticulo(unittest.TestCase):
    def test_crear(self):
        articulo = Articulo()
        self.assertEqual(articulo._cod_articulo, "A302")
        self.assertEqual(articulo._cod_cliente, "C343")
        self.assertEqual(articulo._nombre, "Balón de Joma")
        self.assertEqual(articulo._descripcion, "Balón de Joma 2022")
        self.assertEqual(articulo._categoria, "DEPORTES")
    
    def test_str(self):
        articulo = Articulo("A302", "C343", "Balón de Joma", 
        "Balón de Joma 2022", "DEPORTES")
        self.assertEqual("A302;C343;Balón de Joma;Balón de Joma 2022;DEPORTES", str(articulo))