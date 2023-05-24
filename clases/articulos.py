class Articulo:
    def __init__(self, cod_articulo, cod_cliente, nombre, descripcion, categoria):
        self._cod_articulo = cod_articulo #PRIMARY KEY
        self._cod_cliente = cod_cliente #FOREIGN KEY
        self._nombre = nombre
        self._descripcion = descripcion
        self._categoria = categoria

    def __str__(self):
        return f"{self._cod_articulo};{self._cod_cliente};{self._nombre};{self._descripcion};{self._categoria}"