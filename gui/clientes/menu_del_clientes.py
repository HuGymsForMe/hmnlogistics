import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelClientes(tk.Toplevel):
    def __init__(self, master, almacen_clientes, almacen_articulos, menu_clientes):
        super().__init__(master)
        self.almacen_clientes = almacen_clientes
        self.almacen_articulos = almacen_articulos
        self.menu_clientes = menu_clientes

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_CLIENTE = "Código de Cliente:"

        self.withdraw()
        self.minsize(250, 125)
        self.geometry("250x125+650+150")
        self.maxsize(250, 125)
        self.title("BORRAR CLIENTE")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_cliente_seleccionado = tk.StringVar()

        self.title_del_clientes = ttk.Label(self, text="BORRAR CLIENTE", font=("Helvetica", 12))
        self.print_cod_cliente= ttk.Label(self, text="CÓDIGO DE CLIENTE:", font=("Helvetica", 9))
        self.eleccion_cod_cliente = ttk.Combobox(self, values=[], textvariable=self.cod_cliente_seleccionado, foreground="gray")
        self.eleccion_cod_cliente.insert(0, self.PLACEHOLDER_COD_CLIENTE)
        self.eleccion_cod_cliente.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_cliente)
        self.eleccion_cod_cliente.bind('<FocusOut>', self.set_placeholder_eleccion_cod_cliente)
        self.boton_del_cliente = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_cliente)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_cliente()
        self.title_del_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_cliente.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_cliente(self):
        self.posibles_cod_cliente = self.almacen_clientes.generar_combobox()
        self.eleccion_cod_cliente['values'] = self.posibles_cod_cliente

    def tratar_del_cliente(self):
        dato_borrar_cliente = self.cod_cliente_seleccionado.get()
        reaviso = messagebox.askyesno(message="¿DESEA ELIMINAR EL CLIENTE?")
        if (self.almacen_clientes.del_datos(dato_borrar_cliente) and reaviso):
            self.almacen_articulos.del_articulos_por_del_cliente(dato_borrar_cliente)
            cliente_cancel = messagebox.showinfo(message="CLIENTE ELMINADO CORRECTAMENTE") #AVISAR AL USUARIO QUE SI BORRA EL CLIENTE, BORRA SUS ARTÍCULOS
        else:
            cliente_not_found = messagebox.showerror(message="CLIENTE NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_cliente(self, event):
        if self.eleccion_cod_cliente.get() == self.PLACEHOLDER_COD_CLIENTE:
            self.eleccion_cod_cliente.delete(0, tk.END)
            self.eleccion_cod_cliente.config(foreground='black')

    def set_placeholder_eleccion_cod_cliente(self, event):
        if self.eleccion_cod_cliente.get() == "":
            self.eleccion_cod_cliente.insert(0, self.PLACEHOLDER_COD_CLIENTE)
            self.eleccion_cod_cliente.config(foreground='gray')
    
    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_clientes.deiconify()

    def limpiar_campos(self):
        self.cod_cliente_seleccionado.set('')
        self.set_placeholder_eleccion_cod_cliente(None)