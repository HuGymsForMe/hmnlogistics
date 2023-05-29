from tkcalendar import DateEntry
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

from clases.validator import Validator

class AddEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, almacen_departamentos, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.menu_empleados = menu_empleados
        self.no_mostrar_calendario = True
        self.validador = Validator()

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_CODIGO_DEPARTAMENTO = "Código de Departamento:"
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_APELLIDOS = "Apellidos:"
        self.PLACEHOLDER_SALARIO = "Salario:"
        self.PLACEHOLDER_DOMICILIO = "Domicilio:"
        self.PLACEHOLDER_TELEFONO = "Teléfono:"
        self.PLACEHOLDER_OFICIO = "Oficio:"

        self.withdraw()
        self.minsize(400, 650)
        self.geometry("400x650+650+50")
        self.maxsize(400, 650)
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
        self.oficio_seleccionado = tk.StringVar()

        self.title_add_empleados = ttk.Label(self, text="AÑADIR EMPLEADO", font=("Helvetica", 12))
        self.print_cod_departamento = ttk.Label(self, text="CÓDIGO DE DEPARTAMENTO:", font=("Helvetica", 9))
        self.eleccion_cod_departamento = ttk.Combobox(self, values=[], textvariable=self.cod_departamento_seleccionado, foreground="gray")
        self.print_dni = ttk.Label(self, text="DNI:", font=("Helvetica", 9))
        self.input_dni = ttk.Entry(self, foreground="gray", textvariable=self.dni_seleccionado)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.nombre_seleccionado)
        self.print_apellidos = ttk.Label(self, text="APELLIDOS:", font=("Helvetica", 9))
        self.input_apellidos = ttk.Entry(self, foreground="gray", textvariable=self.apellidos_seleccionados)
        self.print_fecha_nac = ttk.Label(self, text="FECHA DE NACIMIENTO:", font=("Helvetica", 9))
        self.print_salario = ttk.Label(self, text="SALARIO:", font=("Helvetica", 9))
        self.input_salario = ttk.Entry(self, foreground="gray", textvariable=self.salario_seleccionado)
        self.print_domicilio = ttk.Label(self, text="DOMICILIO:", font=("Helvetica", 9))
        self.input_domicilio = ttk.Entry(self, foreground="gray", textvariable=self.domicilio_seleccionado)
        self.print_telefono = ttk.Label(self, text="TELÉFONO:", font=("Helvetica", 9))
        self.input_telefono = ttk.Entry(self, foreground="gray", textvariable=self.telefono_seleccionado)
        self.print_oficio = ttk.Label(self, text="oficio:", font=("Helvetica", 9))
        self.posibles_oficios = ['GESTOR', 'TÉCNICO', 'RR.HH', 'ANALISTA', 'CARRETILLERO', 'MOZO DE ALMACÉN']
        self.eleccion_oficio = ttk.Combobox(self, values=self.posibles_oficios, textvariable=self.oficio_seleccionado, foreground="gray")
        self.boton_add_empleados = ttk.Button(self, text="AÑADIR")

    def mostrar_menu(self):
        self.actualizar_posibles_departamentos()
        self.title_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_apellidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_fecha_nac.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        if self.no_mostrar_calendario: #LO PONEMOS ASÍ PARA QUE SOLO SE MUESTRE UNA VEZ
            self.input_fecha_pedido = DateEntry(self, date_pattern='yyyy-mm-dd') #NO LO PONEMOS EN EL INIT PORQUE SALTA UN PANTALLAZO RARO
            self.input_fecha_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
            self.no_mostrar_calendario = False
        self.print_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        
        self.deiconify()
        self.mainloop()

    def actualizar_posibles_departamentos(self):
        self.posibles_departamentos = self.almacen_departamentos.generar_combobox()
        self.eleccion_cod_departamento['values'] = self.posibles_departamentos

    def on_close(self):
       self.withdraw()
       #self.limpiar_campos()
       self.menu_empleados.deiconify()

    

