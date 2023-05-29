import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.pedidos.menu_add_pedidos import AddPedidos
from gui.pedidos.menu_del_pedidos import DelPedidos
from gui.pedidos.menu_lis_pedidos import LisPedidos

class MenuPedido(tk.Toplevel):
    def __init__(self, master, app, almacen_pedidos, almacen_distribuidores, almacen_sucursales):
        super().__init__(master)
        self._app = app
        self.almacen_pedidos = almacen_pedidos
        self.almacen_distribuidores = almacen_distribuidores
        self.almacen_sucursales = almacen_sucursales
        self.ventana_add_pedidos = AddPedidos(self.master, self.almacen_pedidos, self.almacen_sucursales, self.almacen_distribuidores, self)
        self.ventana_del_pedidos = DelPedidos(self.master, self.almacen_pedidos, self)
        self.ventana_lis_pedidos = LisPedidos(self.master, self.almacen_pedidos, self.almacen_sucursales, self.almacen_distribuidores, self)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ PEDIDOS")
        self.title_pedidos = ttk.Label(self, text="MENÚ PEDIDOS", font=("Helvetica", 14))
        self.boton_add_pedidos = ttk.Button(self, text="AÑADIR PEDIDO", command=self.abrir_ventana_add_pedidos)
        self.boton_del_pedidos = ttk.Button(self, text="BORRAR PEDIDO", command=self.abrir_ventana_del_pedidos)
        self.boton_lis_pedidos = ttk.Button(self, text="MIS PEDIDOS", command=self.abrir_ventana_lis_pedidos)

    def mostrar_menu(self):
        self.deiconify()
        self.title_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()

    def abrir_ventana_add_pedidos(self):
        self.ocultar_menu()
        self.ventana_add_pedidos.mostrar_menu()
        self.ventana_add_pedidos.mainloop()

    def abrir_ventana_del_pedidos(self):
        self.ocultar_menu()
        self.ventana_del_pedidos.mostrar_menu()
        self.ventana_del_pedidos.mainloop()

    def abrir_ventana_lis_pedidos(self):
        self.ocultar_menu()
        self.ventana_lis_pedidos.mostrar_menu()
        self.ventana_lis_pedidos.mainloop()
