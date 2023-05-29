import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from gui.pedidos.menu_mod_pedidos import ModPedidos

class LisPedidos(tk.Toplevel):
    '''
    CONSIDERAMOS QUE NO ES NECESARIA UNA VENTANA DE MODIFICAR YA QUE SOLO CONTIENE
    UN NOMBRE Y UN CÓDIGO CON LO CUÁL, LA ÚNICA MODIFICACIÓN A REALIZAR ES UN BORRADO
    DEL DISTRIBUIDOR O UNA INSERCIÓN.
    '''
    def __init__(self, master, almacen_pedidos, almacen_sucursales, almacen_distribuidores, menu_pedidos):
        super().__init__(master)
        self.almacen_pedidos = almacen_pedidos
        self.almacen_sucursales = almacen_sucursales
        self.almacen_distribuidores = almacen_distribuidores
        self.menu_pedidos = menu_pedidos
    
        self.minsize(900, 400)
        self.geometry("900x400+400+150")
        self.maxsize(1300, 400)

        self.withdraw()
        self.title("MIS PEDIDOS")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_pedido_var = tk.StringVar()
        self.cod_distribuidor_var = tk.StringVar()
        self.cod_sucursal_var = tk.StringVar()
        self.fecha_pedido_var = tk.StringVar()
        self.cantidad_articulos_var = tk.StringVar()
        self.peso_var = tk.StringVar()
        self.precio_var = tk.StringVar()

        self.ventana_mod_pedidos = ModPedidos(self.master, self.almacen_pedidos, self.almacen_sucursales, self.almacen_distribuidores, 
        self.cod_pedido_var, self.cod_distribuidor_var, self.cod_sucursal_var, self.fecha_pedido_var, self.cantidad_articulos_var,
        self.peso_var, self.precio_var, self)

        self.title_lis_pedidos = ttk.Label(self, text="MIS PEDIDOS", font=("Helvetica", 12)) 
        self.tree_pedidos = ttk.Treeview(self)
        self.print_filtro = ttk.Label(self, text="REALIZAR BUSQUEDA:", font=("Helvetica", 9))    
        self.input_filtro = ttk.Entry(self)

        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        self.boton_mod_pedidos = ttk.Button(self, text="MODIFICAR PEDIDO", command=self.abrir_ventana_mod_pedidos)

        #TABLA
        self.tree_pedidos["columns"] = ("COD_PEDIDO", "COD_DISTRIBUIDOR", 
        "COD_SUCURSAL", "FECHA DEL PEDIDO", "CANTIDAD DE ARTÍCULOS", "PESO", "PRECIO")   
        
        self.tree_pedidos.column("#0", width=100, stretch=tk.NO)  # Columna de índice
        self.tree_pedidos.column("COD_PEDIDO", anchor=tk.W, width=50)
        self.tree_pedidos.column("COD_DISTRIBUIDOR", anchor=tk.W, width=50)
        self.tree_pedidos.column("COD_SUCURSAL", anchor=tk.W, width=50)
        self.tree_pedidos.column("FECHA DEL PEDIDO", anchor=tk.W, width=60)
        self.tree_pedidos.column("CANTIDAD DE ARTÍCULOS", anchor=tk.W, width=100)
        self.tree_pedidos.column("PESO", anchor=tk.W, width=40)
        self.tree_pedidos.column("PRECIO", anchor=tk.W, width=40)
        
        self.tree_pedidos.heading("#0", text="NUM_PEDIDO", anchor=tk.W)
        self.tree_pedidos.heading("COD_PEDIDO", text="COD_PEDIDO", anchor=tk.W)
        self.tree_pedidos.heading("COD_DISTRIBUIDOR", text="COD_DISTRIBUIDOR", anchor=tk.W)
        self.tree_pedidos.heading("COD_SUCURSAL", text="COD_SUCURSAL", anchor=tk.W)
        self.tree_pedidos.heading("FECHA DEL PEDIDO", text="FECHA DEL PEDIDO", anchor=tk.W)
        self.tree_pedidos.heading("CANTIDAD DE ARTÍCULOS", text="CANTIDAD DE ARTÍCULOS", anchor=tk.W)
        self.tree_pedidos.heading("PESO", text="PESO", anchor=tk.W)
        self.tree_pedidos.heading("PRECIO", text="PRECIO", anchor=tk.W)

        self.tree_pedidos.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.title_lis_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tree_pedidos.pack(fill="both", expand=True)
        self.boton_mod_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.crear_listado()
        self.deiconify()

    def crear_listado(self):
        self.tree_pedidos.delete(*self.tree_pedidos.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for pedido in self.almacen_pedidos._pedidos:
            if (busqueda in pedido._cod_pedido.upper()
            or busqueda in pedido._cod_distribuidor.upper()
            or busqueda in pedido._cod_sucursal.upper()
            or busqueda in pedido._fecha_pedido.upper()
            or busqueda in pedido._cantidad_articulos.upper()
            or busqueda in pedido._peso.upper()
            or busqueda in pedido._precio.upper() or not busqueda):
                self.tree_pedidos.insert("", tk.END, text=f"{contador}",
                                            values=(pedido._cod_pedido, pedido._cod_distribuidor, pedido._cod_sucursal, 
                                            pedido._fecha_pedido, pedido._cantidad_articulos, pedido._peso,
                                            pedido._precio))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_pedidos.deiconify()

    def recoger_datos(self):
        dato_cod_pedido = self.cod_pedido_var.get()
        dato_cod_distribuidor = self.cod_distribuidor_var.get()
        dato_cod_sucursal = self.cod_sucursal_var.get().upper()
        dato_fecha_pedido = self.fecha_pedido_var.get().upper()
        dato_cantidad_articulos = self.cantidad_articulos_var.get().upper()
        dato_peso = self.peso_var.get().upper()
        dato_precio = self.precio_var.get().upper()
        return dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_cantidad_articulos, dato_peso, dato_precio

    def on_select(self, event):
        try:
            selected_item = self.tree_pedidos.selection()[0]
            values = self.tree_pedidos.item(selected_item)['values']
            self.cod_pedido_var.set(values[self.almacen_pedidos.CamposFicheroCsv.COD_PEDIDO])
            self.cod_distribuidor_var.set(values[self.almacen_pedidos.CamposFicheroCsv.COD_DISTRIBUIDOR])
            self.cod_sucursal_var.set(values[self.almacen_pedidos.CamposFicheroCsv.COD_SUCURSAL])
            self.fecha_pedido_var.set(values[self.almacen_pedidos.CamposFicheroCsv.FECHA_PEDIDO])
            self.cantidad_articulos_var.set(values[self.almacen_pedidos.CamposFicheroCsv.CANTIDAD_ARTICULOS])
            self.peso_var.set(values[self.almacen_pedidos.CamposFicheroCsv.PESO])
            self.precio_var.set(values[self.almacen_pedidos.CamposFicheroCsv.PRECIO])
        except IndexError:
            pass

    def ocultar_menu(self):
        self.withdraw()
        
    def abrir_ventana_mod_pedidos(self):
        dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_cantidad_articulos, dato_peso, dato_precio = self.recoger_datos()
        if (dato_cod_pedido == '' and dato_cod_distribuidor == '' 
        and dato_cod_sucursal == '' and dato_fecha_pedido == '' and dato_cantidad_articulos == ''
        and dato_peso == '' and dato_precio == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN ARTÍCULO")
        else:
            self.ocultar_menu()
            self.ventana_mod_pedidos.mostrar_menu()
            self.ventana_mod_pedidos.mainloop()
