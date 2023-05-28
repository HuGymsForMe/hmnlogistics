class Empleado:
    def __init__(self, cod_empleado, cod_departamento, dni, nombre, apellidos, 
    fecha_nac, fecha_alta, salario, domicilio, telefono):
        self._cod_empleado = cod_empleado
        self._cod_departamento = cod_departamento
        self._dni = dni
        self._fecha_alta = fecha_alta
        self._salario = salario
        self._telefono = telefono
        self._tipo = tipo

    def __str__(self):
        return f"{self._cod_empleado};{self._cod_departamento};{self._dni};{self._fecha_alta};{self._salario};{self._telefono};{self._tipo}"

#PODEMOS PLANTEAR DOS LISTADOS, UNO CON TODOS LOS ATRIBUTOS Y OTRO CON ALGUNOS QUE NECESITEMOS PARA ALGO CONCRETO