import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from gui.clientes.menu_mod_clientes import ModClientes

class LisClientes(tk.Toplevel):
    def __init__(self, master, almacen_clientes, almacen_sucursales, menu_clientes):
        super().__init__(master)
        self.almacen_clientes = almacen_clientes
        self.almacen_sucursales = almacen_sucursales
        self.menu_clientes = menu_clientes
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png') 

        self.minsize(606, 360)
        self.geometry("606x360+400+150")
        self.maxsize(606, 360)

        self.cod_cliente_var = tk.StringVar()
        self.cod_sucursal_var = tk.StringVar()
        self.nombre_var = tk.StringVar()

        self.ventana_mod_clientes = ModClientes(self.master, self.almacen_clientes, 
        self.almacen_sucursales, self.cod_cliente_var, self.cod_sucursal_var, self.nombre_var, self)

        self.withdraw()
        self.title("MIS CLIENTES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.style = ttk.Style()
        self.style.configure('Config.TLabel', width=60)

        self.title_lis_clientes = ttk.Label(self, text="MIS CLIENTES", font=("Helvetica", 12), style='Config.TLabel') 
        self.tree_clientes = ttk.Treeview(self, style='Config.TLabel') 
        self.print_filtro = ttk.Label(self, text="REALIZAR BUSQUEDA:", font=("Helvetica", 9), style='Config.TLabel')    
        self.input_filtro = ttk.Entry(self, style='Config.TLabel')
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio, style='Config.TLabel')
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)
        self.boton_mod_clientes = ttk.Button(self, text="MODIFICAR CLIENTE", command=self.abrir_ventana_mod_clientes)

        #TABLA
        self.tree_clientes["columns"] = ("COD_CLIENTE", "COD_SUCURSAL", "NOMBRE")  
        
        self.tree_clientes.column("#0", width=100, stretch=tk.NO)
        self.tree_clientes.column("COD_CLIENTE", anchor=tk.W, width=50)
        self.tree_clientes.column("COD_SUCURSAL", anchor=tk.W, width=60)
        self.tree_clientes.column("NOMBRE", anchor=tk.W, width=100)
        
        self.tree_clientes.heading("#0", text="NUM_CLIENTE", anchor=tk.W)
        self.tree_clientes.heading("COD_CLIENTE", text="COD_CLIENTE", anchor=tk.W)
        self.tree_clientes.heading("COD_SUCURSAL", text="COD_SUCURSAL", anchor=tk.W,)
        self.tree_clientes.heading("NOMBRE", text="NOMBRE", anchor=tk.W)

        self.tree_clientes.bind('<<TreeviewSelect>>', self.on_select)

    def mostrar_menu(self):
        self.title_lis_clientes.grid(row=0, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.print_filtro.grid(row=1, column=0, columnspan=20, padx=5, pady=5, sticky="nsew")
        self.input_filtro.grid(row=2, column=0, columnspan=18, padx=5, pady=5, sticky="nsew")
        self.boton_microfono.grid(row=2, column=18, padx=5, pady=5, sticky="nsew")
        self.tree_clientes.grid(row=3, column=0, rowspan=21, padx=5, pady=10, sticky="nsew")
        self.boton_mod_clientes.grid(row=23, column=0, columnspan=20, padx=5, pady=10, sticky="nsew")
        self.crear_listado()
        self.deiconify()
        self.input_filtro.focus_set()

    def crear_listado(self):
        self.tree_clientes.delete(*self.tree_clientes.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for cliente in self.almacen_clientes._clientes:
            if (busqueda in cliente._cod_cliente.upper()
            or busqueda in cliente._cod_sucursal.upper()
            or busqueda in cliente._nombre.upper() or not busqueda):
                self.tree_clientes.insert("", tk.END, text=f"{contador}",
                                            values=(cliente._cod_cliente, cliente._cod_sucursal, cliente._nombre))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_clientes.deiconify()

    def recoger_datos(self):
        dato_cod_cliente = self.cod_cliente_var.get()
        dato_cod_sucursal = self.cod_sucursal_var.get()
        dato_nombre = self.nombre_var.get().upper()
        return dato_cod_cliente, dato_cod_sucursal, dato_nombre

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
            selected_item = self.tree_clientes.selection()[0]
            values = self.tree_clientes.item(selected_item)['values']
            self.cod_cliente_var.set(values[self.almacen_clientes.CamposFicheroCsv.COD_CLIENTE])
            self.cod_sucursal_var.set(values[self.almacen_clientes.CamposFicheroCsv.COD_SUCURSAL])
            self.nombre_var.set(values[self.almacen_clientes.CamposFicheroCsv.NOMBRE])
        except IndexError:
            pass

    def ocultar_menu(self):
        self.withdraw()
        
    def abrir_ventana_mod_clientes(self):
        dato_cod_cliente, dato_cod_sucursal, dato_nombre = self.recoger_datos()
        if (dato_cod_cliente == '' and dato_cod_sucursal == '' and dato_nombre == ''):
            adevertencia = messagebox.showwarning(message="DEBES SELECCIONAR UN CLIENTE")
        else:
            self.ocultar_menu()
            self.ventana_mod_clientes.mostrar_menu()
            self.ventana_mod_clientes.mainloop()