import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.empleados.menu_add_empleados import AddEmpleados

class MenuEmpleados(tk.Toplevel):
    def __init__(self, master, app, almacen_empleados, almacen_departamentos):
        super().__init__(master, app)
        self._app = app
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.ventana_add_empleados = AddEmpleados(self.master, self.almacen_empleados, self.almacen_departamentos, self)

        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.minsize(300, 200)
        self.geometry("300x200+700+100")
        self.maxsize(300, 200)
        self.title("MENÚ EMPLEADOS")
        self.title_empleados = ttk.Label(self, text="MENÚ EMPLEADOS", font=("Helvetica", 14))
        self.boton_add_empleados = ttk.Button(self, text="AÑADIR EMPLEADO", command=self.abrir_ventana_add_empleados)
        self.boton_del_empleados = ttk.Button(self, text="BORRAR EMPLEADO")
        self.boton_lis_empleados = ttk.Button(self, text="MIS EMPLEADOS")

    def mostrar_menu(self):
        self.title_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_lis_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def ocultar_menu(self):
        self.withdraw()

    def abrir_ventana_add_empleados(self):
        self.ocultar_menu()
        self.ventana_add_empleados.mostrar_menu()
        self.ventana_add_empleados.mainloop()

    def on_close(self):
        self.ocultar_menu()
        self.master.deiconify()
