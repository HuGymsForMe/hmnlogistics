from tkcalendar import DateEntry
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from clases.validator import Validator

class AddPedidos(tk.Toplevel):
    def __init__(self, master, almacen_pedidos, almacen_sucursales, almacen_distribuidores, menu_pedidos):
        super().__init__(master)
        self.almacen_pedidos = almacen_pedidos
        self.almacen_sucursales = almacen_sucursales
        self.almacen_distribuidores = almacen_distribuidores
        self.menu_pedidos = menu_pedidos
        self.no_mostrar_calendario = True
        self.validador = Validator()

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_DISTRIBUIDOR = "Código de Distribuidor:"
        self.PLACEHOLDER_COD_SUCURSAL = "Código de Sucursal:"
        self.PLACEHOLDER_NUM_ARTICULOS = "Nº Artículos:"
        self.PLACEHOLDER_PESO = "Peso:"
        self.PLACEHOLDER_PRECIO = "Precio:"

        self.withdraw()
        self.minsize(400, 450)
        self.geometry("400x450+650+100")
        self.maxsize(400, 450)
        self.title("AÑADIR DISTRIBUIDOR")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_distribuidor_seleccionado = tk.StringVar()
        self.cod_sucursal_seleccionado = tk.StringVar()
        self.input_num_articulos_seleccionado = tk.StringVar()
        self.input_peso_seleccionado = tk.StringVar()
        self.input_precio_seleccionado = tk.StringVar()
        
        self.title_add_pedidos = ttk.Label(self, text="AÑADIR PEDIDO", font=("Helvetica", 12))
        self.print_cod_distribuidor = ttk.Label(self, text="CÓDIGO DE DISTRIBUIDOR:", font=("Helvetica", 9))
        self.eleccion_cod_distribuidor = ttk.Combobox(self, values=[], textvariable=self.cod_distribuidor_seleccionado, foreground="gray")
        self.eleccion_cod_distribuidor.insert(0, self.PLACEHOLDER_COD_DISTRIBUIDOR)
        self.eleccion_cod_distribuidor.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_distribuidor)
        self.eleccion_cod_distribuidor.bind('<FocusOut>', self.set_placeholder_eleccion_cod_distribuidor)
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_cod_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_seleccionado, foreground="gray")
        self.eleccion_cod_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
        self.eleccion_cod_sucursal.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_sucursal)
        self.eleccion_cod_sucursal.bind('<FocusOut>', self.set_placeholder_eleccion_cod_sucursal)
        self.print_fecha_pedido = ttk.Label(self, text="FECHA PEDIDO:", font=("Helvetica", 9))
        self.print_num_articulos = ttk.Label(self, text="Nº ARTÍCULOS:", font=("Helvetica", 9))
        self.input_num_articulos = ttk.Spinbox(self, from_=0, to=100, increment=1, foreground="gray",textvariable=self.input_num_articulos_seleccionado)
        self.input_num_articulos.insert(0, self.PLACEHOLDER_NUM_ARTICULOS)
        self.input_num_articulos.bind('<FocusIn>', self.clear_placeholder_input_num_articulos)
        self.input_num_articulos.bind('<FocusOut>', self.set_placeholder_input_num_articulos)
        self.print_peso = ttk.Label(self, text="PESO(kg):", font=("Helvetica", 9))
        self.input_peso = ttk.Entry(self, foreground="gray", textvariable=self.input_peso_seleccionado)
        self.input_peso.insert(0, self.PLACEHOLDER_PESO)
        self.input_peso.bind('<FocusIn>', self.clear_placeholder_input_peso)
        self.input_peso.bind('<FocusOut>', self.set_placeholder_input_peso)
        self.print_precio = ttk.Label(self, text="PRECIO(€):", font=("Helvetica", 9))
        self.input_precio = ttk.Entry(self, foreground="gray", textvariable=self.input_precio_seleccionado)
        self.input_precio.insert(0, self.PLACEHOLDER_PRECIO)
        self.input_precio.bind('<FocusIn>', self.clear_placeholder_input_precio)
        self.input_precio.bind('<FocusOut>', self.set_placeholder_input_precio)
        self.boton_add_pedido = ttk.Button(self, text="AÑADIR", command=self.comprobar_pedidos)

    def mostrar_menu(self):
        self.actualizar_posibles_distribuidores_sucursales()
        self.title_add_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_fecha_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        if self.no_mostrar_calendario: #LO PONEMOS ASÍ PARA QUE SOLO SE MUESTRE UNA VEZ
            self.input_fecha_pedido = DateEntry(self, date_pattern='yyyy-mm-dd') #NO LO PONEMOS EN EL INIT PORQUE SALTA UN PANTALLAZO RARO
            self.input_fecha_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
            self.no_mostrar_calendario = False
        self.print_num_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_num_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_peso.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_peso.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_precio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_precio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_distribuidores_sucursales(self):
        self.posibles_distribuidores = self.almacen_distribuidores.generar_combobox()
        self.eleccion_cod_distribuidor['values'] = self.posibles_distribuidores
        self.posibles_sucursales = self.almacen_sucursales.generar_combobox()
        self.eleccion_cod_sucursal['values'] = self.posibles_sucursales

    def recoger_datos_pedidos(self):
        dato_cod_pedido = f"P{str(random.randrange(1,1001))}"
        dato_cod_distribuidor = self.cod_distribuidor_seleccionado.get()
        dato_cod_sucursal = self.cod_sucursal_seleccionado.get()
        dato_fecha_pedido = self.input_fecha_pedido.get()
        dato_num_articulos = int(self.input_num_articulos.get())
        dato_peso = round(float(self.input_peso.get()),2)
        dato_precio = round(float(self.input_precio.get()),2)
        return dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio

    def comprobar_pedidos(self):
        try:
            dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio = self.recoger_datos_pedidos()
            if (dato_cod_distribuidor in self.posibles_distribuidores 
                and dato_cod_sucursal in self.posibles_sucursales
                and self.validador.validador_fecha(dato_fecha_pedido)):
                datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE PEDIDO: {dato_cod_pedido}\nCÓDIGO DE DISTRIBUIDOR: {dato_cod_distribuidor}\n\
