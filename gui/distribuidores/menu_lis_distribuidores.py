import speech_recognition as sr
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class LisDistribuidores(tk.Toplevel):
    '''
    CONSIDERAMOS QUE NO ES NECESARIA UNA VENTANA DE MODIFICAR YA QUE SOLO CONTIENE
    UN NOMBRE Y UN CÓDIGO CON LO CUÁL, LA ÚNICA MODIFICACIÓN A REALIZAR ES UN BORRADO
    DEL DISTRIBUIDOR O UNA INSERCIÓN.
    '''
    def __init__(self, master, almacen_distribuidores, menu_distribuidores):
        super().__init__(master)
        self.almacen_distribuidores = almacen_distribuidores
        self.menu_distribuidores = menu_distribuidores
        self.IMAGEN_MICRO = os.path.abspath('../hmnlogistics/img/microfono.png') 

        self.cod_distribuidor_var = tk.StringVar()
        self.nombre_var = tk.StringVar()

        self.minsize(472, 350)
        self.geometry("472x350+650+150")
        self.maxsize(472, 350)

        self.withdraw()
        self.title("MIS DISTRIBUIDORES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.style = ttk.Style()
        self.style.configure('Config.TLabel', width=40)

        self.title_lis_distribuidores = ttk.Label(self, text="MIS DISTRIBUIDORES", font=("Helvetica", 12), style='Config.TLabel') 
        self.tree_distribuidores = ttk.Treeview(self, style='Config.TLabel') 
        self.print_filtro = ttk.Label(self, text="REALIZAR BUSQUEDA:", font=("Helvetica", 9), style='Config.TLabel')    
        self.input_filtro = ttk.Entry(self, style='Config.TLabel')
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio, style='Config.TLabel')
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        #TABLA
        self.tree_distribuidores["columns"] = ("COD_DISTRIBUIDOR", "NOMBRE")  
        
        self.tree_distribuidores.column("#0", width=100, stretch=tk.NO)
        self.tree_distribuidores.column("COD_DISTRIBUIDOR", anchor=tk.W, width=30)
        self.tree_distribuidores.column("NOMBRE", anchor=tk.W, width=50)
        
        self.tree_distribuidores.heading("#0", text="NUM_DISTRIBUIDORES", anchor=tk.W)
        self.tree_distribuidores.heading("COD_DISTRIBUIDOR", text="COD_DISTRIBUIDOR", anchor=tk.W,)
        self.tree_distribuidores.heading("NOMBRE", text="NOMBRE", anchor=tk.W)

    def mostrar_menu(self):
        self.title_lis_distribuidores.grid(row=0, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.print_filtro.grid(row=1, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
        self.input_filtro.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")
        self.boton_microfono.grid(row=2, column=8, padx=5, pady=5, sticky="nsew")
        self.tree_distribuidores.grid(row=3, column=0, rowspan=11, padx=5, pady=10, sticky="nsew")
        self.crear_listado()
        self.deiconify()
        self.input_filtro.focus_set()

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
        self.tree_distribuidores.delete(*self.tree_distribuidores.get_children())
        busqueda = self.input_filtro.get().upper()
        contador = 1
        for distribuidor in self.almacen_distribuidores._distribuidores:
            if (busqueda in distribuidor._cod_distribuidor.upper()
            or busqueda in distribuidor._nombre.upper() or not busqueda):
                self.tree_distribuidores.insert("", tk.END, text=f"{contador}",
                                            values=(distribuidor._cod_distribuidor, distribuidor._nombre))
                contador += 1

    def realizar_busqueda(self, event):
        self.crear_listado()

    def on_close(self):
        self.withdraw()
        self.menu_distribuidores.deiconify()
