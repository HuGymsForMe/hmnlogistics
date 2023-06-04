from tkcalendar import DateEntry
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import datetime

from clases.validator import Validator

class AddEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, almacen_departamentos, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.menu_empleados = menu_empleados
        self.validador = Validator()

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_DEPARTAMENTO = "Código de Departamento:"
        self.PLACEHOLDER_DNI = "Ej: 00000000B"
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_APELLIDOS = "Apellidos:"
        self.PLACEHOLDER_FECHA_NAC = "Formato: 'YYYY-MM-DD'"
        self.PLACEHOLDER_SALARIO = "Salario:"
        self.PLACEHOLDER_DOMICILIO = "Domicilio:"
        self.PLACEHOLDER_TELEFONO = "Teléfono:"
        self.PLACEHOLDER_OFICIO = "Oficio:"

        self.withdraw()
        self.minsize(400, 700)
        self.geometry("400x7000+650+50")
        self.maxsize(400, 700)
        self.title("AÑADIR EMPLEADO")
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
        self.eleccion_cod_departamento.insert(0, self.PLACEHOLDER_COD_DEPARTAMENTO)
        self.eleccion_cod_departamento.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_departamento)
        self.eleccion_cod_departamento.bind('<FocusOut>', self.set_placeholder_eleccion_cod_departamento)
        self.print_dni = ttk.Label(self, text="DNI:", font=("Helvetica", 9))
        self.input_dni = ttk.Entry(self, foreground="gray", textvariable=self.dni_seleccionado)
        self.input_dni.insert(0, self.PLACEHOLDER_DNI)
        self.input_dni.bind('<FocusIn>', self.clear_placeholder_input_dni)
        self.input_dni.bind('<FocusOut>', self.set_placeholder_input_dni)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.nombre_seleccionado)
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.print_apellidos = ttk.Label(self, text="APELLIDOS:", font=("Helvetica", 9))
        self.input_apellidos = ttk.Entry(self, foreground="gray", textvariable=self.apellidos_seleccionados)
        self.input_apellidos.insert(0, self.PLACEHOLDER_APELLIDOS)
        self.input_apellidos.bind('<FocusIn>', self.clear_placeholder_input_apellidos)
        self.input_apellidos.bind('<FocusOut>', self.set_placeholder_input_apellidos)
        self.print_fecha_nac = ttk.Label(self, text="FECHA DE NACIMIENTO:", font=("Helvetica", 9))
        self.input_fecha_nac = ttk.Entry(self, foreground="gray", textvariable=self.fecha_nac_seleccionada)
        self.input_fecha_nac.insert(0, self.PLACEHOLDER_FECHA_NAC)
        self.input_fecha_nac.bind('<FocusIn>', self.clear_placeholder_input_fecha_nac)
        self.input_fecha_nac.bind('<FocusOut>', self.set_placeholder_input_fecha_nac)
        self.print_salario = ttk.Label(self, text="SALARIO:", font=("Helvetica", 9))
        self.input_salario = ttk.Entry(self, foreground="gray", textvariable=self.salario_seleccionado)
        self.input_salario.insert(0, self.PLACEHOLDER_SALARIO)
        self.input_salario.bind('<FocusIn>', self.clear_placeholder_input_salario)
        self.input_salario.bind('<FocusOut>', self.set_placeholder_input_salario)
        self.print_domicilio = ttk.Label(self, text="DOMICILIO:", font=("Helvetica", 9))
        self.input_domicilio = ttk.Entry(self, foreground="gray", textvariable=self.domicilio_seleccionado)
        self.input_domicilio.insert(0, self.PLACEHOLDER_DOMICILIO)
        self.input_domicilio.bind('<FocusIn>', self.clear_placeholder_input_domicilio)
        self.input_domicilio.bind('<FocusOut>', self.set_placeholder_input_domicilio)
        self.print_telefono = ttk.Label(self, text="TELÉFONO:", font=("Helvetica", 9))
        self.input_telefono = ttk.Entry(self, foreground="gray", textvariable=self.telefono_seleccionado)
        self.input_telefono.insert(0, self.PLACEHOLDER_TELEFONO)
        self.input_telefono.bind('<FocusIn>', self.clear_placeholder_input_telefono)
        self.input_telefono.bind('<FocusOut>', self.set_placeholder_input_telefono)
        self.print_oficio = ttk.Label(self, text="OFICIO:", font=("Helvetica", 9))
        self.posibles_oficios = ['GESTOR', 'TÉCNICO', 'RR.HH', 'ANALISTA', 'CARRETILLERO', 'MOZO DE ALMACÉN']
        self.eleccion_oficio = ttk.Combobox(self, values=self.posibles_oficios, textvariable=self.oficio_seleccionado, foreground="gray")
        self.eleccion_oficio.insert(0, self.PLACEHOLDER_OFICIO)
        self.eleccion_oficio.bind('<FocusIn>', self.clear_placeholder_eleccion_oficio)
        self.eleccion_oficio.bind('<FocusOut>', self.set_placeholder_eleccion_oficio)
        self.boton_add_empleado = ttk.Button(self, text="AÑADIR", command=self.comprobar_empleados)

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
        self.input_fecha_nac.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_domicilio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_empleado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()
        self.mainloop()

    def actualizar_posibles_departamentos(self):
        self.posibles_departamentos = self.almacen_departamentos.generar_combobox()
        self.eleccion_cod_departamento['values'] = self.posibles_departamentos

    def recoger_datos_empleados(self):
        dato_cod_empleado = f"EMP{str(random.randrange(1,1001))}"
        dato_cod_departamento = self.cod_departamento_seleccionado.get().upper()
        dato_dni = self.dni_seleccionado.get().upper()
        dato_nombre = self.nombre_seleccionado.get().upper()
        dato_apellidos = self.apellidos_seleccionados.get().upper()
        dato_fecha_nac = self.fecha_nac_seleccionada.get().upper()
        dato_fecha_alta = datetime.date.today().strftime('%Y-%m-%d')
        dato_salario = self.salario_seleccionado.get()
        dato_domicilio = self.domicilio_seleccionado.get().upper()
        dato_telefono = self.telefono_seleccionado.get()
        dato_oficio = self.oficio_seleccionado.get().upper()
        return (dato_cod_empleado, dato_cod_departamento, dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac,
        dato_fecha_alta, dato_salario, dato_domicilio, dato_telefono, dato_oficio)

    def comprobar_empleados(self):
        (dato_cod_empleado, dato_cod_departamento, dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac,
        dato_fecha_alta, dato_salario, dato_domicilio, dato_telefono, dato_oficio) = self.recoger_datos_empleados()
        if (dato_cod_departamento in self.posibles_departamentos
         and dato_oficio in self.posibles_oficios
         and self.validador.validador_dni(dato_dni) 
         and self.validador.validador_telefono(dato_telefono)
         and self.validador.validador_es_numero(dato_salario)):
            datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE EMPLEADO: {dato_cod_empleado}\nCÓDIGO DE DEPARTAMENTO: {dato_cod_departamento}\n\
