import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from gui.empleados.menu_mod_empleados import ModEmpleados

class LisEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, almacen_departamentos, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.almacen_departamentos = almacen_departamentos
        self.menu_empleados = menu_empleados
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png') 

        self.minsize(800, 400)
        self.geometry("800x400+650+150")
        self.maxsize(800, 400)

        self.withdraw()
        self.title("MIS EMPLEADOS")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.cod_empleado_var = tk.StringVar()
        self.cod_departamento_var = tk.StringVar()
        self.dni_var = tk.StringVar()
        self.fecha_alta_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        self.oficio_var = tk.StringVar()

        self.ventana_mod_empleados = ModEmpleados(self.master, self.almacen_empleados, self.almacen_departamentos, 
        self.cod_empleado_var, self.cod_departamento_var, self.dni_var, self.fecha_alta_var, self.telefono_var, 
        self.salario_var, self.oficio_var, self)

        self.title_lis_empleados = ttk.Label(self, text="MIS EMPLEADOS", font=("Helvetica", 12)) 
        self.tree_empleados = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        self.boton_mod_empleados = ttk.Button(self, text="MODIFICAR EMPLEADO", command=self.abrir_ventana_mod_empleados)

        #TABLA
        self.tree_empleados["columns"] = ("COD_EMPLEADO", "COD_DEPARTAMENTO", "DNI", "FECHA DE ALTA", "TELÉFONO", "SALARIO", "OFICIO")  
        
        self.tree_empleados.column("#0", width=100, stretch=tk.NO)
        self.tree_empleados.column("COD_EMPLEADO", anchor=tk.W, width=60)
        self.tree_empleados.column("COD_DEPARTAMENTO", anchor=tk.W, width=60)
        self.tree_empleados.column("DNI", anchor=tk.W, width=60)
        self.tree_empleados.column("FECHA DE ALTA", anchor=tk.W, width=60)
        self.tree_empleados.column("TELÉFONO", anchor=tk.W, width=60)
        self.tree_empleados.column("SALARIO", anchor=tk.W, width=60)
        self.tree_empleados.column("OFICIO", anchor=tk.W, width=60)
        
        self.tree_empleados.heading("#0", text="NUM_EMPLEADO", anchor=tk.W)
        self.tree_empleados.heading("COD_EMPLEADO", text="COD_EMPLEADO", anchor=tk.W,)
        self.tree_empleados.heading("COD_DEPARTAMENTO", text="COD_DEPARTAMENTO", anchor=tk.W)
        self.tree_empleados.heading("DNI", text="DNI", anchor=tk.W)
        self.tree_empleados.heading("FECHA DE ALTA", text="FECHA DE ALTA", anchor=tk.W,)
        self.tree_empleados.heading("TELÉFONO", text="TELÉFONO", anchor=tk.W)
        self.tree_empleados.heading("SALARIO", text="SALARIO", anchor=tk.W)
        self.tree_empleados.heading("OFICIO", text="OFICIO", anchor=tk.W)

        self.tree_empleados.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.title_lis_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_microfono.pack()
        self.tree_empleados.pack(fill="both", expand=True)
        self.boton_mod_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.crear_listado()
        self.deiconify()

    def recoger_datos(self):
        dato_cod_empleado = self.cod_empleado_var.get()
        dato_cod_departamento = self.cod_departamento_var.get()
        dato_dni = self.dni_var.get()
        dato_fecha_alta = self.fecha_alta_var.get()
        dato_telefono = self.telefono_var.get()
        dato_salario = self.salario_var.get()
        dato_oficio = self.oficio_var.get()
        return dato_cod_empleado , dato_cod_departamento, dato_dni, dato_fecha_alta, dato_telefono, dato_salario, dato_oficio

    def recoger_audio(self):
        tus_palabras = sr.Recognizer()
        with sr.Microphone() as source:
            audio = tus_palabras.listen(source)
        try:
            self.boton_microfono.configure(state="disabled")
            text = tus_palabras.recognize_google(audio, language="es-ES").upper()
            self.input_filtro.delete(0, tk.END)
            self.input_filtro.insert(tk.END, text)
            self.crear_listado()
        except sr.UnknownValueError:
            messagebox.showerror(message="NO SE PUDO RECONOCER TU VOZ")
        except sr.RequestError:
            messagebox.showerror(message="NO SE PUDO RECONOCER TU VOZ")
        finally:
            self.boton_microfono.configure(state="normal")

    def on_select(self, event):
        try:
            selected_item = self.tree_empleados.selection()[0]
            values = self.tree_empleados.item(selected_item)['values']
            self.cod_empleado_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_0])
            self.cod_departamento_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_1])
            self.dni_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_2])
            self.fecha_alta_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_3])
            self.telefono_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_4])
            self.salario_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_5])
            self.oficio_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_6])
        except IndexError:
            pass


    def crear_listado(self):
        self.tree_empleados.delete(*self.tree_empleados.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for empleado in self.almacen_empleados._empleados:
            if (busqueda in empleado._cod_empleado.upper()
                or busqueda in empleado._cod_departamento.upper() 
                or busqueda in empleado._dni.upper()
                or busqueda in empleado._fecha_alta.upper()
                or busqueda in empleado._telefono.upper()
                or busqueda in empleado._oficio.upper() or not busqueda):
                self.tree_empleados.insert("", tk.END, text=f"{contador}",
                                            values=(empleado._cod_empleado, empleado._cod_departamento, empleado._dni, 
                                            empleado._fecha_alta, empleado._telefono, empleado._salario, empleado._oficio))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_empleados.deiconify()

    def abrir_ventana_mod_empleados(self):
        dato_cod_empleado , dato_cod_departamento, dato_dni, dato_fecha_alta, dato_telefono, dato_salario, dato_oficio = self.recoger_datos()
        if (dato_cod_empleado == '' and dato_cod_departamento == '' 
        and dato_dni == '' and dato_fecha_alta == '' and dato_telefono == ''
        and dato_salario == '' and dato_oficio == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN EMPLEADO")
        else:
            self.withdraw()
            self.ventana_mod_empleados.mostrar_menu()
            self.ventana_mod_empleados.mainloop()
