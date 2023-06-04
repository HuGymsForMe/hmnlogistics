import unittest

from clases.datos_empleados import DatosEmpleado

class TestDatosEmpleado(unittest.TestCase):
    def test_crear(self):
        datos_empleado = DatosEmpleado()
        self.assertEqual(datos_empleado._dni, "03452219H")
        self.assertEqual(datos_empleado._nombre, "PEDRO")
        self.assertEqual(datos_empleado._apellidos, "PÉREZ CABEZAS")
        self.assertEqual(datos_empleado._fecha_nac, "2000-01-01")
        self.assertEqual(datos_empleado._domicilio, "CALLE LA ROSA, 94")

    def test_str(self):
        datos_empleado = DatosEmpleado("03452219H", "PEDRO", "PÉREZ CABEZAS", "2000-01-01", "CALLE DE LA ROSA, 94")
        self.assertEqual("03452219H;PEDRO;PÉREZ CABEZAS;2000-01-01;CALLE DE LA ROSA, 94", str(datos_empleado))
