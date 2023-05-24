import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class LisArticulos(tk.Toplevel):
    class ConstantesListado:
        COD_ARTICULO = 0
        COD_CLIENTE = 1
        NOMBRE = 2
        DESCRIPCION = 3
        CATEGORIA = 4

        @staticmethod
        def opciones():
            return range(LisArticulos.ConstantesListado.COD_ARTICULO,
                        LisArticulos.ConstantesListado.CATEGORIA+1)

    def __init__(self, master, almacen_articulos, almacen_clientes, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.almacen_clientes = almacen_clientes
        self.menu_articulos = menu_articulos

        self.minsize(900, 530)
        self.geometry("900x530+400+150")
        self.maxsize(1300, 530)

        self.withdraw()
        self.title("MIS SUCURSALES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_articulo_var = tk.StringVar()
        self.cod_cliente_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.categoria_var = tk.StringVar()

        self.title_lis_sucursales = ttk.Label(self, text="MIS ARTÍCULOS", font=("Helvetica", 12)) 
        self.tree_articulos = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        #MODIFICACION
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
        self.boton_mod_articulos = ttk.Button(self, text="MODIFICAR", command=self.realizar_modificaciones)

        #TABLA
        self.tree_articulos["columns"] = ("COD_ARTICULO", "COD_CLIENTE", "NOMBRE", "DESCRIPCION", "CATEGORIA")   
        
        self.tree_articulos.column("#0", width=100, stretch=tk.NO)  # Columna de índice
        self.tree_articulos.column("COD_ARTICULO", anchor=tk.W, width=50)
        self.tree_articulos.column("COD_CLIENTE", anchor=tk.W, width=60)
        self.tree_articulos.column("NOMBRE", anchor=tk.W, width=50)
        self.tree_articulos.column("DESCRIPCION", anchor=tk.W, width=100)
        self.tree_articulos.column("CATEGORIA", anchor=tk.W, width=30)
        
        self.tree_articulos.heading("#0", text="NUM_SUCURSAL", anchor=tk.W)
        self.tree_articulos.heading("COD_ARTICULO", text="COD_ARTICULO", anchor=tk.W)
        self.tree_articulos.heading("COD_CLIENTE", text="COD_CLIENTE", anchor=tk.W)
        self.tree_articulos.heading("NOMBRE", text="NOMBRE", anchor=tk.W)
        self.tree_articulos.heading("DESCRIPCION", text="DESCRIPCION", anchor=tk.W)
        self.tree_articulos.heading("CATEGORIA", text="CATEGORIA", anchor=tk.W)

        self.tree_articulos.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_cliente()
        self.title_lis_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tree_articulos.pack(fill="both", expand=True)
        self.crear_listado()

        #CAMPOS MODIFICACIONES
        self.print_cod_articulo.pack()
        self.input_cod_articulo.pack()
        self.print_cod_cliente.pack()
        self.eleccion_cod_cliente.pack()
        self.print_nombre.pack()
        self.input_nombre.pack()
        self.print_descripcion.pack()
        self.input_descripcion.pack()
        self.print_categoria.pack()
        self.eleccion_categorias.pack()
        self.boton_mod_articulos.pack()
        self.deiconify()

    def actualizar_posibles_cod_cliente(self):
        self.posibles_cod_cliente = self.almacen_clientes.generar_combobox()
        self.eleccion_cod_cliente['values'] = self.posibles_cod_cliente

    def crear_listado(self):
        self.tree_articulos.delete(*self.tree_articulos.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for articulo in self.almacen_articulos._articulos:
            if (busqueda in articulo._cod_articulo.upper()
            or busqueda in articulo._cod_cliente.upper()
            or busqueda in articulo._nombre.upper()
            or busqueda in articulo._descripcion.upper()
            or busqueda in articulo._categoria.upper() or not busqueda):
                self.tree_articulos.insert("", tk.END, text=f"{contador}",
                                            values=(articulo._cod_articulo, articulo._cod_cliente, articulo._nombre, 
                                            articulo._descripcion, articulo._categoria))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_articulos.deiconify()

    def recoger_datos(self):
        dato_cod_articulo = self.cod_articulo_var.get()
        dato_cod_cliente = self.cod_cliente_var.get()
        dato_nombre = self.nombre_var.get().upper()
        dato_descripcion = self.descripcion_var.get().upper()
        dato_categoria = self.categoria_var.get().upper()
        return dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria    

    def realizar_modificaciones(self):
        dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria = self.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL ARTÍCULO?")
        if reaviso:
            if dato_cod_cliente in self.posibles_cod_cliente and dato_categoria in self.posibles_categorias:
                self.almacen_articulos.del_datos(dato_cod_articulo)
                self.almacen_articulos.add_datos(dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria)
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_select(self, event):
        try:
            selected_item = self.tree_articulos.selection()[0]
            values = self.tree_articulos.item(selected_item)['values']
            self.cod_articulo_var.set(values[self.ConstantesListado.COD_ARTICULO])
            self.cod_cliente_var.set(values[self.ConstantesListado.COD_CLIENTE])
            self.nombre_var.set(values[self.ConstantesListado.NOMBRE])
            self.descripcion_var.set(values[self.ConstantesListado.DESCRIPCION])
            self.categoria_var.set(values[self.ConstantesListado.CATEGORIA])
        except IndexError:
            pass