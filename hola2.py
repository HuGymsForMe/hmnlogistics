class LisArticulos(tk.Toplevel):
    def __init__(self, master, almacen_articulos, menu_articulos):
        super().__init__(master)
        self.almacen_articulos = almacen_articulos
        self.menu_articulos = menu_articulos

        # Resto del código...

        self.title_lis_sucursales.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.input_filtro.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.tree_articulos.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.crear_listado()

        self.print_cod_cliente.grid(row=3, column=0, padx=10, pady=5)
        self.input_cod_cliente.grid(row=3, column=1, padx=10, pady=5)
        self.print_nombre.grid(row=4, column=0, padx=10, pady=5)
        self.input_nombre.grid(row=4, column=1, padx=10, pady=5)
        self.print_descripcion.grid(row=5, column=0, padx=10, pady=5)
        self.input_descripcion.grid(row=5, column=1, padx=10, pady=5)
        self.print_categoria.grid(row=6, column=0, padx=10, pady=5)
        self.input_categoria.grid(row=6, column=1, padx=10, pady=5)

        self.deiconify()

LisArticulos()