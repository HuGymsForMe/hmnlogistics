import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = tree.selection()[0]
    # Obtener los valores de las columnas del objeto seleccionado
    values = tree.item(selected_item)['values']
    print("Objeto seleccionado:", values)

root = tk.Tk()

# Crear el TreeView
tree = ttk.Treeview(root)
tree.pack()

# Agregar columnas
tree['columns'] = ('Columna 1', 'Columna 2')

# Configurar encabezados de columna
tree.heading('#0', text='Objeto')
tree.heading('Columna 1', text='Valor 1')
tree.heading('Columna 2', text='Valor 2')

# Agregar objetos al TreeView
tree.insert('', 'end', text='Objeto 1', values=('Valor 1.1', 'Valor 1.2'))
tree.insert('', 'end', text='Objeto 2', values=('Valor 2.1', 'Valor 2.2'))

# Configurar evento de selección
tree.bind('<<TreeviewSelect>>', on_select)

root.mainloop()
