import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelSucursales(tk.Toplevel):
    def __init__(self, master, menu_sucursales):
        super().__init__(master)
        self.menu_sucursales = menu_sucursales

        self.withdraw()
        self.minsize(250, 125)
        self.geometry("250x125+650+150")
        self.maxsize(250, 125)
        self.title("BORRAR CLIENTE")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.title_del_sucursales = ttk.Label(self, text="BORRAR CLIENTE", font=("Helvetica", 12))
        self.print_del_sucursales = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.input_del_sucursales = ttk.Entry(self, foreground="gray")

        self.title_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

    def on_close(self):
       self.withdraw()
       self.menu_sucursales.deiconify()