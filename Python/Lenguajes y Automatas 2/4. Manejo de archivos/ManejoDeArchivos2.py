from io import open #Libreria para hace uso del sisteme Input y Output
import pathlib #Libreria para el uso de archivos
# todo esto se necesita convertir en string
# el metodo path para la busqueda del archivo, el absolute busca el arhivo y el directorio del archivo
ruta = str(pathlib.Path().absolute())+"/4. Manejo de archivos/documento.txt "
print(ruta)
# una variable para la apertura dl archivo con su ruta y la "r" para leer "a+" para abrir
archivo = open(ruta, "r")
# variable para usarla en lista y usando el metodo .readlines() para leer el contenido del archivo
lista = archivo.readlines()
archivo.close()
# Uso del for para imprimir el contenido del archivo
for elemento in lista:
    print("- "+elemento.upper()) #imprime el contenido en Mayúscula (el metodo lower es para hacerlas minusculas)