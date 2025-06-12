from io import open #Libreria para hace uso del sisteme Input y Output
import pathlib #

ruta = str(pathlib.Path().absolute())+"/4. Manejo de archivos/documento.txt "
print(ruta)
archivo = open(ruta, "a+")
archivo.write("Agregamos datos desde python \n")
archivo.close()