import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class ModEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, almacen_departamentos, cod_empleado_var, cod_departamento_var,
    dni_var, fecha_alta_var, telefono_var, salario_var, oficio_var, menu_lis_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.cod_empleado_var = cod_empleado_var
        self.cod_departamento_var = cod_departamento_var
        self.dni_var = dni_var
        self.fecha_alta_var = fecha_alta_var
        self.telefono_var = telefono_var
        self.salario_var = salario_var
        self.oficio_var = oficio_var
        self.menu_lis_empleados = menu_lis_empleados

        self.withdraw()
        self.minsize(350, 450)
        self.geometry("350x450+650+100")
        self.maxsize(350, 450)
        self.title("MODIFICAR EMPLEADO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.print_cod_empleado = ttk.Label(self, text="CÓDIGO DE EMPLEADO:", font=("Helvetica", 9))
        self.input_cod_empleado = ttk.Entry(self, textvariable=self.cod_empleado_var, state='readonly')
        self.print_cod_departamento = ttk.Label(self, text="CÓDIGO DE DEPARTAMENTO:", font=("Helvetica", 9))
        self.eleccion_cod_departamento = ttk.Combobox(self, values=[], textvariable=self.cod_departamento_var)
        self.print_dni = ttk.Label(self, text="DNI:", font=("Helvetica", 9))
        self.input_dni = ttk.Entry(self, textvariable=self.dni_var, state='readonly')
        self.print_telefono = ttk.Label(self, text="TELÉFONO:", font=("Helvetica", 9))
        self.input_telefono = ttk.Entry(self, textvariable=self.telefono_var)
        self.print_salario = ttk.Label(self, text="SALARIO:", font=("Helvetica", 9))
        self.input_salario = ttk.Entry(self, textvariable=self.salario_var)
        self.print_oficio = ttk.Label(self, text="OFICIO:", font=("Helvetica", 9))
        self.posibles_oficios = ['GESTOR', 'TÉCNICO', 'RR.HH', 'ANALISTA', 'CARRETILLERO', 'MOZO DE ALMACÉN']
        self.eleccion_oficio = ttk.Combobox(self, values=self.posibles_oficios, textvariable=self.oficio_var)
        self.boton_mod_empleado = ttk.Button(self, text="REALIZAR CAMBIOS")

    def mostrar_menu(self):
        self.actualizar_posibles_cod_departamento()
        self.print_cod_empleado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_empleado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_telefono.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_salario.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_oficio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_empleado.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_departamento(self):
        self.posibles_cod_departamento = self.almacen_departamentos.generar_combobox()
        self.eleccion_cod_departamento['values'] = self.posibles_cod_departamento

    def realizar_modificaciones(self): #MODIFICAR
        dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria = self.menu_lis_articulos.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL EMPLEADO?")
        if reaviso:
            if dato_cod_cliente in self.posibles_cod_cliente and dato_categoria in self.posibles_categorias:
                self.almacen_articulos.del_datos(dato_cod_articulo)
                self.almacen_articulos.add_datos(dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria)
                messagebox.showinfo(message="EL EMPLEADO SE MODIFICÓ CORRECTAMENTE")
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_close(self):
        self.withdraw()
        self.menu_lis_empleados.deiconify()

    