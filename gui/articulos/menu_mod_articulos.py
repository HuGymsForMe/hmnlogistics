import tkinter as tk
from tkinter import *
from tkinter import ttk

class ModArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.menu_articulos = menu_articulos