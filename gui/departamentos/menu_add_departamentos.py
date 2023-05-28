import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class AddDepartamentos(tk.Toplevel):
    def __init__(self, master, almacen_departamentos, almacen_sucursales, menu_departamentos):
        super().__init__(master)
        self.almacen_departamentos = almacen_departamentos
        self.almacen_sucursales = almacen_sucursales
        self.menu_departamentos = menu_departamentos

        self.withdraw()
        self.minsize(200, 200)
        self.geometry("200x200+650+100")
        self.maxsize(200, 200)
        self.title("AÑADIR DEPARTAMENTO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        #FORMATO PLACEHOLDER
        self.PLACEHOLDER_COD_SUCURSAL = "Código de sucursal:"
        self.PLACEHOLDER_NOMBRE = "Nombre:"

        self.cod_sucursal_seleccionado = tk.StringVar()
        self.nombre_seleccionado = tk.StringVar()

        self.title_add_empleados = ttk.Label(self, text="AÑADIR EMPLEADO", font=("Helvetica", 12))
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_seleccionado, foreground="gray")
        self.eleccion_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
        self.eleccion_sucursal.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_sucursal)
        self.eleccion_sucursal.bind('<FocusOut>', self.set_placeholder_eleccion_cod_sucursal)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.nombre_seleccionado)
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.boton_add_departamentos = ttk.Button(self, text="AÑADIR", command=self.comprobar_departamentos)

    def mostrar_menu(self):
        self.actualizar_posibles_sucursales()
        self.title_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def recoger_datos_departamentos(self):
        dato_cod_departamento = f"DEPT{str(random.randrange(1,1001))}"
        dato_cod_sucursal = self.cod_sucursal_seleccionado.get()
        dato_nombre = self.nombre_seleccionado.get().upper()
        return dato_cod_departamento, dato_cod_sucursal, dato_nombre

    def comprobar_departamentos(self):
        dato_cod_departamento, dato_cod_sucursal, dato_nombre = self.recoger_datos_departamentos()
        datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE DEPARTAMENTO: {dato_cod_departamento}\nCÓDIGO DE SUCURSAL: {dato_cod_sucursal}\nNOMBRE: {dato_nombre}")
        if datos:
            if self.almacen_departamentos.add_datos(dato_cod_departamento, dato_cod_sucursal, dato_nombre):
                cod_repetido = messagebox.showinfo(message="EL DEPARTAMENTO YA SE ENCUENTRA EN EL SISTEMA")

    def actualizar_posibles_sucursales(self):
        self.posibles_sucursales = self.almacen_sucursales.generar_combobox()
        self.eleccion_sucursal['values'] = self.posibles_sucursales

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_sucursal.get() == self.PLACEHOLDER_COD_SUCURSAL:
            self.eleccion_sucursal.delete(0, tk.END)
            self.eleccion_sucursal.config(foreground='black')

    def set_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_sucursal.get() == "":
            self.eleccion_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
            self.eleccion_sucursal.config(foreground='gray')

    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
            self.input_nombre.config(foreground='gray')

    def ocultar_menu(self):
        self.withdraw()

    def on_close(self):
        self.ocultar_menu()
        self.menu_departamentos.deiconify()

    def limpiar_campos(self):
        self.cod_sucursal_seleccionado.set('')
        self.set_placeholder_input_nombre(None)
        self.nombre_seleccionado.set('')
        self.set_placeholder_input_nombre(None)
