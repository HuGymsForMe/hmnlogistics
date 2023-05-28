import tkinter as tk
from gui.menuhmn import MenuHmn

import os

class Programa:
    def __init__(self):
        self.almacen = {}
        self.root = tk.Tk()
        self.menu = MenuHmn(self.root, self.almacen)

    def main(self):
        self.menu.ventana_sucursal.almacen_sucursales.cargar_datos()
        self.menu.ventana_cliente.almacen_clientes.cargar_datos()
        self.menu.ventana_articulo.almacen_articulos.cargar_datos()
        self.menu.ventana_distribuidor.almacen_distribuidores.cargar_datos()
        self.menu.ventana_pedidos.almacen_pedidos.cargar_datos()
        self.menu.ventana_departamentos.almacen_departamentos.cargar_datos()
        #self.menu.ventana_empleados.almacen_empleados.cargar_datos()
        self.menu.main()
        self.root.mainloop()

if __name__ == "__main__":
    Programa().main()