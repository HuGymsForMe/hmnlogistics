import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.articulos.menu_add_articulos import AddArticulos
from gui.articulos.menu_del_articulos import DelArticulos
from gui.articulos.menu_lis_articulos import LisArticulos

class MenuArticulos(tk.Toplevel):
    def __init__(self, master, app, almacen_articulos, almacen_clientes):
        super().__init__(master, app)
        self._app = app
        self.almacen_articulos = almacen_articulos
        self.almacen_clientes = almacen_clientes
        self.ventana_add_articulos = AddArticulos(self.master, self.almacen_articulos, self.almacen_clientes, self)
        self.ventana_del_articulos = DelArticulos(self.master, self.almacen_articulos, self)
        self.ventana_lis_articulos = LisArticulos(self.master, self.almacen_articulos, self.almacen_clientes, self)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ ARTICULOS")
        self.title_articulos = ttk.Label(self, text="MENÚ ARTICULOS", font=("Helvetica", 14))
        self.boton_add_articulos = ttk.Button(self, text="AÑADIR ARTÍCULO", command=self.abrir_ventana_add_articulos)
        self.boton_del_articulos = ttk.Button(self, text="BORRAR ARTÍCULO", command=self.abrir_ventana_del_articulos)
        self.boton_lis_articulos = ttk.Button(self, text="MIS ARTÍCULOS", command=self.abrir_ventana_lis_articulos)
        self.boton_mod_articulos = ttk.Button(self, text="MODIFICAR ARTÍCULOS", command=self.abrir_ventana_mod_articulos)
                                
    def mostrar_menu(self):
        self.deiconify()
        self.title_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()

    def abrir_ventana_add_articulos(self):
        self.ocultar_menu()
        self.ventana_add_articulos.mostrar_menu()
        self.ventana_add_articulos.mainloop()
    
    def abrir_ventana_del_articulos(self):
        self.ocultar_menu()
        self.ventana_del_articulos.mostrar_menu()
        self.ventana_del_articulos.mainloop()

    def abrir_ventana_lis_articulos(self):
        self.ocultar_menu()
        self.ventana_lis_articulos.mostrar_menu()
        self.ventana_lis_articulos.mainloop()

    def abrir_ventana_mod_articulos(self):
        self.ocultar_menu()