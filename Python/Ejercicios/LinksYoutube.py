from tkinter import *
from pytube import YouTube 
"""
crear instalador sin que detecete el antivirus (NORTION NO funciona)
pyinstaller --windowed --icon=bts.ico LinksYoutube.py
"""
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title('Tu propio descargador de YouTube')
root.configure(bg='#AACDE2')

Label(root, text='Descarga tus videos',
      font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)

link = StringVar()

Label(root, text='Link de tu video',
      font='arial 15 bold', bg='#AACDE2').place(x=90, y=80)

link_enter = Entry(root, width=70, 
                   textvariable=link).place(x=32,y=120)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, 
          text='Descargado', 
          font='arial 13 bold', bg='#AACDE2', fg='#B57199').place(x=180, y=240)
    
Button(root, 
       text='Descargar', 
       font='arial 13 bold italic', 
       bg='#B57199', padx=2, 
       command=Downloader).place(x=180, y=180)

root.mainloop()