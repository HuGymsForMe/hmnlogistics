class DatosEmpleado:
    def __init__(self, dni, nombre, apellidos, fecha_nac, salario, domicilio):
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._fecha_nac = fecha_nac
        self._salario = salario
        self._domicilio = domicilio

    def __str__(self):
        return f"{self._dni};{self._nombre};{self._apellidos};{self._fecha_nac};{self._salario};{self._domicilio}"