from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk


def seleccionar(ev):
    global texto_seleccionado
    texto_seleccionado = ev.widget.get(ANCHOR)
    seleccion = int(comboprincipal.get())
    if seleccion == 0:
        texto_seleccionado = 'Elemento Seleccionado macth'

root = Tk()

comboprincipal = ttk.Combobox(root)
comboprincipal["values"]= ("match","search","findall","finditer")
comboprincipal.current()
comboprincipal.pack(expand=True, fill=BOTH)

texto_seleccionado = comboprincipal.current(), 'Ningún elemento Seleccionado'

comboprincipal.bind('<<ComboBoxSelect>>', seleccionar)

root.bind('<Return>', lambda ev:showinfo(title='Texto Seleccionado', message=texto_seleccionado))

root.mainloop()