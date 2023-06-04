import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.sucursales.menu_add_sucursales import AddSucursales
from gui.sucursales.menu_del_sucursales import DelSucursales
from gui.sucursales.menu_lis_sucursales import LisSucursales

class MenuSucursales(tk.Toplevel):
    def __init__(self, master, app, almacen_sucursales, almacen_departamentos):
        super().__init__(master, app)
        self._app = app
        self.almacen_sucursales = almacen_sucursales
        self.almacen_departamentos = almacen_departamentos
        self.ventana_add_sucursales = AddSucursales(self.master, self.almacen_sucursales, self)
        self.ventana_del_sucursales = DelSucursales(self.master, self.almacen_sucursales, self.almacen_departamentos, self)
        self.ventana_lis_sucursales = LisSucursales(self.master, self.almacen_sucursales, self)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ SUCURSALES")
        self.title_sucursales = ttk.Label(self, text="MENÚ SUCURSALES", font=("Helvetica", 14))
        self.boton_add_sucursales = ttk.Button(self, text="AÑADIR SUCURSAL", command=self.abrir_ventana_add_sucursales)
        self.boton_del_sucursales = ttk.Button(self, text="BORRAR SUCURSAL", command=self.abrir_ventana_del_sucursales)
        self.boton_lis_sucursales = ttk.Button(self, text="MIS SUCURSALES", command=self.abrir_ventana_lis_sucursales)

    def mostrar_menu(self):
        self.deiconify()
        self.title_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()

    def abrir_ventana_add_sucursales(self):
        self.ocultar_menu()
        self.ventana_add_sucursales.mostrar_menu()
        self.ventana_add_sucursales.mainloop()
    
    def abrir_ventana_del_sucursales(self):
        self.ocultar_menu()
        self.ventana_del_sucursales.mostrar_menu()
        self.ventana_del_sucursales.mainloop()

    def abrir_ventana_lis_sucursales(self):
        self.ocultar_menu()
        self.ventana_lis_sucursales.mostrar_menu()
        self.ventana_lis_sucursales.mainloop()
