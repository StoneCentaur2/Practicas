contactos = [{
    "nombre":"Antonio",
    "edad":"21",
    "telefono":"63811648"
},
{
    "nombre":"Martin",
    "edad":"17",
    "telefono":"638915184"
}]
#cambio de dato
listas = ''
while listas != "Parar":
    nombre = input("Ingresar el nombre a capturar: ")
    edad = input("Ingresar la edad a capturar: ")
    telefono = input("Ingresar el telefono a capturar: ")
    listas = input("Desea ingresar más (sí / Parar): ")
    contactos.append({"nombre":nombre,"edad":edad,"telefono":telefono})

#Impresión de nombre
print("\n Lista de contactos")
print(contactos)
#que pida nombre, edad y numero de telefono