DNI: {dato_dni}\nNOMBRE: {dato_nombre}\nAPELLIDOS: {dato_apellidos}\nFECHA DE NACIMIENTO: {dato_fecha_nac}\nFECHA DE ALTA: {dato_fecha_alta}\n\
SALARIO: {dato_salario}\nDOMICILIO: {dato_domicilio}\nTELÉFONO: {dato_telefono}\nOFICIO: {dato_oficio}")
            if datos:
                if self.almacen_empleados.add_datos(dato_cod_empleado, dato_cod_departamento, dato_dni, dato_fecha_alta, dato_salario, dato_telefono, dato_oficio):
                    cod_repetido = messagebox.showinfo(message="EL EMPLEADO YA ESTÁ REGISTRADO EN EL SISTEMA")
                if self.almacen_empleados.add_datos_2(dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio):
                    cod_repetido
            self.on_close()
        else:
            datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_departamento(self, event):
        if self.eleccion_cod_departamento.get() == self.PLACEHOLDER_COD_DEPARTAMENTO:
            self.eleccion_cod_departamento.delete(0, tk.END)
            self.eleccion_cod_departamento.config(foreground='black')

    def set_placeholder_eleccion_cod_departamento(self, event):
        if self.eleccion_cod_departamento.get() == "":
            self.eleccion_cod_departamento.insert(0, self.PLACEHOLDER_COD_DEPARTAMENTO)
            self.eleccion_cod_departamento.config(foreground='gray')

    def clear_placeholder_input_dni(self, event):
        if self.input_dni.get() == self.PLACEHOLDER_DNI:
            self.input_dni.delete(0, tk.END)
            self.input_dni.config(foreground='black')

    def set_placeholder_input_dni(self, event):
        if self.input_dni.get() == "":
            self.input_dni.insert(0, self.PLACEHOLDER_DNI)
            self.input_dni.config(foreground='gray')

    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
            self.input_nombre.config(foreground='gray')

    def clear_placeholder_input_apellidos(self, event):
        if self.input_apellidos.get() == self.PLACEHOLDER_APELLIDOS:
            self.input_apellidos.delete(0, tk.END)
            self.input_apellidos.config(foreground='black')

    def set_placeholder_input_apellidos(self, event):
        if self.input_apellidos.get() == "":
            self.input_apellidos.insert(0, self.PLACEHOLDER_APELLIDOS)
            self.input_apellidos.config(foreground='gray')

    def clear_placeholder_input_fecha_nac(self, event):
        if self.input_fecha_nac.get() == self.PLACEHOLDER_FECHA_NAC:
            self.input_fecha_nac.delete(0, tk.END)
            self.input_fecha_nac.config(foreground='black')

    def set_placeholder_input_fecha_nac(self, event):
        if self.input_fecha_nac.get() == "":
            self.input_fecha_nac.insert(0, self.PLACEHOLDER_FECHA_NAC)
            self.input_fecha_nac.config(foreground='gray')

    def clear_placeholder_input_salario(self, event):
        if self.input_salario.get() == self.PLACEHOLDER_SALARIO:
            self.input_salario.delete(0, tk.END)
            self.input_salario.config(foreground='black')

    def set_placeholder_input_salario(self, event):
        if self.input_salario.get() == "":
            self.input_salario.insert(0, self.PLACEHOLDER_SALARIO)
            self.input_salario.config(foreground='gray')

    def clear_placeholder_input_domicilio(self, event):
        if self.input_domicilio.get() == self.PLACEHOLDER_DOMICILIO:
            self.input_domicilio.delete(0, tk.END)
            self.input_domicilio.config(foreground='black')

    def set_placeholder_input_domicilio(self, event):
        if self.input_domicilio.get() == "":
            self.input_domicilio.insert(0, self.PLACEHOLDER_DOMICILIO)
            self.input_domicilio.config(foreground='gray')

    def clear_placeholder_input_telefono(self, event):
        if self.input_telefono.get() == self.PLACEHOLDER_TELEFONO:
            self.input_telefono.delete(0, tk.END)
            self.input_telefono.config(foreground='black')

    def set_placeholder_input_telefono(self, event):
        if self.input_telefono.get() == "":
            self.input_telefono.insert(0, self.PLACEHOLDER_TELEFONO)
            self.input_telefono.config(foreground='gray')

    def clear_placeholder_eleccion_oficio(self, event):
        if self.eleccion_oficio.get() == self.PLACEHOLDER_OFICIO:
            self.eleccion_oficio.delete(0, tk.END)
            self.eleccion_oficio.config(foreground='black')

    def set_placeholder_eleccion_oficio(self, event):
        if self.eleccion_oficio.get() == "":
            self.eleccion_oficio.insert(0, self.PLACEHOLDER_OFICIO)
            self.eleccion_oficio.config(foreground='gray')

    def on_close(self):
       self.withdraw()
       #self.limpiar_campos()
       self.menu_empleados.deiconify()

    

