class Pedido:
    def __init__(self, cod_pedido, cod_distribuidor, cod_sucursal, fecha_pedido, cantidad_articulos, peso, precio):
        self._cod_pedido = cod_pedido #PRIMARY KEY
        self._cod_distribuidor = cod_distribuidor #FOREIGN KEY
        self._cod_sucursal = cod_sucursal #FOREIGN KEY
        self._fecha_pedido = fecha_pedido
        self._cantidad_articulos = cantidad_articulos
        self._peso = peso
        self._precio = precio

    def __str__(self):
        return f"{self._cod_pedido};{self._cod_distribuidor};{self._cod_sucursal};{self._fecha_pedido};{self._cantidad_articulos};{self._peso};{self._precio}"

