class Sucursal:
    def __init__(self, cod_sucursal, provincia, direccion):
        self._cod_sucursal = cod_sucursal #PRIMARY KEY
        self._provincia = provincia
        self._direccion = direccion

    def __str__(self):
        return f"{self._cod_sucursal};{self._provincia};{self._direccion}"