import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class LisClientes(tk.Toplevel):
    class ConstantesListado:
        COD_CLIENTE = 0
        COD_SUCURSAL = 1
        NOMBRE = 2

        @staticmethod
        def opciones():
            return range(LisClientes.ConstantesListado.COD_CLIENTE,
                        LisClientes.ConstantesListado.NOMBRE+1)

    def __init__(self, master, almacen_clientes, almacen_sucursal, menu_clientes):
        super().__init__(master)
        self.almacen_clientes = almacen_clientes
        self.almacen_sucursal = almacen_sucursal
        self.menu_clientes = menu_clientes

        self.minsize(900, 450)
        self.geometry("900x450+400+150")
        self.maxsize(1300, 450)

        self.cod_cliente_var = tk.StringVar()
        self.cod_sucursal_var = tk.StringVar()
        self.nombre_var = tk.StringVar()

        self.withdraw()
        self.title("MIS SUCURSALES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.title_lis_clientes = ttk.Label(self, text="MIS CLIENTES", font=("Helvetica", 12)) 
        self.tree_clientes = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        #MODIFICACION
        self.print_cod_cliente = ttk.Label(self, text="CÓDIGO DE CLIENTE:", font=("Helvetica", 9))
        self.input_cod_cliente = ttk.Entry(self, textvariable=self.cod_cliente_var, state='readonly')
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_cod_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_var)
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, textvariable=self.nombre_var)
        self.boton_mod_clientes = ttk.Button(self, text="MODIFICAR", command=self.realizar_modificaciones)

        self.tree_clientes["columns"] = ("COD_CLIENTE", "COD_SUCURSAL", "NOMBRE")  
        
        self.tree_clientes.column("#0", width=100, stretch=tk.NO)
        self.tree_clientes.column("COD_CLIENTE", anchor=tk.W, width=50)
        self.tree_clientes.column("COD_SUCURSAL", anchor=tk.W, width=60)
        self.tree_clientes.column("NOMBRE", anchor=tk.W, width=100)
        
        self.tree_clientes.heading("#0", text="NUM_CLIENTE", anchor=tk.W)
        self.tree_clientes.heading("COD_CLIENTE", text="COD_CLIENTE", anchor=tk.W)
        self.tree_clientes.heading("COD_SUCURSAL", text="COD_SUCURSAL", anchor=tk.W,)
        self.tree_clientes.heading("NOMBRE", text="NOMBRE", anchor=tk.W)

        self.tree_clientes.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_sucursal()
        self.title_lis_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tree_clientes.pack(fill="both", expand=True)

        #CAMPOS MODIFICACIONES
        self.print_cod_cliente.pack()
        self.input_cod_cliente.pack()
        self.print_cod_sucursal.pack()
        self.eleccion_cod_sucursal.pack()
        self.print_nombre.pack()
        self.input_nombre.pack()
        self.boton_mod_clientes.pack()
        self.crear_listado()
        self.deiconify()

    def actualizar_posibles_cod_sucursal(self):
        self.posibles_cod_sucursal = self.almacen_sucursal.generar_combobox()
        self.eleccion_cod_sucursal['values'] = self.posibles_cod_sucursal

    def crear_listado(self):
        self.tree_clientes.delete(*self.tree_clientes.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for cliente in self.almacen_clientes._clientes:
            if (busqueda in cliente._cod_cliente.upper()
            or busqueda in cliente._cod_sucursal.upper()
            or busqueda in cliente._nombre.upper() or not busqueda):
                self.tree_clientes.insert("", tk.END, text=f"{contador}",
                                            values=(cliente._cod_cliente, cliente._cod_sucursal, cliente._nombre))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_clientes.deiconify()

    def recoger_datos(self):
        dato_cod_cliente = self.cod_cliente_var.get()
        dato_cod_sucursal = self.cod_sucursal_var.get()
        dato_nombre = self.nombre_var.get().upper()
        return dato_cod_cliente, dato_cod_sucursal, dato_nombre

    def realizar_modificaciones(self):
        dato_cod_cliente, dato_cod_sucursal, dato_nombre = self.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR EL CLIENTE?")
        if reaviso:
            if dato_cod_sucursal in self.posibles_cod_sucursal:
                self.almacen_clientes.del_datos(dato_cod_cliente)
                self.almacen_clientes.add_datos(dato_cod_cliente, dato_cod_sucursal, dato_nombre)
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_select(self, event):
        try:
            selected_item = self.tree_clientes.selection()[0]
            values = self.tree_clientes.item(selected_item)['values']
            self.cod_cliente_var.set(values[self.ConstantesListado.COD_CLIENTE])
            self.cod_sucursal_var.set(values[self.ConstantesListado.COD_SUCURSAL])
            self.nombre_var.set(values[self.ConstantesListado.NOMBRE])
        except IndexError:
            pass