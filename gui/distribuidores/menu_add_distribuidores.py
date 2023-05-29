import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class AddDistribuidores(tk.Toplevel):
    def __init__(self, master, almacen_distribuidores, menu_distribuidores):
        super().__init__(master)
        self.almacen_distribuidores = almacen_distribuidores
        self.menu_distribuidores = menu_distribuidores

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_NOMBRE = "Nombre:"

        self.withdraw()
        self.minsize(200, 150)
        self.geometry("200x150+650+100")
        self.maxsize(200, 150)
        self.title("AÑADIR DISTRIBUIDOR")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.input_nombre_seleccionado = tk.StringVar()

        self.title_add_distribuidores = ttk.Label(self, text="AÑADIR DISTRIBUIDOR", font=("Helvetica", 12))
        self.print_nombre = ttk.Label(self, text="NOMBRE:", font=("Helvetica", 9))
        self.input_nombre = ttk.Entry(self, foreground="gray", textvariable=self.input_nombre_seleccionado)
        self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
        self.input_nombre.bind('<FocusIn>', self.clear_placeholder_input_nombre)
        self.input_nombre.bind('<FocusOut>', self.set_placeholder_input_nombre)
        self.boton_add_sucursal = ttk.Button(self, text="AÑADIR", command=self.comprobar_distribuidores)

    def mostrar_menu(self):
        self.title_add_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_nombre.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def recoger_datos_distribuidores(self):
        dato_nombre = self.input_nombre_seleccionado.get().upper()
        dato_cod_distribuidor = f"D{str(random.randrange(1,1001))}"
        return dato_cod_distribuidor, dato_nombre

    def comprobar_distribuidores(self):
        dato_cod_distribuidor, dato_nombre = self.recoger_datos_distribuidores()
        datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE DISTRIBUIDOR: {dato_cod_distribuidor}\nNOMBRE: {dato_nombre}")
        if datos:
            if self.almacen_distribuidores.add_datos(dato_cod_distribuidor, dato_nombre):
                cod_repetido = messagebox.showinfo(message="EL DISTRIBUIDOR YA SE ENCUENTRA EN EL SISTEMA")
            else:
                self.on_close()

    #PLACEHOLDERS
    def clear_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == self.PLACEHOLDER_NOMBRE:
            self.input_nombre.delete(0, tk.END)
            self.input_nombre.config(foreground='black')

    def set_placeholder_input_nombre(self, event):
        if self.input_nombre.get() == "":
            self.input_nombre.insert(0, self.PLACEHOLDER_NOMBRE)
            self.input_nombre.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_distribuidores.deiconify()

    def limpiar_campos(self):
        self.input_nombre_seleccionado.set('')
        self.set_placeholder_input_nombre(None)

    