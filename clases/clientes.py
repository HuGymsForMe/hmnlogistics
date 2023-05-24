class Cliente:
    def __init__(self, cod_cliente, cod_sucursal, nombre):
        self._cod_cliente = cod_cliente #PRIMARY KEY
        self._cod_sucursal = cod_sucursal #FOREIGN KEY
        self._nombre = nombre

    def __str__(self):
        return f"{self._cod_cliente};{self._cod_sucursal};{self._nombre}"
