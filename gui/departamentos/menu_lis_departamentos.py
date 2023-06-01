import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from gui.departamentos.menu_mod_departamentos import ModDepartamentos

class LisDepartamentos(tk.Toplevel):
    def __init__(self, master, almacen_departamentos, almacen_sucursales, menu_departamentos):
        super().__init__(master)
        self.almacen_departamentos = almacen_departamentos
        self.almacen_sucursales = almacen_sucursales
        self.menu_departamentos = menu_departamentos
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png') 

        self.minsize(700, 375)
        self.geometry("700x375+400+150")
        self.maxsize(900, 375)

        self.cod_departamento_var = tk.StringVar()
        self.cod_sucursal_var = tk.StringVar()
        self.nombre_var = tk.StringVar()

        self.ventana_mod_departamentos = ModDepartamentos(self.master, self.almacen_departamentos,
        self.almacen_sucursales, self.cod_departamento_var, self.cod_sucursal_var, self.nombre_var, self)

        self.withdraw()
        self.title("MIS DEPARTAMENTOS")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.title_lis_departamentos = ttk.Label(self, text="MIS DEPARTAMENTOS", font=("Helvetica", 12)) 
        self.tree_departamentos = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)
        self.boton_mod_departamentos = ttk.Button(self, text="MODIFICAR DEPARTAMENTO", command=self.abrir_ventana_mod_departamentos)

        #TABLA
        self.tree_departamentos["columns"] = ("COD_DEPARTAMENTO", "COD_SUCURSAL", "NOMBRE")  
        
        self.tree_departamentos.column("#0", width=100, stretch=tk.NO)
        self.tree_departamentos.column("COD_DEPARTAMENTO", anchor=tk.W, width=50)
        self.tree_departamentos.column("COD_SUCURSAL", anchor=tk.W, width=60)
        self.tree_departamentos.column("NOMBRE", anchor=tk.W, width=100)
        
        self.tree_departamentos.heading("#0", text="NUM_DEPARTAMENTO", anchor=tk.W)
        self.tree_departamentos.heading("COD_DEPARTAMENTO", text="COD_DEPARTAMENTO", anchor=tk.W)
        self.tree_departamentos.heading("COD_SUCURSAL", text="COD_SUCURSAL", anchor=tk.W,)
        self.tree_departamentos.heading("NOMBRE", text="NOMBRE", anchor=tk.W)

        self.tree_departamentos.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.title_lis_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_microfono.pack()
        self.tree_departamentos.pack(fill="both", expand=True)
        self.boton_mod_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.crear_listado()
        self.deiconify()

    def crear_listado(self):
        self.tree_departamentos.delete(*self.tree_departamentos.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for departamento in self.almacen_departamentos._departamentos:
            if (busqueda in departamento._cod_departamento.upper()
            or busqueda in departamento._cod_sucursal.upper()
            or busqueda in departamento._nombre.upper() or not busqueda):
                self.tree_departamentos.insert("", tk.END, text=f"{contador}",
                                            values=(departamento._cod_departamento, departamento._cod_sucursal, departamento._nombre))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_departamentos.deiconify()

    def recoger_datos(self):
        dato_cod_departamento = self.cod_departamento_var.get()
        dato_cod_sucursal = self.cod_sucursal_var.get()
        dato_nombre = self.nombre_var.get().upper()
        return dato_cod_departamento, dato_cod_sucursal, dato_nombre

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
            selected_item = self.tree_departamentos.selection()[0]
            values = self.tree_departamentos.item(selected_item)['values']
            self.cod_departamento_var.set(values[self.almacen_departamentos.CamposFicheroCsv.COD_DEPARTAMENTO])
            self.cod_sucursal_var.set(values[self.almacen_departamentos.CamposFicheroCsv.COD_SUCURSAL])
            self.nombre_var.set(values[self.almacen_departamentos.CamposFicheroCsv.NOMBRE])
        except IndexError:
            pass
        
    def abrir_ventana_mod_departamentos(self):
        dato_cod_departamento, dato_cod_sucursal, dato_nombre = self.recoger_datos()
        if (dato_cod_departamento == '' and dato_cod_sucursal == '' and dato_nombre == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN DEPARTAMENTO")
        else:
            self.withdraw()
            self.ventana_mod_departamentos.mostrar_menu()
            self.ventana_mod_departamentos.mainloop()
    