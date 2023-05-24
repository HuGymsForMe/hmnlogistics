class Distribuidor:
    def __init__(self, cod_distribuidor, nombre):
        self._cod_distribuidor = cod_distribuidor
        self._nombre = nombre

    def __str__(self):
        return f"{self._cod_distribuidor};{self._nombre}"