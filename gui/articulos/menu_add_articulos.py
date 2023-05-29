import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk


class AddArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, almacen_clientes, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.almacen_clientes = almacen_clientes
        self.menu_articulos = menu_articulos

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_CLIENTE = "Código de Cliente:"
        self.PLACEHOLDER_NOMBRE = "Nombre:"
        self.PLACEHOLDER_DESCRIPCION = "Descripción:"
        self.PLACEHOLDER_CATEGORIA = "Ej: ROPA"

        self.withdraw()
        self.minsize(350, 350)
        self.geometry("350x350+650+100")
        self.maxsize(350, 350)
        self.title("AÑADIR ARTÍCULO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_cliente_seleccionado = tk.StringVar()
        self.input_nombre_seleccionado = tk.StringVar()
        self.input_descripcion_seleccionada = tk.StringVar()
        self.categoria_seleccionada = tk.StringVar()
        
        self.title_add_articulos = ttk.Label(self, text="AÑADIR ARTÍCULO", font=("Helvetica", 12))
        self.print_cod_cliente = ttk.Label(self, text="CÓDIGO DE CLIENTE:", font=("Helvetica", 9))
        self.eleccion_cod_cliente = ttk.Combobox(self, values=[], textvariable=self.cod_cliente_seleccionado, foreground="gray")
        self.eleccion_cod_cliente.insert(0, self.PLACEHOLDER_COD_CLIENTE)
        self.eleccion_cod_cliente.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_cliente)
        self.eleccion_cod_cliente.bind('<FocusOut>', self.set_placeholder_eleccion_cod_cliente)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.input_nombre_seleccionado)
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.print_descripcion = ttk.Label(self, text="DESCRIPCIÓN:", font=("Helvetica", 9))
        self.input_descripcion = ttk.Entry(self, foreground="gray", textvariable=self.input_descripcion_seleccionada)
        self.input_descripcion.insert(0, self.PLACEHOLDER_DESCRIPCION)
        self.input_descripcion.bind('<FocusIn>', self.clear_placeholder_input_descripcion)
        self.input_descripcion.bind('<FocusOut>', self.set_placeholder_input_descripcion)
        self.print_categoria = ttk.Label(self, text="CATEGORÍA:", font=("Helvetica", 9))
        self.posibles_categorias = ["ROPA", "OCIO", "DEPORTES", "ALIMENTACIÓN", "HOGAR", "COSMÉTICA", "EDUCACIÓN", "TECNOLOGÍA"]
        self.eleccion_categorias = ttk.Combobox(self, values=self.posibles_categorias, textvariable=self.categoria_seleccionada, foreground="gray")
        self.eleccion_categorias.insert(0, self.PLACEHOLDER_CATEGORIA)
        self.eleccion_categorias.bind('<FocusIn>', self.clear_placeholder_input_categoria)
        self.eleccion_categorias.bind('<FocusOut>', self.set_placeholder_input_categoria)
        self.boton_add_articulo = ttk.Button(self, text="AÑADIR", command=self.comprobar_articulos)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_cliente()
        self.title_add_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_descripcion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_descripcion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_categoria.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_categorias.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_cliente(self):
        self.posibles_cod_cliente = self.almacen_clientes.generar_combobox()
        self.eleccion_cod_cliente['values'] = self.posibles_cod_cliente

    def recoger_datos_articulos(self):
        dato_cod_cliente = self.cod_cliente_seleccionado.get()
        dato_nombre = self.input_nombre_seleccionado.get().upper()
        dato_descripcion = self.input_descripcion_seleccionada.get().upper()
        dato_categoria = self.categoria_seleccionada.get().upper()
        dato_cod_articulo = f"A{str(random.randrange(1,1001))}"
        return dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria

    def comprobar_articulos(self):
        dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria = self.recoger_datos_articulos()
        if dato_cod_cliente in self.posibles_cod_cliente and dato_categoria in self.posibles_categorias:
            datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE ARTICULO: {dato_cod_articulo}\nCÓDIGO DE CLIENTE: {dato_cod_cliente}\nNOMBRE: {dato_nombre}\nDESCRIPCIÓN: {dato_descripcion}\nCATEGORÍA: {dato_categoria}")
            if datos:
                if (self.almacen_articulos.add_datos(dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria)):
                    cod_repetido = messagebox.showinfo(message="EL CÓDIGO GENERADO POR EL SISTEMA YA ESTÁ ASIGNADO")
                else:
                    self.on_close()
        else:
            datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_cliente(self, event):
        if self.eleccion_cod_cliente.get() == self.PLACEHOLDER_COD_CLIENTE:
            self.eleccion_cod_cliente.delete(0, tk.END)
            self.eleccion_cod_cliente.config(foreground='black')

    def set_placeholder_eleccion_cod_cliente(self, event):
        if self.eleccion_cod_cliente.get() == "":
            self.eleccion_cod_cliente.insert(0, self.PLACEHOLDER_COD_CLIENTE)
            self.eleccion_cod_cliente.config(foreground='gray')

    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
            self.input_nombre.config(foreground='gray')

    def clear_placeholder_input_descripcion(self, event):
        if self.input_descripcion.get() == self.PLACEHOLDER_DESCRIPCION:
            self.input_descripcion.delete(0, tk.END)
            self.input_descripcion.config(foreground='black')

    def set_placeholder_input_descripcion(self, event):
        if self.input_descripcion.get() == "":
            self.input_descripcion.insert(0, self.PLACEHOLDER_DESCRIPCION)
            self.input_descripcion.config(foreground='gray')

    def clear_placeholder_input_categoria(self, event):
        if self.eleccion_categorias.get() == self.PLACEHOLDER_CATEGORIA:
            self.eleccion_categorias.delete(0, tk.END)
            self.eleccion_categorias.config(foreground='black')

    def set_placeholder_input_categoria(self, event):
        if self.eleccion_categorias.get() == "":
            self.eleccion_categorias.insert(0, self.PLACEHOLDER_CATEGORIA)
            self.eleccion_categorias.config(foreground='gray')
    
    def on_close(self):
       self.withdraw()
       self.limpiar_campos()
       self.menu_articulos.deiconify()

    def limpiar_campos(self):
        self.cod_cliente_seleccionado.set('')
        self.set_placeholder_eleccion_cod_cliente(None)
        self.input_nombre_seleccionado.set('')
        self.set_placeholder_input_nombre(None)
        self.input_descripcion_seleccionada.set('')
        self.set_placeholder_input_descripcion(None)
        self.categoria_seleccionada.set('')
        self.set_placeholder_input_categoria(None)
    