CÓDIGO DE SUCURSAL: {dato_cod_sucursal}\nFECHA DE PEDIDO: {dato_fecha_pedido}\nNº ARTICULOS: {dato_num_articulos}\nPESO: {dato_peso}\n\
PRECIO: {dato_precio}")
                if datos:
                    if self.almacen_pedidos.add_datos(dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio):
                        cod_repetido = messagebox.showinfo(message="EL DISTRIBUIDOR YA SE ENCUENTRA EN EL SISTEMA")
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")
        except ValueError:
            datos_erroneos


    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_distribuidor(self, event):
        if self.eleccion_cod_distribuidor.get() == self.PLACEHOLDER_COD_DISTRIBUIDOR:
            self.eleccion_cod_distribuidor.delete(0, tk.END)
            self.eleccion_cod_distribuidor.config(foreground='black')

    def set_placeholder_eleccion_cod_distribuidor(self, event):
        if self.eleccion_cod_distribuidor.get() == "":
            self.eleccion_cod_distribuidor.insert(0, self.PLACEHOLDER_COD_DISTRIBUIDOR)
            self.eleccion_cod_distribuidor.config(foreground='gray')
    
    def clear_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_cod_sucursal.get() == self.PLACEHOLDER_COD_SUCURSAL:
            self.eleccion_cod_sucursal.delete(0, tk.END)
            self.eleccion_cod_sucursal.config(foreground='black')

    def set_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_cod_sucursal.get() == "":
            self.eleccion_cod_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
            self.eleccion_cod_sucursal.config(foreground='gray')
    
    def clear_placeholder_input_num_articulos(self, event):
        if self.input_num_articulos.get() == self.PLACEHOLDER_NUM_ARTICULOS:
            self.input_num_articulos.delete(0, tk.END)
            self.input_num_articulos.config(foreground='black')

    def set_placeholder_input_num_articulos(self, event):
        if self.input_num_articulos.get() == "":
            self.input_num_articulos.insert(0, self.PLACEHOLDER_NUM_ARTICULOS)
            self.input_num_articulos.config(foreground='gray')

    def clear_placeholder_input_peso(self, event):
        if self.input_peso.get() == self.PLACEHOLDER_PESO:
            self.input_peso.delete(0, tk.END)
            self.input_peso.config(foreground='black')

    def set_placeholder_input_peso(self, event):
        if self.input_peso.get() == "":
            self.input_peso.insert(0, self.PLACEHOLDER_PESO)
            self.input_peso.config(foreground='gray')

    def clear_placeholder_input_precio(self, event):
        if self.input_precio.get() == self.PLACEHOLDER_PRECIO:
            self.input_precio.delete(0, tk.END)
            self.input_precio.config(foreground='black')

    def set_placeholder_input_precio(self, event):
        if self.input_precio.get() == "":
            self.input_precio.insert(0, self.PLACEHOLDER_PRECIO)
            self.input_precio.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_pedidos.deiconify()

    def limpiar_campos(self):
        self.eleccion_cod_distribuidor.set('')
        self.set_placeholder_eleccion_cod_distribuidor(None)
        self.eleccion_cod_sucursal.set('')
        self.set_placeholder_eleccion_cod_sucursal(None)
        self.input_num_articulos_seleccionado.set('')
        self.set_placeholder_input_num_articulos(None)
        self.input_peso_seleccionado.set('')
        self.set_placeholder_input_peso(None)
        self.input_precio_seleccionado.set('')
        self.set_placeholder_input_precio(None)
