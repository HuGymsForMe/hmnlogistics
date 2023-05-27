import tkinter as tk
from tkinter import *
from tkinter import ttk

from almacen.almacen_departamentos import AlmacenDepartamentos

class MenuDepartamentos(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master, app)
        self._app = app
        self.almacen_departamentos = AlmacenDepartamentos(self)

        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ ARTICULOS")
        self.title_departamentos = ttk.Label(self, text="MENÚ DEPARTAMENTOS", font=("Helvetica", 14))
        self.boton_add_departamentos = ttk.Button(self, text="AÑADIR DEPARTAMENTO")
        self.boton_del_departamentos = ttk.Button(self, text="BORRAR DEPARTAMENTO")
        self.boton_lis_departamentos = ttk.Button(self, text="MIS DEPARTAMENTOS")

    def mostrar_menu(self):
        self.title_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()
