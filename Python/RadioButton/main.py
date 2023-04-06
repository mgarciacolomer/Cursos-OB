import tkinter as tk

def selectOption():
    labelOpcion.config(text=f'La opción seleccionada es la número: {opcion.get()}')
def resetButton():
    opcion.set(None)
    labelOpcion.config(text='Ninguna opción seleccionada')

window = tk.Tk()

opcion = tk.StringVar()
opcion.set(None)

radioButton1 = tk.Radiobutton(window, text='Primera Opción', value=1, height=2, width=100, variable=opcion, command=selectOption)
radioButton1.pack()
radioButton2 = tk.Radiobutton(window, text='Segunda Opción', value=2, height=2, width=100, variable=opcion, command=selectOption)
radioButton2.pack()
radioButton3 = tk.Radiobutton(window, text='Tercera Opción', value=3, height=2, width=100, variable=opcion, command=selectOption)
radioButton3.pack()

labelOpcion = tk.Label(window, text='Ninguna opción seleccionada')
labelOpcion.pack()

botonReinicio = tk.Button(window, text='Reinicio', command=resetButton)
botonReinicio.pack()

window.mainloop()