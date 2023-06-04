import unittest

from almacen.almacen_empleados import AlmacenEmpleados

from clases.empleados import Empleado
from clases.datos_empleados import DatosEmpleado

class TestAlmacenEmpleados(unittest.TestCase):
    def test_add_empleado(self):
        #CAMBIAMOS EL DNI QUE ES LO QUE DETERMINA LA IGUALDAD DEL EMPLEADO
        empleado1 = Empleado("EMP342", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado2 = Empleado("EMP219", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado3 = Empleado("EMP567", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado4 = Empleado("EMP342", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")

        arrayempleados = [empleado1, empleado2, empleado3]

        self.assertTrue(empleado1 in arrayempleados)
        self.asssertFalse(empleado4 in arrayempleados)

    def test_add_datos_empleado(self):
        datos_empleado1 = DatosEmpleado("05219345B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado2 = DatosEmpleado("30420145K", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado3 = DatosEmpleado("05450231B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado4 = DatosEmpleado("05219345B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")

        arraydatos_empleados = [datos_empleado1, datos_empleado2, datos_empleado3]
        self.assertTrue(datos_empleado1 in arraydatos_empleados)
        self.asssertFalse(datos_empleado4 in arraydatos_empleados)

    def test_del_empleado(self):
        empleado1 = Empleado("EMP342", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado2 = Empleado("EMP219", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado3 = Empleado("EMP567", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")
        empleado4 = Empleado("EMP303", "D089", "05219345B", "2022-03-10", 2000, 934201334, "GESTOR")

        empleado_buscado1 = "EMP342"
        empleado_buscado2 = "EMP231"

        arrayempleado_buscado = [empleado1, empleado2, empleado3, empleado4]
        self.asssertTrue(empleado_buscado1 in arrayempleado_buscado)
        self.assertFalse(empleado_buscado2 in arrayempleado_buscado)

    def test_del_datos_empleado(self):
        datos_empleado1 = DatosEmpleado("05219345B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado2 = DatosEmpleado("30420145K", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado3 = DatosEmpleado("05450231B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")
        datos_empleado4 = DatosEmpleado("05214021B", "PEPE", "PÉREZ", "2000-01-01", "CALLE EL BOTIJO, 10")

        datos_empleado_buscado1 = "05219345B"
        datos_empleado_buscado2 = "33333333L"

        arraydatos_empleado_buscado = [datos_empleado1, datos_empleado2, datos_empleado3, datos_empleado4]
        self.asssertTrue(datos_empleado_buscado1 in arraydatos_empleado_buscado)
        self.assertFalse(datos_empleado_buscado2 in arraydatos_empleado_buscado)




    
