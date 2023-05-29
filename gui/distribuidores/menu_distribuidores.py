import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.distribuidores.menu_add_distribuidores import AddDistribuidores
from gui.distribuidores.menu_lis_distribuidores import LisDistribuidores
from gui.distribuidores.menu_del_distribuidores import DelDistribuidores

class MenuDistribuidor(tk.Toplevel):
    def __init__(self, master, app, almacen_distribuidores, almacen_pedidos):
        super().__init__(master, app)
        self._app = app
        self.almacen_distribuidores = almacen_distribuidores
        self.almacen_pedidos = almacen_pedidos
        self.ventana_add_distribuidores = AddDistribuidores(self.master, self.almacen_distribuidores, self)
        self.ventana_lis_distribuidores = LisDistribuidores(self.master, self.almacen_distribuidores, self)
        self.ventana_del_distribuidores = DelDistribuidores(self.master, self.almacen_distribuidores, self.almacen_pedidos, self)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ DISTRIBUIDOR")
        self.title_clientes = ttk.Label(self, text="MENÚ DISTRIBUIDORES", font=("Helvetica", 14))
        self.boton_add_distribuidores = ttk.Button(self, text="AÑADIR DISTRIBUIDOR", command=self.abrir_ventana_add_distribuidores)
        self.boton_del_distribuidores = ttk.Button(self, text="BORRAR DISTRIBUIDOR", command=self.abrir_ventana_del_distribuidores)
        self.boton_lis_distribuidores = ttk.Button(self, text="MIS DISTRIBUIDORES", command=self.abrir_ventana_lis_distribuidores)
        #self.boton_del_clientes = ttk.Button(self, text="BORRAR DISTRIBUIDOR", command=self.abrir_ventana_del_clientes)

    def mostrar_menu(self):
        self.deiconify()
        self.title_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()

    def abrir_ventana_add_distribuidores(self):
        self.ocultar_menu()
        self.ventana_add_distribuidores.mostrar_menu()
        self.ventana_add_distribuidores.mainloop()

    def abrir_ventana_del_distribuidores(self):
        self.ocultar_menu()
        self.ventana_del_distribuidores.mostrar_menu()
        self.ventana_del_distribuidores.mainloop()

    def abrir_ventana_lis_distribuidores(self):
        self.ocultar_menu()
        self.ventana_lis_distribuidores.mostrar_menu()
        self.ventana_lis_distribuidores.mainloop()