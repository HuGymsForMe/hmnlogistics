from datetime import datetime, date
import re

class Validator:
    def __init__(self):
        self.formato_fecha = None

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
