import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

from gui.empleados.menu_mod_datos_empleados import ModDatosEmpleados

class LisDatosEmpleados(tk.Toplevel):
    def __init__(self, master, almacen_empleados, menu_empleados):
        super().__init__(master)
        self.almacen_empleados = almacen_empleados
        self.menu_empleados = menu_empleados
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png') 

        self.minsize(690, 400)
        self.geometry("695x400+650+150")
        self.maxsize(695, 400)

        self.withdraw()
        self.title("MIS EMPLEADOS")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.style = ttk.Style()
        self.style.configure('Config.TLabel', width=40)

        self.dni_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.apellidos_var = tk.StringVar()
        self.fecha_nac_var = tk.StringVar()
        self.domicilio_var = tk.StringVar()

        self.ventana_mod_empleados = ModDatosEmpleados(self.master, self.almacen_empleados, self.dni_var, self.nombre_var, 
        self.apellidos_var, self.fecha_nac_var, self.domicilio_var, self)

        self.title_lis_datos_empleados = ttk.Label(self, text="MIS EMPLEADOS", font=("Helvetica", 12), style='Config.TLabel') 
        self.tree_datos_empleados = ttk.Treeview(self, style='Config.TLabel')
        self.print_filtro = ttk.Label(self, text="REALIZAR BUSQUEDA:", font=("Helvetica", 9), style='Config.TLabel')    
        self.input_filtro = ttk.Entry(self, style='Config.TLabel')
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio, style='Config.TLabel')
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        self.boton_mod_empleados = ttk.Button(self, text="MODIFICAR EMPLEADO", command=self.abrir_ventana_mod_empleados)

        #TABLA
        self.tree_datos_empleados["columns"] = ("DNI", "NOMBRE", "APELLIDOS", "FECHA_NAC", "DOMICILIO")  
        
        self.tree_datos_empleados.column("#0", width=100, stretch=tk.NO)
        self.tree_datos_empleados.column("DNI", anchor=tk.W, width=60)
        self.tree_datos_empleados.column("NOMBRE", anchor=tk.W, width=60)
        self.tree_datos_empleados.column("APELLIDOS", anchor=tk.W, width=60)
        self.tree_datos_empleados.column("FECHA_NAC", anchor=tk.W, width=60)
        self.tree_datos_empleados.column("DOMICILIO", anchor=tk.W, width=60)
        
        self.tree_datos_empleados.heading("#0", text="NUM_EMPLEADO", anchor=tk.W)
        self.tree_datos_empleados.heading("DNI", text="DNI", anchor=tk.W)
        self.tree_datos_empleados.heading("NOMBRE", text="NOMBRE", anchor=tk.W,)
        self.tree_datos_empleados.heading("APELLIDOS", text="APELLIDOS", anchor=tk.W)
        self.tree_datos_empleados.heading("FECHA_NAC", text="FECHA_NAC", anchor=tk.W)
        self.tree_datos_empleados.heading("DOMICILIO", text="DOMICILIO", anchor=tk.W)

        self.tree_datos_empleados.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.title_lis_datos_empleados.grid(row=0, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.print_filtro.grid(row=1, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.input_filtro.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")
        self.boton_microfono.grid(row=2, column=8, padx=5, pady=5, sticky="nsew")
        self.tree_datos_empleados.grid(row=3, column=0, rowspan=11, padx=5, pady=10, sticky="nsew")
        self.boton_mod_empleados.grid(row=23, column=0, columnspan=20, padx=5, pady=5, sticky="nsew")
        self.crear_listado()
        self.deiconify()
        self.input_filtro.focus_set()


    def recoger_datos(self):
        dato_dni = self.dni_var.get()
        dato_nombre = self.nombre_var.get()
        dato_apellidos = self.apellidos_var.get()
        dato_fecha_nac = self.fecha_nac_var.get()
        dato_domicilio = self.domicilio_var.get()
        return dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio

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
            messagebox.showerror(message="SE HA PRODUCIDO UN ERROR")
        finally:
            self.boton_microfono.configure(state="normal")

    def on_select(self, event):
        try:
            selected_item = self.tree_datos_empleados.selection()[0]
            values = self.tree_datos_empleados.item(selected_item)['values']
            self.dni_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_0])
            self.nombre_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_1])
            self.apellidos_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_2])
            self.fecha_nac_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_3])
            self.domicilio_var.set(values[self.almacen_empleados.CamposFicheroCsv.CAMPO_4])
        except IndexError:
            pass


    def crear_listado(self):
        self.tree_datos_empleados.delete(*self.tree_datos_empleados.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for empleado in self.almacen_empleados._datos_empleados:
            if (busqueda in empleado._dni.upper()
                or busqueda in empleado._nombre.upper()
                or busqueda in empleado._apellidos.upper()
                or busqueda in empleado._fecha_nac.upper()
                or busqueda in empleado._domicilio.upper() or not busqueda):
                self.tree_datos_empleados.insert("", tk.END, text=f"{contador}",
                                            values=(empleado._dni, empleado._nombre, empleado._apellidos,
                                            empleado._fecha_nac, empleado._domicilio))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_empleados.deiconify()

    def abrir_ventana_mod_empleados(self):
        dato_dni, dato_nombre, dato_apellidos, dato_fecha_nac, dato_domicilio = self.recoger_datos()
        if (dato_dni == '' and dato_nombre == '' and dato_apellidos == '' and dato_fecha_nac == '' and dato_domicilio == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN EMPLEADO")
        else:
            self.withdraw()
            self.ventana_mod_empleados.mostrar_menu()
            self.ventana_mod_empleados.mainloop()