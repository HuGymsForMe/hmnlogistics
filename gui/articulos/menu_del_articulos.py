import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.menu_articulos = menu_articulos

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_ARTICULO = "Código de Artículo:"

        self.withdraw()
        self.minsize(250, 150)
        self.geometry("250x150+650+150")
        self.maxsize(250, 150)
        self.title("BORRAR ARTÍCULO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_articulo_seleccionado = tk.StringVar()

        self.title_del_articulos = ttk.Label(self, text="BORRAR ARTÍCULO", font=("Helvetica", 12))
        self.print_cod_articulo = ttk.Label(self, text="CÓDIGO DE ARTÍCULO:", font=("Helvetica", 9))
        self.eleccion_cod_articulo = ttk.Combobox(self, values=[], textvariable=self.cod_articulo_seleccionado, foreground="gray")
        self.eleccion_cod_articulo.insert(0, self.PLACEHOLDER_COD_ARTICULO)
        self.eleccion_cod_articulo.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_articulo)
        self.eleccion_cod_articulo.bind('<FocusOut>', self.set_placeholder_eleccion_cod_articulo)
        self.boton_del_articulo = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_articulo)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_articulo()
        self.title_del_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_articulo.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_articulo(self):
        self.posibles_cod_articulo = self.almacen_articulos.generar_combobox()
        self.eleccion_cod_articulo['values'] = self.posibles_cod_articulo

    def tratar_del_articulo(self):
        dato_borrar_articulo = self.cod_articulo_seleccionado.get()
        reaviso = messagebox.askyesno(message="¿DESEA ELIMINAR EL ARTÍCULO?")
        if (self.almacen_articulos.del_datos(dato_borrar_articulo) and reaviso):
            articulo_cancel = messagebox.showinfo(message="ARTÍCULO ELMINADO CORRECTAMENTE")
            self.on_close()
        else:
            articulo_not_found = messagebox.showerror(message="ARTÍCULO NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_articulo(self, event):
        if self.eleccion_cod_articulo.get() == self.PLACEHOLDER_COD_ARTICULO:
            self.eleccion_cod_articulo.delete(0, tk.END)
            self.eleccion_cod_articulo.config(foreground='black')

    def set_placeholder_eleccion_cod_articulo(self, event):
        if self.eleccion_cod_articulo.get() == "":
            self.eleccion_cod_articulo.insert(0, self.PLACEHOLDER_COD_ARTICULO)
            self.eleccion_cod_articulo.config(foreground='gray')
    
    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_articulos.deiconify()

    def limpiar_campos(self):
        self.cod_articulo_seleccionado.set('')
        self.set_placeholder_eleccion_cod_articulo(None)