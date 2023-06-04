import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.departamentos.menu_add_departamentos import AddDepartamentos
from gui.departamentos.menu_del_departamentos import DelDepartamentos
from gui.departamentos.menu_lis_departamentos import LisDepartamentos

class MenuDepartamentos(tk.Toplevel):
    def __init__(self, master, app, almacen_departamentos, almacen_sucursales, almacen_empleados):
        super().__init__(master, app)
        self._app = app
        self.almacen_departamentos = almacen_departamentos
        self.almacen_sucursales = almacen_sucursales
        self.almacen_empleados = almacen_empleados
        self.ventana_add_departamentos = AddDepartamentos(self.master, self.almacen_departamentos, self.almacen_sucursales, self)
        self.ventana_del_departamentos = DelDepartamentos(self.master, self.almacen_departamentos, self.almacen_empleados, self)
        self.ventana_lis_departamentos = LisDepartamentos(self.master, self.almacen_departamentos, self.almacen_sucursales, self)

        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ DEPARTAMENTOS")
        self.title_departamentos = ttk.Label(self, text="MENÚ DEPARTAMENTOS", font=("Helvetica", 14))
        self.boton_add_departamentos = ttk.Button(self, text="AÑADIR DEPARTAMENTO", command=self.abrir_ventana_add_departamentos)
        self.boton_del_departamentos = ttk.Button(self, text="BORRAR DEPARTAMENTO", command=self.abrir_ventana_del_departamentos)
        self.boton_lis_departamentos = ttk.Button(self, text="MIS DEPARTAMENTOS", command=self.abrir_ventana_lis_departamentos)

    def mostrar_menu(self):
        self.title_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def abrir_ventana_add_departamentos(self):
        self.ocultar_menu()
        self.ventana_add_departamentos.mostrar_menu()
        self.ventana_add_departamentos.mainloop()
    
    def abrir_ventana_del_departamentos(self):
        self.ocultar_menu()
        self.ventana_del_departamentos.mostrar_menu()
        self.ventana_del_departamentos.mainloop()

    def abrir_ventana_lis_departamentos(self):
        self.ocultar_menu()
        self.ventana_lis_departamentos.mostrar_menu()
        self.ventana_lis_departamentos.mainloop()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()
