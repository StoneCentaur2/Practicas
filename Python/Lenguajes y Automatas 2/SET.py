#Ejemplo:
"""personas={"victor",
"Juan",
"Francisco"
}
personas.add("Paco")
personas.remove("Francisco")

print(type(personas))
print(personas)"""
#Ejercicio:
personas = {''}
listas = ""
while listas != "Parar":
    listas = input("Ingrese los nombres o 'Parar': ")
    personas.add(listas)
listas = input("Desea eliminar a alguien de la lista? (S/N): ")
if listas == "S":
    listas = input("Ingrese lo que quiere eliminar: ")
    personas.remove(listas)
#Eliminación de basura
personas.remove('')
personas.remove('Parar')
#impresión
print(type(personas))
print(personas)