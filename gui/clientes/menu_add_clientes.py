import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class AddClientes(tk.Toplevel):
    def __init__(self, master, almacen_clientes, almacen_sucursales, menu_clientes):
        super().__init__(master)
        self.almacen_clientes = almacen_clientes
        self.almacen_sucursales = almacen_sucursales
        self.menu_clientes = menu_clientes

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_COD_SUCURSAL = "Código de Sucursal:"

        self.withdraw()
        self.minsize(225, 200)
        self.geometry("225x200+650+100")
        self.maxsize(225, 200)
        self.title("AÑADIR CLIENTE")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.sucursal_seleccionada = tk.StringVar()
        self.input_nombre_seleccionado = tk.StringVar()

        self.title_add_clientes = ttk.Label(self, text="AÑADIR CLIENTE", font=("Helvetica", 12))
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.input_nombre_seleccionado)
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_sucursal = ttk.Combobox(self, values=[], textvariable=self.sucursal_seleccionada, foreground="gray")
        self.eleccion_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
        self.eleccion_sucursal.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_sucursal)
        self.eleccion_sucursal.bind('<FocusOut>', self.set_placeholder_eleccion_cod_sucursal)
        self.boton_add_sucursal = ttk.Button(self, text="AÑADIR", command=self.comprobar_clientes)

    def mostrar_menu(self):
        self.actualizar_posibles_sucursales()
        self.title_add_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_sucursales(self):
        self.posibles_sucursales = self.almacen_sucursales.generar_combobox()
        self.eleccion_sucursal['values'] = self.posibles_sucursales

    def recoger_datos_clientes(self):
        dato_cod_sucursal = self.sucursal_seleccionada.get()
        dato_nombre = self.input_nombre_seleccionado.get().upper()
        dato_cod_cliente = f"C{str(random.randrange(1,1001))}"
        return dato_cod_cliente, dato_cod_sucursal, dato_nombre

    def comprobar_clientes(self):
        dato_cod_cliente, dato_cod_sucursal, dato_nombre = self.recoger_datos_clientes()
        if dato_cod_sucursal in self.posibles_sucursales:
            datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE CLIENTE: {dato_cod_cliente}\nCÓDIGO DE SUCURSAL: {dato_cod_sucursal}\nNOMBRE: {dato_nombre}")
            if datos:
                if(self.almacen_clientes.add_datos(dato_cod_cliente, dato_cod_sucursal, dato_nombre)):
                    cod_repetido = messagebox.showinfo(message="EL CLIENTE YA SE ENCUENTRA EN EL SISTEMA")
                self.on_close()
        else:
            datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    #PLACEHOLDERS
    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
            self.input_nombre.config(foreground='gray')

    def clear_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_sucursal.get() == self.PLACEHOLDER_COD_SUCURSAL:
            self.eleccion_sucursal.delete(0, tk.END)
            self.eleccion_sucursal.config(foreground='black')

    def set_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_sucursal.get() == "":
            self.eleccion_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
            self.eleccion_sucursal.config(foreground='gray')
    
    def on_close(self):
       self.withdraw()
       self.limpiar_campos()
       self.menu_clientes.deiconify()

    def limpiar_campos(self):
        self.input_nombre_seleccionado.set('')
        self.set_placeholder_input_nombre(None)
        self.sucursal_seleccionada.set('')
        self.set_placeholder_eleccion_cod_sucursal(None)
