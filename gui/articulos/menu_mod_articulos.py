import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class ModArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, almacen_clientes, cod_articulo_var, cod_cliente_var, 
    nombre_var, descripcion_var, categoria_var, menu_lis_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.almacen_clientes = almacen_clientes
        self.cod_articulo_var = cod_articulo_var
        self.cod_cliente_var = cod_cliente_var
        self.nombre_var = nombre_var
        self.descripcion_var = descripcion_var
        self.categoria_var = categoria_var
        self.menu_lis_articulos = menu_lis_articulos

        self.withdraw()
        self.minsize(350, 350)
        self.geometry("350x350+650+100")
        self.maxsize(350, 350)
        self.title("MODIFICAR SUCURSAL")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.print_cod_articulo = ttk.Label(self, text="CÓDIGO DE ARTÍCULO:", font=("Helvetica", 9))
        self.input_cod_articulo = ttk.Entry(self, textvariable=self.cod_articulo_var, state='readonly')
        self.print_cod_cliente = ttk.Label(self, text="CÓDIGO DE CLIENTE:", font=("Helvetica", 9))
        self.eleccion_cod_cliente = ttk.Combobox(self, values=[], textvariable=self.cod_cliente_var)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, textvariable=self.nombre_var)
        self.print_descripcion = ttk.Label(self, text="DESCRIPCIÓN:", font=("Helvetica", 9))
        self.input_descripcion = ttk.Entry(self, textvariable=self.descripcion_var)
        self.print_categoria = ttk.Label(self, text="CATEGORÍA:", font=("Helvetica", 9))
        self.posibles_categorias = ["ROPA", "OCIO", "DEPORTES", "ALIMENTACIÓN", "HOGAR", "COSMÉTICA", "EDUCACIÓN", "TECNOLOGÍA"]
        self.eleccion_categorias = ttk.Combobox(self, values=self.posibles_categorias, textvariable=self.categoria_var)
        self.boton_mod_articulos = ttk.Button(self, text="REALIZAR CAMBIOS", command=self.realizar_modificaciones)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_cliente()
        self.print_cod_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_descripcion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_descripcion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_categoria.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_categorias.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_cliente(self):
        self.posibles_cod_cliente = self.almacen_clientes.generar_combobox()
        self.eleccion_cod_cliente['values'] = self.posibles_cod_cliente

    def realizar_modificaciones(self):
        dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria = self.menu_lis_articulos.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL ARTÍCULO?")
        if reaviso:
            if dato_cod_cliente in self.posibles_cod_cliente and dato_categoria in self.posibles_categorias:
                self.almacen_articulos.del_datos(dato_cod_articulo)
                self.almacen_articulos.add_datos(dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria)
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_close(self):
        self.withdraw()
        self.menu_lis_articulos.deiconify()
