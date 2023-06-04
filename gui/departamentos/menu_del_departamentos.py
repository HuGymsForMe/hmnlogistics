import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class DelDepartamentos(tk.Toplevel):
    def __init__(self, master, almacen_departamentos, almacen_empleados, menu_departamentos):
        super().__init__(master)
        self.almacen_departamentos = almacen_departamentos
        self.almacen_empleados = almacen_empleados
        self.menu_departamentos = menu_departamentos

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_COD_DEPARTAMENTO = "Código de Departamento:"

        self.withdraw()
        self.minsize(300, 150)
        self.geometry("300x150+650+150")
        self.maxsize(300, 150)
        self.title("BORRAR DEPARTAMENTO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.cod_departamento_seleccionado = tk.StringVar()

        self.title_del_departamentos = ttk.Label(self, text="BORRAR DEPARTAMENTO", font=("Helvetica", 12))
        self.print_cod_departamento = ttk.Label(self, text="CÓDIGO DE DEPARTAMENTO:", font=("Helvetica", 9))
        self.eleccion_cod_departamento = ttk.Combobox(self, values=[], textvariable=self.cod_departamento_seleccionado, foreground="gray")
        self.eleccion_cod_departamento.insert(0, self.PLACEHOLDER_COD_DEPARTAMENTO)
        self.eleccion_cod_departamento.bind('<FocusIn>', self.clear_placeholder_eleccion_cod_departamento)
        self.eleccion_cod_departamento.bind('<FocusOut>', self.set_placeholder_eleccion_cod_departamento)
        self.boton_del_departamento = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_departamento)

    def mostrar_menu(self):
        self.actualizar_posibles_cod_departamento()
        self.title_del_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_cod_departamento(self):
        self.posibles_cod_departamento = self.almacen_departamentos.generar_combobox()
        self.eleccion_cod_departamento['values'] = self.posibles_cod_departamento

    def tratar_del_departamento(self):
        dato_borrar_departamento = self.cod_departamento_seleccionado.get()
        reaviso = messagebox.askyesno(message="  ¿DESEA ELIMINAR EL DEPARTAMENTO?,  \nSE DESVINCULARÁN TODOS SUS EMPLEADOS")
        if (self.almacen_departamentos.del_datos(dato_borrar_departamento) and reaviso):
            self.almacen_empleados.del_empleados_por_del_departamento(dato_borrar_departamento)
            departamento_cancel = messagebox.showinfo(message="DEPARTAMENTO ELMINADO CORRECTAMENTE")
            self.on_close()
        elif not reaviso:
            pass
        elif dato_borrar_departamento not in self.posibles_cod_departamento:
            departamento_not_found = messagebox.showerror(message="DEPARTAMENTO NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_cod_departamento(self, event):
        if self.eleccion_cod_departamento.get() == self.PLACEHOLDER_COD_DEPARTAMENTO:
            self.eleccion_cod_departamento.delete(0, tk.END)
            self.eleccion_cod_departamento.config(foreground='black')

    def set_placeholder_eleccion_cod_departamento(self, event):
        if self.eleccion_cod_departamento.get() == "":
            self.eleccion_cod_departamento.insert(0, self.PLACEHOLDER_COD_DEPARTAMENTO)
            self.eleccion_cod_departamento.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_departamentos.deiconify() 

    def limpiar_campos(self):
        self.cod_departamento_seleccionado.set('')
        self.set_placeholder_eleccion_cod_departamento(None) 