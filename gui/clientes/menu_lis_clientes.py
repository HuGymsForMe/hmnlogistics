import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from gui.clientes.menu_mod_clientes import ModClientes

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

        self.minsize(900, 350)
        self.geometry("900x350+400+150")
        self.maxsize(1300, 350)

        self.cod_cliente_var = tk.StringVar()
        self.cod_sucursal_var = tk.StringVar()
        self.nombre_var = tk.StringVar()

        self.ventana_mod_clientes = ModClientes(self.master, self.almacen_clientes, 
        self.almacen_sucursal, self.cod_cliente_var, self.cod_sucursal_var, self.nombre_var, self)

        self.withdraw()
        self.title("MIS SUCURSALES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.title_lis_clientes = ttk.Label(self, text="MIS CLIENTES", font=("Helvetica", 12)) 
        self.tree_clientes = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        self.boton_mod_articulos = ttk.Button(self, text="MODIFICAR CLIENTE", command=self.abrir_ventana_mod_clientes)

        #TABLA
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
        self.title_lis_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.tree_clientes.pack(fill="both", expand=True)
        self.boton_mod_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.crear_listado()
        self.deiconify()

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

    def on_select(self, event):
        try:
            selected_item = self.tree_clientes.selection()[0]
            values = self.tree_clientes.item(selected_item)['values']
            self.cod_cliente_var.set(values[self.ConstantesListado.COD_CLIENTE])
            self.cod_sucursal_var.set(values[self.ConstantesListado.COD_SUCURSAL])
            self.nombre_var.set(values[self.ConstantesListado.NOMBRE])
        except IndexError:
            pass

    def ocultar_menu(self):
        self.withdraw()
        
    def abrir_ventana_mod_clientes(self):
        dato_cod_cliente, dato_cod_sucursal, dato_nombre = self.recoger_datos()
        if (dato_cod_cliente == '' and dato_cod_sucursal == '' and dato_nombre == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN CLIENTE")
        else:
            self.ocultar_menu()
            self.ventana_mod_clientes.mostrar_menu()
            self.ventana_mod_clientes.mainloop()