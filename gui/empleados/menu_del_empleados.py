import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class DelEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.menu_empleados = menu_empleados

        #FORMATO PLACEHOLDERS
        self.PLACEHOLDER_DNI = "Ej 00000000B:"

        self.withdraw()
        self.minsize(250, 150)
        self.geometry("250x150+650+150")
        self.maxsize(250, 150)
        self.title("BORRAR EMPLEADO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.dni_seleccionado = tk.StringVar()

        self.title_del_departamentos = ttk.Label(self, text="BORRAR EMPLEADO", font=("Helvetica", 12))
        self.print_dni = ttk.Label(self, text="DNI DEL EMPLEADO:", font=("Helvetica", 9))
        self.eleccion_dni = ttk.Combobox(self, values=[], textvariable=self.dni_seleccionado, foreground="gray")
        self.eleccion_dni.insert(0, self.PLACEHOLDER_DNI)
        self.eleccion_dni.bind('<FocusIn>', self.clear_placeholder_eleccion_dni)
        self.eleccion_dni.bind('<FocusOut>', self.set_placeholder_eleccion_dni)
        self.boton_del_departamento = ttk.Button(self, text="ELIMINAR", command=self.tratar_del_empleado)

    def mostrar_menu(self):
        self.actualizar_posibles_dni()
        self.title_del_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_dni.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_del_departamento.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_dni(self):
        self.posibles_dni = self.almacen_empleados.generar_combobox()
        self.eleccion_dni['values'] = self.posibles_dni

    def tratar_del_empleado(self):
        dato_dni = self.dni_seleccionado.get()
        reaviso = messagebox.askyesno(message="¿DESEA ELIMINAR EL EMPLEADO?")
        if self.almacen_empleados.del_datos(dato_dni) and reaviso:
            pass
        if self.almacen_empleados.del_datos_2(dato_dni) and reaviso:
            empleado_cancel = messagebox.showinfo(message="EMPLEADO ELMINADO CORRECTAMENTE")
            self.on_close()
        elif not reaviso:
            pass
        elif dato_dni not in self.posibles_dni:
            empleado_not_found = messagebox.showerror(message="EMPLEADO NO ENCONTRADO EN EL SISTEMA")

    #PLACEHOLDERS
    def clear_placeholder_eleccion_dni(self, event):
        if self.eleccion_dni.get() == self.PLACEHOLDER_DNI:
            self.eleccion_dni.delete(0, tk.END)
            self.eleccion_dni.config(foreground='black')

    def set_placeholder_eleccion_dni(self, event):
        if self.eleccion_dni.get() == "":
            self.eleccion_dni.insert(0, self.PLACEHOLDER_DNI)
            self.eleccion_dni.config(foreground='gray')

    def on_close(self):
        self.withdraw()
        self.limpiar_campos()
        self.menu_empleados.deiconify() 

    def limpiar_campos(self):
        self.dni_seleccionado.set('')
        self.set_placeholder_eleccion_dni(None) 
