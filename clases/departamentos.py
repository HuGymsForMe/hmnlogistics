class Departamento:
    def __init__(self, cod_departamento, cod_sucursal, nombre):
        self._cod_departamento = cod_departamento
        self._cod_sucursal = cod_sucursal
        self._nombre = nombre

    def __str__(self):
        return f"{self._cod_departamento};{self._cod_sucursal};{self._nombre}"
