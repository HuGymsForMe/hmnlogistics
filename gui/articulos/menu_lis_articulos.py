import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from gui.articulos.menu_mod_articulos import ModArticulos

class LisArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, almacen_clientes, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.almacen_clientes = almacen_clientes
        self.menu_articulos = menu_articulos

        self.minsize(900, 400)
        self.geometry("900x400+400+150")
        self.maxsize(1300, 400)

        self.withdraw()
        self.title("MIS SUCURSALES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_articulo_var = tk.StringVar()
        self.cod_cliente_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.categoria_var = tk.StringVar()

        self.ventana_mod_articulos = ModArticulos(self.master, self.almacen_articulos, self.almacen_clientes,
        self.cod_articulo_var, self.cod_cliente_var, self.nombre_var, self.descripcion_var, self.categoria_var, self)

        self.title_lis_sucursales = ttk.Label(self, text="MIS ARTÍCULOS", font=("Helvetica", 12)) 
        self.tree_articulos = ttk.Treeview(self)
        self.print_filtro = ttk.Label(self, text="REALIZAR BUSQUEDA:", font=("Helvetica", 9))    
        self.input_filtro = ttk.Entry(self)

        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        self.boton_mod_articulos = ttk.Button(self, text="MODIFICAR ARTÍCULO", command=self.abrir_ventana_mod_articulos)

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
        self.title_lis_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tree_articulos.pack(fill="both", expand=True)
        self.boton_mod_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.crear_listado()
        self.deiconify()

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

    def on_select(self, event):
        try:
            selected_item = self.tree_articulos.selection()[0]
            values = self.tree_articulos.item(selected_item)['values']
            self.cod_articulo_var.set(values[self.almacen_articulos.CamposFicheroCsv.COD_ARTICULO])
            self.cod_cliente_var.set(values[self.almacen_articulos.CamposFicheroCsv.COD_CLIENTE])
            self.nombre_var.set(values[self.almacen_articulos.CamposFicheroCsv.NOMBRE])
            self.descripcion_var.set(values[self.almacen_articulos.CamposFicheroCsv.DESCRIPCION])
            self.categoria_var.set(values[self.almacen_articulos.CamposFicheroCsv.CATEGORIA])
        except IndexError:
            pass

    def ocultar_menu(self):
        self.withdraw()
        
    def abrir_ventana_mod_articulos(self):
        dato_cod_articulo, dato_cod_cliente, dato_nombre, dato_descripcion, dato_categoria = self.recoger_datos()
        if (dato_cod_articulo == '' and dato_cod_cliente == '' 
        and dato_nombre == '' and dato_descripcion == '' and dato_categoria == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN ARTÍCULO")
        else:
            self.ocultar_menu()
            self.ventana_mod_articulos.mostrar_menu()
            self.ventana_mod_articulos.mainloop()