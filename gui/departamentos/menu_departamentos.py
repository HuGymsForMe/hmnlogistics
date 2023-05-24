import tkinter as tk
from tkinter import *
from tkinter import ttk

from almacen.almacen_departamentos import AlmacenDepartamentos

class MenuDepartamentos(tk.Toplevel):
    def __init__(self, master, app):
        super().__init__(master, app)
        self._app = app
        self.almacen_departamentos = AlmacenDepartamentos(self)

        self.withdraw()