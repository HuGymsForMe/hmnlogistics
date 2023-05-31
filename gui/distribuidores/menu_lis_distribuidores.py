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

        self.minsize(500, 300)
        self.geometry("500x300+650+150")
        self.maxsize(500, 300)

        self.withdraw()
        self.title("MIS DISTRIBUIDORES")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.foto_micro = tk.PhotoImage(file=self.IMAGEN_MICRO)

        self.title_lis_distribuidores = ttk.Label(self, text="MIS DISTRIBUIDORES", font=("Helvetica", 12)) 
        self.tree_distribuidores = ttk.Treeview(self)    
        self.input_filtro = ttk.Entry(self)
        self.boton_microfono = ttk.Button(self, image=self.foto_micro, command=self.recoger_audio)
        self.input_filtro.bind('<KeyRelease>', self.realizar_busqueda)

        #TABLA
        self.tree_distribuidores["columns"] = ("COD_DISTRIBUIDOR", "NOMBRE")  
        
        self.tree_distribuidores.column("#0", width=100, stretch=tk.NO)
        self.tree_distribuidores.column("COD_DISTRIBUIDOR", anchor=tk.W, width=60)
        self.tree_distribuidores.column("NOMBRE", anchor=tk.W, width=100)
        
        self.tree_distribuidores.heading("#0", text="NUM_DISTRIBUIDORES", anchor=tk.W)
        self.tree_distribuidores.heading("COD_DISTRIBUIDOR", text="COD_DISTRIBUIDOR", anchor=tk.W,)
        self.tree_distribuidores.heading("NOMBRE", text="NOMBRE", anchor=tk.W)

    def mostrar_menu(self):
        self.title_lis_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_filtro.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_microfono.pack()
        self.tree_distribuidores.pack(fill="both", expand=True)
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
