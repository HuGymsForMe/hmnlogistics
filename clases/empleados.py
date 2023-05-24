class Empleado:
    def __init__(self, cod_empleado, cod_departamento, dni, nombre, apellidos, 
    fecha_nac, fecha_alta, salario, domicilio, telefono):
        self._cod_empleado = cod_empleado
        self._cod_departamento = cod_departamento
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._fecha_nac = fecha_nac
        self._fecha_alta = fecha_alta
        self._salario = salario
        self._domicilio = domicilio
        self._telefono = telefono

    def __str__(self):
        return f"{self._cod_empleado};{self._cod_departamento};{self._dni};{self._nombre};\n\
{self._apellidos};{self._fecha_nac};{self._fecha_alta};{self._salario};{self._domicilio};{self._telefono}"