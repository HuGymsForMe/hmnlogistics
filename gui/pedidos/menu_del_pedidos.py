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
        self.minsize(250, 125)
        self.geometry("250x125+650+150")
        self.maxsize(250, 125)
        self.title("BORRAR PEDIDO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_pedidos.deiconify()    