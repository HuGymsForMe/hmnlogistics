import re
import abc
from datetime import datetime, date

class Validator:
    @staticmethod
    def __init__(self):
        #self.patron_dni = r'^\d{8}[A-Za-z]$'
        #self.patron_telef = r'^\d{9}$'
        self.formato_fecha = None

    def validador_fecha(self, dato_fecha_pedido):
        fecha_actual = date.today()
        self.formato_fecha = "%d/%m/%y"
        patron_fecha = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{2})$"
        if re.match(patron_fecha, dato_fecha_pedido.strftime(self.formato_fecha)):
            if dato_fecha_pedido > fecha_actual:
                return True
        return False