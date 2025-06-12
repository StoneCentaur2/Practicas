nm = input("Ingrese el nombre a imprimir: ")

while True:
    try:
        nu = int(input("Ingrese el numero de repeticiones: "))
        break
    except ValueError:
        print("Solo se admiten numeros enteros")
x = 0
while x < nu:
     print(nm)
     x = x+1