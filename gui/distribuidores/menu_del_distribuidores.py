import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class DelDistribuidores(tk.Toplevel):
    def __init__(self, master, almacen_distribuidores, almacen_pedidos, menu_distribuidores):
        super().__init__(master)
        self.almacen_distribuidores = almacen_distribuidores
        self.almacen_pedidos = almacen_pedidos
        self.menu_distribuidores = menu_distribuidores

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_DISTRIBUIDOR = "Código de Distribuidor:"

        self.withdraw()
        self.minsize(300, 150)
        self.geometry("300x150+650+150")
        self.maxsize(300, 150)
        self.title("BORRAR PEDIDO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_distribuidor_seleccionado = tk.StringVar()

        self.title_del_distribuidores = ttk.Label(self, text="BORRAR DISTRIBUIDO", font=("Helvetica", 12))
        self.print_cod_distribuidor = ttk.Label(self, text="CÓDIGO DE DISTRIBUIDOR:", font=("Helvetica", 9))
        self.eleccion_cod_distribuidor = ttk.Combobox(self, values=[], textvariable=self.cod_distribuidor_seleccionado, foreground="gray")
        self.eleccion_cod_distribuidor.insert(0, self.PLACEHOLDER_COD_DISTRIBUIDOR)
        self.eleccion_cod_distribuidor.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_distribuidor)
        self.eleccion_cod_distribuidor.bind('<FocusOut>', self.set_placeholder_eleccion_cod_distribuidor)
        self.boton_del_distribuidor = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_distribuidor)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_pedido()
        self.title_del_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_pedido(self):
        self.posibles_cod_distribuidor = self.almacen_distribuidores.generar_combobox()
        self.eleccion_cod_distribuidor['values'] = self.posibles_cod_distribuidor

    def tratar_del_distribuidor(self):
        dato_borrar_distribuidor = self.cod_distribuidor_seleccionado.get()
        reaviso = messagebox.askyesno(message=" ¿DESEA ELIMINAR EL DISTRIBUIDOR?, \nSE DESVINCULARÁN TODOS SUS PEDIDOS")
        if (self.almacen_distribuidores.del_datos(dato_borrar_distribuidor) and reaviso):
            self.almacen_pedidos.del_pedidos_por_del_distribuidor(dato_borrar_distribuidor)
            distribuidor_cancel = messagebox.showinfo(message="DISTRIBUIDOR ELMINADO CORRECTAMENTE")
            self.on_close()
        elif dato_borrar_distribuidor not in self.posibles_cod_distribuidor:
            distribuidor_not_found = messagebox.showerror(message="DISTRIBUIDOR NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_distribuidor(self, event):
        if self.eleccion_cod_distribuidor.get() == self.PLACEHOLDER_COD_DISTRIBUIDOR:
            self.eleccion_cod_distribuidor.delete(0, tk.END)
            self.eleccion_cod_distribuidor.config(foreground='black')

    def set_placeholder_eleccion_cod_distribuidor(self, event):
        if self.eleccion_cod_distribuidor.get() == "":
            self.eleccion_cod_distribuidor.insert(0, self.PLACEHOLDER_COD_DISTRIBUIDOR)
            self.eleccion_cod_distribuidor.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_distribuidores.deiconify() 

    def limpiar_campos(self):
        self.cod_distribuidor_seleccionado.set('')
        self.set_placeholder_eleccion_cod_distribuidor(None)  