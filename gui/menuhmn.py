import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk

import os

from gui.articulos.menu_articulos import MenuArticulos
from gui.clientes.menu_clientes import MenuClientes
from gui.sucursales.menu_sucursales import MenuSucursales
from gui.distribuidores.menu_distribuidores import MenuDistribuidor
from gui.pedidos.menu_pedidos import MenuPedido
from gui.departamentos.menu_departamentos import MenuDepartamentos
from gui.empleados.menu_empleados import MenuEmpleados

from almacen.almacen_articulos import AlmacenArticulos
from almacen.almacen_clientes import AlmacenClientes
from almacen.almacen_sucursales import AlmacenSucursales
from almacen.almacen_distribuidores import AlmacenDistribuidores
from almacen.almacen_pedidos import AlmacenPedidos
from almacen.almacen_departamentos import AlmacenDepartamentos
from almacen.almacen_empleados import AlmacenEmpleados

class MenuHmn:
    def __init__(self, master, app):
        self.master = master
        self._app = app

        self.almacen_articulos = AlmacenArticulos(self)
        self.almacen_clientes = AlmacenClientes(self)
        self.almacen_sucursales = AlmacenSucursales(self)
        self.almacen_distribuidores = AlmacenDistribuidores(self)
        self.almacen_pedidos = AlmacenPedidos(self)
        self.almacen_departamentos = AlmacenDepartamentos(self)
        self.almacen_empleados = AlmacenEmpleados(self)

        self.ventana_articulo = MenuArticulos(self.master, self._app, self.almacen_articulos, self.almacen_clientes)
        self.ventana_cliente = MenuClientes(self.master, self._app, self.almacen_clientes, self.almacen_sucursales, self.almacen_articulos)
        self.ventana_sucursal = MenuSucursales(self.master, self._app, self.almacen_sucursales, self.almacen_departamentos)
        self.ventana_distribuidor = MenuDistribuidor(self.master, self._app, self.almacen_distribuidores, self.almacen_pedidos)
        self.ventana_pedidos = MenuPedido(self.master, self._app, self.almacen_pedidos, self.almacen_distribuidores, self.almacen_sucursales)
        self.ventana_departamentos = MenuDepartamentos(self.master, self._app, self.almacen_departamentos, self.almacen_sucursales, self.almacen_empleados)
        self.ventana_empleados = MenuEmpleados(self.master, self._app, self.almacen_empleados, self.almacen_departamentos)
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.IMAGEN_FAVICON= Image.open(os.path.abspath('../hmnlogistics/img/carretilla.ico'))
        self.resized_favicon = self.IMAGEN_FAVICON.resize((32, 15))
        self.favicon_tk = ImageTk.PhotoImage(self.resized_favicon)
        self.master.iconphoto(True, self.favicon_tk)

        self.master.minsize(800, 600)
        self.master.geometry("800x600+550+100")
        self.master.maxsize(800, 600)
        self.master.deiconify()
        self.master.title("HMN LOGISTICS")

        self.IMAGEN_LOGO = Image.open(os.path.abspath('../hmnlogistics/img/hmnlogistics.jpeg'))
        self.resized_logo_hmn = self.IMAGEN_LOGO.resize((310, 150))
        self.logo_hmn = ImageTk.PhotoImage(self.resized_logo_hmn)
        self.logo_hmn_menu = ttk.Label(self.master, image=self.logo_hmn)

        self.title_hmn = tk.Label(self.master, text="BIENVENIDO", font=("Helvetica", 14))
        self.subtitulo_hmn = ttk.Label(self.master, text="¿QUÉ DESEA GESTIONAR?", font=("Helvetica", 12))
        self.boton_articulos = ttk.Button(self.master, text="ARTÍCULOS", command=self.acceder_menu_articulos)
        self.boton_clientes = ttk.Button(self.master, text="CLIENTES", command=self.acceder_menu_clientes)
        self.boton_sucursales = ttk.Button(self.master, text="SUCURSALES", command=self.acceder_menu_sucursales)
        self.boton_pedidos = ttk.Button(self.master, text="PEDIDOS", command=self.acceder_menu_pedidos)
        self.boton_distribuidores = ttk.Button(self.master, text="DISTRIBUIDORES", command=self.acceder_menu_distribuidores)
        self.boton_departamentos = ttk.Button(self.master, text="DEPARTAMENTOS", command=self.acceder_menu_departamentos)
        self.boton_empleados = ttk.Button(self.master, text="EMPLEADOS", command=self.acceder_menu_empleados)
        self.guardar_datos = ttk.Button(self.master, text="GUARDAR", command=self.clickar_boton_guardar)
        self.guardar_salir = ttk.Button(self.master, text="GUARDAR Y SALIR", command=self.clickar_boton_guardar_salir)

    def main(self):
        self.logo_hmn_menu.pack(side=LEFT, anchor="w", expand=False, padx=40)
        self.subtitulo_hmn.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
        self.boton_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_clientes.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_sucursales.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_distribuidores.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_departamentos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_empleados.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.guardar_datos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.guardar_salir.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

    def ocultar_menu(self):
        self.master.withdraw()
    
    def acceder_menu_articulos(self):
        self.ocultar_menu()
        self.ventana_articulo.mostrar_menu()
    
    def acceder_menu_clientes(self):
        self.ocultar_menu()
        self.ventana_cliente.mostrar_menu()
    
    def acceder_menu_sucursales(self):
        self.ocultar_menu()
        self.ventana_sucursal.mostrar_menu()

    def acceder_menu_distribuidores(self):
        self.ocultar_menu()
        self.ventana_distribuidor.mostrar_menu()

    def acceder_menu_pedidos(self):
        self.ocultar_menu()
        self.ventana_pedidos.mostrar_menu()

    def acceder_menu_departamentos(self):
        self.ocultar_menu()
        self.ventana_departamentos.mostrar_menu()

    def acceder_menu_empleados(self):
        self.ocultar_menu()
        self.ventana_empleados.mostrar_menu()

    def on_close(self):
        self.master.destroy()

    def clickar_boton_guardar(self):
        alerta = messagebox.askyesno(message="DESEAN GUARDAR LOS CAMBIOS")
        if alerta:
            self.recoger_datos()

    def clickar_boton_guardar_salir(self):
        alerta = messagebox.askyesno(message="DESEA GUARDAR LOS CAMBIOS Y SALIR")
        if alerta:
            self.recoger_datos()
            self.master.destroy()

    def recoger_datos(self):
        self.ventana_sucursal.almacen_sucursales.sobreescribir_datos()
        self.ventana_cliente.almacen_clientes.sobreescribir_datos()
        self.ventana_articulo.almacen_articulos.sobreescribir_datos()
        self.ventana_distribuidor.almacen_distribuidores.sobreescribir_datos()
        self.ventana_pedidos.almacen_pedidos.sobreescribir_datos()
        self.ventana_departamentos.almacen_departamentos.sobreescribir_datos()
        self.ventana_empleados.almacen_empleados.sobreescribir_datos()