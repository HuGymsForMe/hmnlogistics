import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelSucursales(tk.Toplevel):
    def __init__(self, master, almacen_sucursales, almacen_departamentos, menu_sucursales):
        super().__init__(master)
        self.almacen_sucursales = almacen_sucursales
        self.almacen_departamentos = almacen_departamentos
        self.menu_sucursales = menu_sucursales

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_SUCURSAL = "Código de Sucursal:"

        self.withdraw()
        self.minsize(250, 150)
        self.geometry("250x150+650+150")
        self.maxsize(250, 150)
        self.title("BORRAR SUCURSAL")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_sucursal_seleccionado = tk.StringVar()
        
        self.title_del_sucursales = ttk.Label(self, text="BORRAR SUCURSAL", font=("Helvetica", 12))
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE SUCURSAL:", font=("Helvetica", 9))
        self.eleccion_cod_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_seleccionado, foreground="gray")
        self.eleccion_cod_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
        self.eleccion_cod_sucursal.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_sucursal)
        self.eleccion_cod_sucursal.bind('<FocusOut>', self.set_placeholder_eleccion_cod_sucursal)
        self.boton_del_sucursales = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_sucursal)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_sucursal()
        self.title_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_sucursal(self):
        self.posibles_cod_sucursal = self.almacen_sucursales.generar_combobox()
        self.eleccion_cod_sucursal['values'] = self.posibles_cod_sucursal

    def tratar_del_sucursal(self):
        dato_borrar_cod_sucursal = self.cod_sucursal_seleccionado.get()
        reaviso = messagebox.askyesno(message="  ¿DESEA ELIMINAR LA SUCURSAL?,  \nSE DESVINCULARÁN TODOS SUS DEPARTAMENTOS")
        if (self.almacen_sucursales.del_datos(dato_borrar_cod_sucursal) and reaviso):
            self.almacen_departamentos.del_departamentos_por_del_sucursal(dato_borrar_cod_sucursal)
            sucursal_cancel = messagebox.showinfo(message="SUCURSAL ELMINADO CORRECTAMENTE")
            self.on_close()
        elif dato_borrar_cod_sucursal not in self.posibles_cod_sucursal:
            sucursal_not_found = messagebox.showerror(message="SUCURSAL NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_cod_sucursal.get() == self.PLACEHOLDER_COD_SUCURSAL:
            self.eleccion_cod_sucursal.delete(0, tk.END)
            self.eleccion_cod_sucursal.config(foreground='black')

    def set_placeholder_eleccion_cod_sucursal(self, event):
        if self.eleccion_cod_sucursal.get() == "":
            self.eleccion_cod_sucursal.insert(0, self.PLACEHOLDER_COD_SUCURSAL)
            self.eleccion_cod_sucursal.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_sucursales.deiconify() 

    def limpiar_campos(self):
        self.cod_sucursal_seleccionado.set('')
        self.set_placeholder_eleccion_cod_sucursal(None) 