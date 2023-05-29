import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.clientes.menu_add_clientes import AddClientes
from gui.clientes.menu_del_clientes import DelClientes
from gui.clientes.menu_lis_clientes import LisClientes

class MenuClientes(tk.Toplevel):
    def __init__(self, master, app, almacen_clientes, almacen_sucursales, almacen_articulos):
        super().__init__(master, app)
        self._app = app
        self.almacen_clientes = almacen_clientes
        self.almacen_sucursales = almacen_sucursales
        self.almacen_articulos = almacen_articulos
        self.ventana_add_clientes = AddClientes(self.master, self.almacen_clientes, self.almacen_sucursales, self)
        self.ventana_del_clientes = DelClientes(self.master, self.almacen_clientes, self.almacen_articulos, self)
        self.ventana_lis_clientes = LisClientes(self.master, self.almacen_clientes, self.almacen_sucursales, self)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ CLIENTES")
        self.title_clientes = ttk.Label(self, text="MENÚ CLIENTES", font=("Helvetica", 14))
        self.boton_add_clientes = ttk.Button(self, text="AÑADIR CLIENTE", command=self.abrir_ventana_add_clientes)
        self.boton_del_clientes = ttk.Button(self, text="BORRAR CLIENTE", command=self.abrir_ventana_del_clientes)
        self.boton_lis_clientes = ttk.Button(self, text="MIS CLIENTES", command=self.abrir_ventana_lis_clientes)

    def mostrar_menu(self):
        self.deiconify()
        self.title_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()

    def abrir_ventana_add_clientes(self):
        self.ocultar_menu()
        self.ventana_add_clientes.mostrar_menu()
        self.ventana_add_clientes.mainloop()

    def abrir_ventana_del_clientes(self):
        self.ocultar_menu()
        self.ventana_del_clientes.mostrar_menu()
        self.ventana_del_clientes.mainloop()

    def abrir_ventana_lis_clientes(self):
        self.ocultar_menu()
        self.ventana_lis_clientes.mostrar_menu()
        self.ventana_lis_clientes.mainloop()