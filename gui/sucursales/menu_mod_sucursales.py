import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class ModSucursales(tk.Toplevel):
    def __init__(self, master, almacen_sucursales, cod_sucursal_var, provincia_var, direccion_var, menu_lis_sucursales):
        super().__init__(master)
        self.almacen_sucursales = almacen_sucursales
        self.cod_sucursal_var = cod_sucursal_var
        self.provincia_var = provincia_var
        self.direccion_var = direccion_var
        self.menu_lis_sucursales = menu_lis_sucursales

        self.withdraw()
        self.minsize(250, 250)
        self.geometry("250x250+650+100")
        self.maxsize(250, 250)
        self.title("MODIFICAR SUCURSAL")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.input_cod_sucursal = ttk.Entry(self, textvariable=self.cod_sucursal_var, state='readonly')
        self.print_provincia = ttk.Label(self, text="PROVINCIA:", font=("Helvetica", 9))
        self.posibles_provincias = [
    "ÁLAVA", "ALBACETE", "ALICANTE", "ALMERÍA", "ASTURIAS", "ÁVILA", "BADAJOZ", "BARCELONA", "BURGOS",
    "CÁCERES", "CÁDIZ", "CANTABRIA", "CASTELLÓN", "CEUTA", "CIUDAD REAL", "CÓRDOBA", "CUENCA", "GERONA", 
    "GRANADA", "GUADALAJARA", "GUIPÚZCOA", "HUELVA", "HUESCA", "ISLAS BALEARES", "JAÉN", "LA CORUÑA", 
    "LA RIOJA", "LAS PALMAS", "LEÓN", "LÉRIDA", "LUGO", "MADRID", "MÁLAGA", "MELILA", "MURCIA", "NAVARRA",
    "ORENSE", "PALENCIA", "PONTEVEDRA", "SALAMANCA", "SANTA CRUZ DE TENERIFE", "SEGOVIA", "SEVILLA", 
    "SORIA", "TARRAGONA", "TERUEL", "TOLEDO", "VALENCIA", "VALLADOLID", "VIZCAYA", "ZAMORA", "ZARAGOZA"
]
        self.eleccion_provincia = ttk.Combobox(self, values=self.posibles_provincias, textvariable=self.provincia_var)
        self.print_direccion = ttk.Label(self, text="DIRECCION:", font=("Helvetica", 9))
        self.input_direccion = ttk.Entry(self, textvariable=self.direccion_var)
        self.boton_mod_sucursales = ttk.Button(self, text="REALIZAR CAMBIOS", command=self.realizar_modificaciones)

    def mostrar_menu(self):
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_provincia.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_provincia.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_direccion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_direccion.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def realizar_modificaciones(self):
        dato_cod_sucursal, dato_provincia, dato_direccion = self.menu_lis_sucursales.recoger_datos()
        reaviso = messagebox.askyesno(message="¿DESEA MODIFICAR LA SUCURSAL?")
        if reaviso:
            if dato_provincia in self.posibles_provincias:
                self.almacen_sucursales.del_datos(dato_cod_sucursal)
                self.almacen_sucursales.add_datos(dato_cod_sucursal, dato_provincia, dato_direccion)
                messagebox.showinfo(message="LA SUCURSAL SE MODIFICÓ CORRECTAMENTE")
                self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")

    def on_close(self):
        self.withdraw()
        self.menu_lis_sucursales.deiconify()