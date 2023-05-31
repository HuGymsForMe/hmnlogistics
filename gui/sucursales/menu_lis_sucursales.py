import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

class LisSucursales(tk.Toplevel):
    def __init__(self, master, almacen_sucursales, menu_sucursales):
        super().__init__(master)
        self.almacen_sucursales = almacen_sucursales
        self.menu_sucursales = menu_sucursales
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png')

        self.minsize(700, 300)
        self.geometry("700x300+400+150")
        self.maxsize(850, 300)

        self.withdraw()
        self.title("MIS SUCURSALES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.title_lis_sucursales = ttk.Label(self, text="MIS SUCURSALES", font=("Helvetica", 12)) 
        self.tree_sucursales = ttk.Treeview(self)
        self.input_filtro = ttk.Entry(self)
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)
        self.tree_sucursales["columns"] = ("COD_SUCURSAL", "PROVINCIA", "DIRECCION")   
        
        self.tree_sucursales.column("#0", width=100, stretch=tk.NO)  # Columna de índice
        self.tree_sucursales.column("COD_SUCURSAL", anchor=tk.W, width=50)
        self.tree_sucursales.column("PROVINCIA", anchor=tk.W, width=60)
        self.tree_sucursales.column("DIRECCION", anchor=tk.W, width=100)
        
        self.tree_sucursales.heading("#0", text="NUM_SUCURSAL", anchor=tk.W)
        self.tree_sucursales.heading("COD_SUCURSAL", text="COD_SUCURSAL", anchor=tk.W)
        self.tree_sucursales.heading("PROVINCIA", text="PROVINCIA", anchor=tk.W)
        self.tree_sucursales.heading("DIRECCION", text="DIRECCION", anchor=tk.W)

    def mostrar_menu(self):
        self.title_lis_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_microfono.pack()
        self.tree_sucursales.pack(fill="both", expand=True)
        self.crear_listado()
        self.deiconify()

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

    def crear_listado(self):
        self.tree_sucursales.delete(*self.tree_sucursales.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for sucursal in self.almacen_sucursales._sucursales:
            if (busqueda in sucursal._cod_sucursal.upper()
            or busqueda in sucursal._provincia.upper()
            or busqueda in sucursal._direccion.upper() or not busqueda):
                self.tree_sucursales.insert("", tk.END, text=f"{contador}",
                                            values=(sucursal._cod_sucursal, sucursal._provincia, sucursal._direccion))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_sucursales.deiconify()
        


        

