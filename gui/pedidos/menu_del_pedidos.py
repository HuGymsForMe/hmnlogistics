import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelPedidos(tk.Toplevel):
    def __init__(self, master, almacen_pedidos, menu_pedidos):
        super().__init__(master)
        self.almacen_pedidos = almacen_pedidos
        self.menu_pedidos = menu_pedidos

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_PEDIDO = "Código de Pedido:"

        self.withdraw()
        self.minsize(300, 150)
        self.geometry("300x150+650+150")
        self.maxsize(300, 150)
        self.title("BORRAR PEDIDO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_pedido_seleccionado = tk.StringVar()

        self.title_del_pedidos = ttk.Label(self, text="BORRAR PEDIDO", font=("Helvetica", 12))
        self.print_cod_pedido = ttk.Label(self, text="CÓDIGO DE PEDIDO:", font=("Helvetica", 9))
        self.eleccion_cod_pedido = ttk.Combobox(self, values=[], textvariable=self.cod_pedido_seleccionado, foreground="gray")
        self.eleccion_cod_pedido.insert(0, self.PLACEHOLDER_COD_PEDIDO)
        self.eleccion_cod_pedido.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_pedido)
        self.eleccion_cod_pedido.bind('<FocusOut>', self.set_placeholder_eleccion_cod_pedido)
        self.boton_del_pedido = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_pedido)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_pedido()
        self.title_del_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_pedido(self):
        self.posibles_cod_pedido = self.almacen_pedidos.generar_combobox()
        self.eleccion_cod_pedido['values'] = self.posibles_cod_pedido

    def tratar_del_pedido(self):
        dato_borrar_pedido = self.cod_pedido_seleccionado.get()
        reaviso = messagebox.askyesno(message="¿DESEA ELIMINAR EL PEDIDO?")
        if (self.almacen_pedidos.del_datos(dato_borrar_pedido) and reaviso):
            articulo_cancel = messagebox.showinfo(message="PEDIDO ELMINADO CORRECTAMENTE")
        elif not reaviso:
            pass
        elif dato_borrar_pedido not in self.posibles_cod_pedido:
            articulo_not_found = messagebox.showerror(message="PEDIDO NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_pedido(self, event):
        if self.eleccion_cod_pedido.get() == self.PLACEHOLDER_COD_PEDIDO:
            self.eleccion_cod_pedido.delete(0, tk.END)
            self.eleccion_cod_pedido.config(foreground='black')

    def set_placeholder_eleccion_cod_pedido(self, event):
        if self.eleccion_cod_pedido.get() == "":
            self.eleccion_cod_pedido.insert(0, self.PLACEHOLDER_COD_PEDIDO)
            self.eleccion_cod_pedido.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_pedidos.deiconify() 

    def limpiar_campos(self):
        self.cod_pedido_seleccionado.set('')
        self.set_placeholder_eleccion_cod_pedido(None)  