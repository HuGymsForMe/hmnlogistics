import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class ModDatosEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, dni_var, nombre_var, apellidos_var, 
    fecha_nac_var, domicilio_var, menu_lis_datos_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.dni_var = dni_var
        self.nombre_var = nombre_var
        self.apellidos_var = apellidos_var
        self.fecha_nac_var = fecha_nac_var
        self.domicilio_var = domicilio_var
        self.menu_lis_datos_empleados = menu_lis_datos_empleados

        self.withdraw()
        self.minsize(350, 450)
        self.geometry("350x450+650+100")
        self.maxsize(350, 450)
        self.title("MODIFICAR EMPLEADO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.print_dni = ttk.Label(self, text="DNI:", font=("Helvetica", 9))
        self.input_dni = ttk.Entry(self, textvariable=self.dni_var, state='readonly')
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, textvariable=self.nombre_var)
        self.print_apellidos = ttk.Label(self, text="APELLIDOS:", font=("Helvetica", 9))
        self.input_apellidos = ttk.Entry(self, textvariable=self.apellidos_var)
        self.print_fecha_nac = ttk.Label(self, text="FECHA DE NACIMIENTO:", font=("Helvetica", 9))
        self.input_fecha_nac = ttk.Entry(self, textvariable=self.fecha_nac_var, state='readonly')
        self.print_domicilio = ttk.Label(self, text="DOMICILIO:", font=("Helvetica", 9))
        self.input_domicilio = ttk.Entry(self, textvariable=self.domicilio_var)
        self.boton_mod_empleado = ttk.Button(self, text="REALIZAR CAMBIOS", command=self.realizar_modificaciones)

    def mostrar_menu(self):
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_fecha_nac.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_fecha_nac.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_empleado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def realizar_modificaciones(self):
        dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio = self.menu_lis_datos_empleados.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL EMPLEADO?")
        if reaviso:
            self.almacen_empleados.del_datos_2(dato_dni)
            self.almacen_empleados.add_datos_2(dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio)
            messagebox.showinfo(message="EL EMPLEADO SE MODIFICÓ CORRECTAMENTE")
            self.on_close()
        else:
            datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_close(self):
        self.withdraw()
        self.menu_lis_datos_empleados.deiconify()