import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.empleados.menu_add_empleados import AddEmpleados
from gui.empleados.menu_del_empleados import DelEmpleados
from gui.empleados.menu_lis_empleados import LisEmpleados
from gui.empleados.menu_lis_datos_empleados import LisDatosEmpleados

class MenuEmpleados(tk.Toplevel):
    def __init__(self, master, app, almacen_empleados, almacen_departamentos):
        super().__init__(master, app)
        self._app = app
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.ventana_add_empleados = AddEmpleados(self.master, self.almacen_empleados, self.almacen_departamentos, self)
        self.ventana_del_empleados = DelEmpleados(self.master, self.almacen_empleados, self)
        self.ventana_lis_empleados = LisEmpleados(self.master, self.almacen_empleados, self.almacen_departamentos, self)
        self.ventana_lis_datos_empleados = LisDatosEmpleados(self.master, self.almacen_empleados, self)

        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(350, 233)
        self.geometry("350x233+700+100")
        self.maxsize(350, 233)
        self.title("MENÚ EMPLEADOS")
        self.title_empleados = ttk.Label(self, text="MENÚ EMPLEADOS", font=("Helvetica", 14))
        self.boton_add_empleados = ttk.Button(self, text="AÑADIR EMPLEADO", command=self.abrir_ventana_add_empleados)
        self.boton_del_empleados = ttk.Button(self, text="BORRAR EMPLEADO", command=self.abrir_ventana_del_empleados)
        self.boton_lis_empleados = ttk.Button(self, text="GESTIÓN DE LOS EMPLEADOS", command=self.abrir_ventana_lis_empleados)
        self.boton_lis_datos_empleados = ttk.Button(self, text="DATOS DE LOS EMPLEADOS", command=self.abrir_ventana_lis_datos_empleados)

    def mostrar_menu(self):
        self.title_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_datos_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def abrir_ventana_add_empleados(self):
        self.ocultar_menu()
        self.ventana_add_empleados.mostrar_menu()
        self.ventana_add_empleados.mainloop()

    def abrir_ventana_del_empleados(self):
        self.ocultar_menu()
        self.ventana_del_empleados.mostrar_menu()
        self.ventana_del_empleados.mainloop()

    def abrir_ventana_lis_empleados(self):
        self.ocultar_menu()
        self.ventana_lis_empleados.mostrar_menu()
        self.ventana_lis_empleados.mainloop()

    def abrir_ventana_lis_datos_empleados(self):
        self.ocultar_menu()
        self.ventana_lis_datos_empleados.mostrar_menu()
        self.ventana_lis_datos_empleados.mainloop()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()
