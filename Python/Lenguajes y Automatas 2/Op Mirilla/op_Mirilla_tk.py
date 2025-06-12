import tkinter as tk #Librería para interfaz grafica
from tkinter import *
from tkinter import messagebox #importando los mensajes
from io import open #liberias para usar el sistema
import pathlib # para buscar los directorios
"""¿Qué es la optimización de mirilla?
La optimización de mirilla trata de estructurar
de manera eficiente el flujo del programa,
sobre todo en instrucciones de bifurcación
como son las decisiones, ciclos y saltos de
rutinas.
¿Donde se aplica? 
En instrucciones de bifurcación
como son las decisiones, ciclos y saltos de
rutinas, la idea es tener los saltos lo más cerca de
las llamadas, siendo el salto lo más pequeño
posible.
¿Usualmente se aplica en?
En los switch, if, while, for, todo aquel que ocupe 
realizar un break de forma más rápida para poder 
realizar una optimización."""
class VentanaP(tk.Frame):
    def __init__(self,master=None): # Es lo que devolverá cuando se use la clase
        super().__init__(master)
        self.master = master
        self.pack()
        self.inicializar_gui()

    def inicializar_gui(self): # Lo que contendrá el gui, osea, botones, labels, textbox y demás
        self.Lbl_name = tk.Label(self,text='Nombre: ')
        self.Lbl_name.grid(row=0,column=0)

        self.txb_name = tk.Entry(self, width=20)
        self.txb_name.grid(row=0,column=1)

        self.btn_name = tk.Button(self, text='Guardar')
        self.btn_name['command']= self.save
        self.btn_name.grid(row=0,column=2)
        
        self.btn_view = tk.Button(self,text='Ver guardados', command=self.view).grid(row=0,column=3) #Segunda forma de acomdar el uso del comando y la ubicación

        self.lbl_contenido = tk.Label(self,text="Archivos guardados").grid(row=1,column=3)

    def save(self): # Para guardar el contendio en un txt
        name = self.txb_name.get().strip()

        if len(name):
            messagebox.showinfo("Guardado", f"Se guardo los datos de {name}")
            ruta = str(pathlib.Path().absolute())+"/Op Mirilla/Nombres.txt "
            archivo = open(ruta, "a+")
            archivo.write(name +"\n")
            archivo.close()
        else:
            messagebox.showerror("Error", "Necesita ingresa un nombre")
    
    def view(self): # Para mirar el archivo
        contenido = self.lbl_contenido
        ruta = str(pathlib.Path().absolute())+"/Op Mirilla/Nombres.txt "
        archivo = open(ruta, "r")
        lista = archivo.readlines()
        archivo.close()
        for elemento in lista:
            contenido
            messagebox.showinfo("Contenido",f"{+lista.index(elemento)+0}. {elemento}")

def main():
    app = tk.Tk()
    app.title("Ventana principal")
    app.geometry("400x200") # Tamaño de la gui
    Ventana = VentanaP(app) # Inicia todo lo que contiene la gui
    Ventana.mainloop() # mantiene la gui inciada en un loop para que no se cierre

if __name__ == '__main__': # Para que sea lo primero en inciar 
    main()
    