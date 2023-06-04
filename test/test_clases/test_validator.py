import unittest

from clases.validator import Validator

class TestValidator(unittest.TestCase):
    def test_validador_fecha(self):
        #VALIDA UNA FECHA POSTERIOR A LA ACTUAL CON FORMATO 'YYYY-MM-DD'
        fecha1 = '2030-03-12'
        fecha2 = '2020-03-12'
        fecha3 = 2020
        self.assertTrue(fecha1)
        self.assertFalse(fecha2)
        self.assertFalse(fecha3)

    def test_validador_dni(self):
        dni1 = '03222782E'
        dni2 = '03222782EB'
        dni3 = 32227829
        self.assertTrue(dni1)
        self.assertFalse(dni2)
        self.assertFalse(dni3)

    def test_validador_telefono(self):
        telefono1 = 934201342
        telefono2 = 74862598665868 #+9 Números
        telefono3 = '934567823' #Telefono debe de ser de tipo 'int'
        telefono4 = 'bhfiuewhig' 
        self.assertTrue(telefono1)
        self.assertFalse(telefono2)
        self.assertFalse(telefono3)
        self.assertFalse(telefono4)

    def test_validador_es_numero(self):
        #ACEPTA TANTO 'INT' COMO 'FLOAT'
        es_numero1 = 354553
        es_numero2 = 3.45
        es_numero3 = '3.45'
        es_numero4 = 'fkjewbvkew'
        self.assertTrue(es_numero1)
        self.assertTrue(es_numero2)
        self.assertFalse(es_numero3)
        self.assertFalse(es_numero4)