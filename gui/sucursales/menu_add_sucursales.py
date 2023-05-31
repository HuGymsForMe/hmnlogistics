import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class AddSucursales(tk.Toplevel):
    def __init__(self, master, almacen_sucursales, menu_sucursales):
        super().__init__(master)
        self.almacen_sucursales = almacen_sucursales
        self.menu_sucursales = menu_sucursales

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_PROVINCIA = "Ej: Álava"
        self.PLACEHOLDER_DIRECCION = "Dirección:"

        self.withdraw()
        self.minsize(200, 200)
        self.geometry("200x200+650+100")
        self.maxsize(200, 200)
        self.title("AÑADIR SUCURSAL")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.provincia_seleccionada = tk.StringVar()
        self.input_direccion_seleccionada = tk.StringVar()

        self.title_add_sucursal = ttk.Label(self, text="AÑADIR SUCURSAL", font=("Helvetica", 12))
        self.print_provincia = ttk.Label(self, text="PROVINCIA:", font=("Helvetica", 9))
        self.posibles_provincias = [
    "ÁLAVA", "ALBACETE", "ALICANTE", "ALMERÍA", "ASTURIAS", "ÁVILA", "BADAJOZ", "BARCELONA", "BURGOS",
    "CÁCERES", "CÁDIZ", "CANTABRIA", "CASTELLÓN", "CEUTA", "CIUDAD REAL", "CÓRDOBA", "CUENCA", "GERONA", 
    "GRANADA", "GUADALAJARA", "GUIPÚZCOA", "HUELVA", "HUESCA", "ISLAS BALEARES", "JAÉN", "LA CORUÑA", 
    "LA RIOJA", "LAS PALMAS", "LEÓN", "LÉRIDA", "LUGO", "MADRID", "MÁLAGA", "MELILA", "MURCIA", "NAVARRA",
    "ORENSE", "PALENCIA", "PONTEVEDRA", "SALAMANCA", "SANTA CRUZ DE TENERIFE", "SEGOVIA", "SEVILLA", 
    "SORIA", "TARRAGONA", "TERUEL", "TOLEDO", "VALENCIA", "VALLADOLID", "VIZCAYA", "ZAMORA", "ZARAGOZA"
]
        self.eleccion_provincia = ttk.Combobox(self, values=self.posibles_provincias, textvariable=self.provincia_seleccionada, foreground="gray")
        self.eleccion_provincia.insert(0, self.PLACEHOLDER_PROVINCIA)
        self.eleccion_provincia.bind('<FocusIn>', self.clear_placeholder_eleccion_provincia)
        self.eleccion_provincia.bind('<FocusOut>', self.set_placeholder_eleccion_provincia)
        self.print_direccion = ttk.Label(self, text="DIRECCIÓN", font=("Helvetica", 9))
        self.input_direccion = ttk.Entry(self, foreground="gray", textvariable=self.input_direccion_seleccionada)
        self.input_direccion.insert(0, self.PLACEHOLDER_DIRECCION)
        self.input_direccion.bind('<FocusIn>', self.clear_placeholder_input_direccion)
        self.input_direccion.bind('<FocusOut>', self.set_placeholder_input_direccion)
        self.boton_add_sucursal = ttk.Button(self, text="AÑADIR", command=self.comprobar_sucursales)

    def mostrar_menu(self):
        self.title_add_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_provincia.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_provincia.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_direccion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_direccion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_add_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def recoger_datos_sucursales(self):
        dato_provincia = self.provincia_seleccionada.get()
        dato_direccion = self.input_direccion_seleccionada.get().upper()
        dato_cod_sucursal = f"S{str(random.randrange(1,1001))}"
        return dato_cod_sucursal, dato_provincia, dato_direccion

    def comprobar_sucursales(self):
        dato_cod_sucursal, dato_provincia, dato_direccion = self.recoger_datos_sucursales()
        if dato_provincia in self.posibles_provincias:
            datos = messagebox.askyesno(message=f"DATOS:\nCÓDIGO DE SUCURSAL:{dato_cod_sucursal}\nPROVINCIA:{dato_provincia}\nDIRECCIÓN:{dato_direccion}")
            if datos:
                if (self.almacen_sucursales.add_datos(dato_cod_sucursal, dato_provincia, dato_direccion)):
                    cod_repetido = messagebox.showinfo(message="EL CÓDIGO GENERADO POR EL SISTEMA YA ESTÁ ASIGNADO")
        else:
            datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_provincia(self, event):
        if self.eleccion_provincia.get() == self.PLACEHOLDER_PROVINCIA:
            self.eleccion_provincia.delete(0, tk.END)
            self.eleccion_provincia.config(foreground='black')

    def set_placeholder_eleccion_provincia(self, event):
        if self.eleccion_provincia.get() == "":
            self.eleccion_provincia.insert(0, self.PLACEHOLDER_PROVINCIA)
            self.eleccion_provincia.config(foreground='gray')

    def clear_placeholder_input_direccion(self, event):
        if self.input_direccion.get() == self.PLACEHOLDER_DIRECCION:
            self.input_direccion.delete(0, tk.END)
            self.input_direccion.config(foreground='black')

    def set_placeholder_input_direccion(self, event):
        if self.input_direccion.get() == "":
            self.input_direccion.insert(0, self.PLACEHOLDER_DIRECCION)
            self.input_direccion.config(foreground='gray')
    
    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_sucursales.deiconify()

    def limpiar_campos(self):
        self.provincia_seleccionada.set('')
        self.set_placeholder_eleccion_provincia(None)
        self.input_direccion_seleccionada.set('')
        self.set_placeholder_input_direccion(None)

    
