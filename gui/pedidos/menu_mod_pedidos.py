import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class ModPedidos(tk.Toplevel):
    def __init__(self, master, almacen_pedidos, almacen_distribuidores, almacen_sucursales, cod_pedido_var, cod_distribuidor_var,
                cod_sucursal_var, fecha_pedido_var, cantidad_articulos_var, peso_var, precio_var, menu_lis_pedidos):
        super().__init__(master)
        self.almacen_pedidos = almacen_pedidos
        self.almacen_distribuidores = almacen_distribuidores
        self.almacen_sucursales = almacen_sucursales
        self.cod_pedido_var = cod_pedido_var
        self.cod_distribuidor_var = cod_distribuidor_var
        self.cod_sucursal_var = cod_sucursal_var
        self.fecha_pedido_var = fecha_pedido_var
        self.cantidad_articulos_var = cantidad_articulos_var
        self.peso_var = peso_var
        self.precio_var = precio_var
        self.menu_lis_pedidos = menu_lis_pedidos

        self.withdraw()
        self.minsize(400, 450)
        self.geometry("400x450+650+100")
        self.maxsize(400, 450)
        self.title("MODIFICAR PEDIDO")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.print_cod_pedido = ttk.Label(self, text="CÓDIGO DE PEDIDO:", font=("Helvetica", 9))
        self.input_cod_pedido = ttk.Entry(self, textvariable=self.cod_pedido_var, state='readonly')
        self.print_cod_distribuidor = ttk.Label(self, text="CÓDIGO DE DISTRIBUIDOR:", font=("Helvetica", 9))
        self.eleccion_cod_distribuidor = ttk.Combobox(self, values=[], textvariable=self.cod_distribuidor_var)
        self.print_cod_sucursal = ttk.Label(self, text="CÓDIGO DE DISTRIBUIDOR:", font=("Helvetica", 9))
        self.eleccion_cod_sucursal = ttk.Combobox(self, values=[], textvariable=self.cod_sucursal_var)
        self.print_fecha_pedido = ttk.Label(self, text="FECHA DE PEDIDO:", font=("Helvetica", 9))
        self.input_fecha_pedido = ttk.Entry(self, textvariable=self.fecha_pedido_var)
        self.print_cantidad_articulos = ttk.Label(self, text="CANTIDAD DE ARTÍCULOS:", font=("Helvetica", 9))
        self.input_cantidad_articulos = ttk.Entry(self, textvariable=self.cantidad_articulos_var)
        self.print_peso = ttk.Label(self, text="PESO(kg):", font=("Helvetica", 9))
        self.input_peso = ttk.Entry(self, textvariable=self.peso_var)
        self.print_precio = ttk.Label(self, text="PRECIO(€):", font=("Helvetica", 9))
        self.input_precio = ttk.Label(self, textvariable=self.precio_var)
        self.boton_mod_pedidos = ttk.Button(self, text="REALIZAR CAMBIOS", command=self.realizar_modificaciones)

    def mostrar_menu(self):
        self.actualizar_posibles_combobox()
        self.print_cod_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cod_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_distribuidor.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.eleccion_cod_sucursal.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_fecha_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_fecha_pedido.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_cantidad_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_cantidad_articulos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_peso.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_peso.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.print_precio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.input_precio.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.boton_mod_pedidos.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.deiconify()

    def actualizar_posibles_combobox(self):
        self.posibles_cod_distribuidor = self.almacen_distribuidores.generar_combobox()
        self.eleccion_cod_distribuidor['values'] = self.posibles_cod_distribuidor
        self.posibles_cod_sucursal = self.almacen_sucursales.generar_combobox()
        self.eleccion_cod_sucursal['values'] = self.posibles_cod_sucursal

    def realizar_modificaciones(self):
        try:
            dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal, dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio = self.almacen_pedidos.recoger_datos()
            if (dato_cod_distribuidor in self.posibles_cod_distribuidor
                and dato_cod_sucursal in self.posibles_cod_sucursal
                and self.validador.validador_fecha(dato_fecha_pedido)):
                    self.almacen_pedidos.del_datos(dato_cod_pedido)
                    self.almacen_pedidos.add_datos(dato_cod_pedido, dato_cod_distribuidor, dato_cod_sucursal,
                    dato_fecha_pedido, dato_num_articulos, dato_peso, dato_precio)
                    messagebox.showinfo(message="EL PEDIDO SE MODIFICÓ CORRECTAMENTE")
                    self.on_close()
            else:
                datos_erroneos = messagebox.showerror(message="DATOS INCORRRECTOS")
        except ValueError:
            datos_erroneos

    def on_close(self):
        self.withdraw()
        self.menu_lis_pedidos.deiconify()