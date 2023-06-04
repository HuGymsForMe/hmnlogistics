import unittest

from clases.empleados import Empleado

class TestEmpleado(unittest.TestCase):
    def test_crear(self):
        empleado = Empleado()
        self.assertEqual(empleado._cod_empleado, "EMP234")
        self.assertEqual(empleado._cod_departamento, "DEPT453")
        self.assertEqual(empleado._dni, "03452291L")
        self.assertEqual(empleado._fecha_alta, "2022-09-28")
        self.assertEqual(empleado._salario, 2000)
        self.assertEqual(empleado._telefono, 989302173)
        self.assertEqual(empleado._oficio, "ANALISTA")

    def test_str(self):
        empleado = Empleado("EMP234", "DEPT453", "03452291L", "2022-09-28", 2000, 989302173, "ANALISTA")
        self.assertEqual("EMP234;DEPT453;03452291L;2022-09-28;2000;989302173;ANALISTA", str(empleado))

