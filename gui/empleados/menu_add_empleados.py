import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

class AddEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, almacen_departamentos, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.menu_empleados = menu_empleados

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_CODIGO_DEPARTAMENTO = "Código de Departamento:"
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_APELLIDOS = "Apellidos:"
        self.PLACEHOLDER_SALARIO = "Salario:"
        self.PLACEHOLDER_DOMICILIO = "Domicilio:"
        self.PLACEHOLDER_TELEFONO = "Teléfono:"
        self.PLACEHOLDER_TIPO = "Tipo:"

        self.withdraw()
        self.minsize(200, 200)
        self.geometry("200x200+650+100")
        self.maxsize(200, 200)
        self.title("AÑADIR CLIENTE")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_empleado_seleccionado = tk.StringVar()
        self.cod_departamento_seleccionado = tk.StringVar()
        self.dni_seleccionado = tk.StringVar()
        self.nombre_seleccionado = tk.StringVar()
        self.apellidos_seleccionados = tk.StringVar()
        self.fecha_nac_seleccionada = tk.StringVar()
        self.fecha_alta_seleccionado = tk.StringVar()
        self.salario_seleccionado = tk.StringVar()
        self.domicilio_seleccionado = tk.StringVar()
        self.telefono_seleccionado = tk.StringVar()
        self.tipo_seleccionado = tk.StringVar()

        self.title_add_empleados = ttk.Label(self, text="AÑADIR EMPLEADO", font=("Helvetica", 12))
        self.print_cod_departamento = ttk.Label(self, text="CÓDIGO DE DEPARTAMENTO:", font=("Helvetica", 9))
        self.input_cod_departamento = ttk.Entry(self, foreground="gray", textvariable=self.cod_departamento_seleccionado) #COMBOBOX
        self.print_dni = ttk.Label(self, text="DNI:", font=("Helvetica", 9))
        self.input_dni = ttk.Entry(self, foreground="gray", textvariable=self.dni_seleccionado)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.nombre_seleccionado)
        self.print_apellidos = ttk.Label(self, text="APELLIDOS:", font=("Helvetica", 9))
        self.input_apellidos = ttk.Entry(self, foreground="gray", textvariable=self.apellidos_seleccionados)
        self.print_fecha_nac = ttk.Label(self, text="FECHA DE NACIMIENTO:", font=("Helvetica", 9))
        self.input_fecha_nac = ttk.Entry(self, foreground="gray", textvariable=self.fecha_nac_seleccionada) #CALENDAR
        self.print_salario = ttk.Label(self, text="SALARIO:", font=("Helvetica", 9))
        self.input_salario = ttk.Entry(self, foreground="gray", textvariable=self.salario_seleccionado)
        self.print_domicilio = ttk.Label(self, text="DOMICILIO:", font=("Helvetica", 9))
        self.input_domicilio = ttk.Entry(self, foreground="gray", textvariable=self.domicilio_seleccionado)
        self.print_telefono = ttk.Label(self, text="TELÉFONO:", font=("Helvetica", 9))
        self.input_telefono = ttk.Entry(self, foreground="gray", textvariable=self.telefono_seleccionado)
        self.print_tipo = ttk.Label(self, text="TIPO:", font=("Helvetica", 9))
        self.input_tipo = ttk.Entry(self, foreground="gray", textvariable=self.tipo_seleccionado) #COMBOBOX
        self.boton_add_empleados = ttk.Button(self, text="AÑADIR")

    def mostrar_menu(self):
        self.title_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def on_close(self):
       self.withdraw()
       #self.limpiar_campos()
       self.menu_clientes.deiconify()

