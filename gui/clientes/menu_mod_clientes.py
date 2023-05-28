import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class ModClientes(tk.Toplevel):
    def __init__(self, master, almacen_clientes, almacen_sucursal, 
    cod_cliente_var, cod_sucursal_var, nombre_var, menu_lis_clientes):
        super().__init__(master)
        self.almacen_clientes = almacen_clientes
        self.almacen_sucursal = almacen_sucursal
        self.cod_cliente_var = cod_cliente_var
        self.cod_sucursal_var = cod_sucursal_var
        self.nombre_var = nombre_var
        self.menu_lis_clientes = menu_lis_clientes

        self.withdraw()
        self.minsize(250, 250)
        self.geometry("250x250+650+100")
        self.maxsize(250, 250)
        self.title("MODIFICAR SUCURSAL")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.print_cod_cliente = ttk.Label(self, text="CÓDIGO DE CLIENTE:", font=("Helvetica", 9))
        self.input_cod_cliente = ttk.Entry(self, textvariable=self.cod_cliente_var, state='readonly')
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_cod_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_var)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, textvariable=self.nombre_var)
        self.boton_mod_clientes = ttk.Button(self, text="MODIFICAR")

    def mostrar_menu(self):
        self.print_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_cliente(self):
        self.posibles_cod_sucursal = self.almacen_sucursal.generar_combobox()
        self.eleccion_cod_sucursal['values'] = self.posibles_cod_sucursal

    def realizar_modificaciones(self):
        dato_cod_cliente, dato_cod_sucursal, dato_nombre = self.menu_lis_clientes.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL CLIENTE?")
        if reaviso:
            if dato_cod_sucursal in self.posibles_cod_sucursal:
                self.almacen_clientes.del_datos(dato_cod_cliente) #NO SE PUEDE HACER YA QUE AUN NO TENEMOS CONFIGURADO EL BORRAR CLIENTE
                self.almacen_clientes.add_datos(dato_cod_cliente, dato_cod_sucursal, dato_nombre)
                messagebox.showinfo(message="EL CLIENTE SE MODIFICÓ CORRECTAMENTE")
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_close(self):
        self.withdraw()
        self.menu_lis_clientes.deiconify()

    