from io import open #Libreria para hace uso del sisteme Input y Output
import pathlib #Libreria para el uso de archivos
# todo esto se necesita convertir en string
# el metodo path para la busqueda del archivo, el absolute busca el arhivo y el directorio del archivo
ruta = str(pathlib.Path().absolute())+"/4. Manejo de archivos/Contenido while.txt "
print(ruta)
archivo = open(ruta, "a+")
contenido = [{
    "numero 1":"1",
    "numero 2":"2",
    "Resultado":"2"}]
lista = ""
while lista != "S":
    num1 = input("Agregue su 1er numero: ")
    num2 = input("Agregue su 2do numero: ")
    res = int(num1) * int(num2)
    lista = input("¿Desea detener (S/N)?: ")
    contenido.append({"numero 1":num1,"numero 2":num2,"Resultado":res})
    archivo.write(str(contenido) + "\n")
# una variable para la apertura dl archivo con su ruta y la "r" para leer "a+" para abrir
archivo = open(ruta, "r")
# variable para usarla en lista y usando el metodo .readlines() para leer el contenido del archivo
lista = archivo.readlines()
archivo.close()
# Uso del for para imprimir el contenido del archivo
for elemento in lista:
    print("- "+elemento) #imprime el contenido en Mayúscula (el metodo lower es para hacerlas minusculas)