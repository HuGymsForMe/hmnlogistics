from datetime import datetime, date
import re

class Validator:
    def __init__(self):
        self.formato_fecha = None
        self.formato_dni = None
        self.formato_telefono = None
        self.formato_es_numero = None

    def validador_fecha(self, dato_fecha_pedido):
        fecha_actual = date.today()
        self.formato_fecha = "%Y-%m-%d"  # Cambiar formato a yyyy-mm-dd
        patron_fecha = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{2})$"
        try:
            fecha_pedido = datetime.strptime(dato_fecha_pedido, self.formato_fecha).date()
            if fecha_pedido > fecha_actual:
                return True
        except ValueError:
            pass
        return False

    def validador_dni(self, dato_dni):
        self.formato_dni = r'^\d{8}[A-Za-z]$'
        if re.match(self.formato_dni, dato_dni):
            #PODRÍA VALIDAR LA LETRA DEL DNI
            return True
        return False 

    def validador_telefono(self, dato_telefono):
        self.formato_telefono = r'^\d{9}$'
        if re.match(self.formato_telefono, dato_telefono):
            return True
        return False

    def validador_es_numero(self, dato_introducido):
        self.formato_es_numero = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
        return re.match(self.formato_es_numero, dato_introducido) is not None
