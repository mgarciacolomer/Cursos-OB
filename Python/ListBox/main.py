import tkinter as tk

mainWindow = tk.Tk()

labelLista = tk.Label(mainWindow, text='Lista de la compra')
labelLista.pack()

listBoxCompra = tk.Listbox(mainWindow, selectmode=tk.EXTENDED, width=100)
listaCompra =['Leche', 'Galletas', 'Pan', 'Patatas', 'Jamón', 'Queso', 'Cerveza']

listBoxCompra.insert(0, *listaCompra)
listBoxCompra.pack()

mainWindow.mainloop()