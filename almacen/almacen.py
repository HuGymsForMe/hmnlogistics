from abc import ABC, abstractmethod

class Almacen(ABC):
    #@abstractmethod
    def cargar_datos(self):
        pass

    #@abstractmethod
    def add_datos(self):
        pass
    
    #@abstractmethod
    def del_datos(self):
        pass

    #@abstractmethod
    def sobreescribir_datos(self):
        pass