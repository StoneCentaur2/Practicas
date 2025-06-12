while True:
    try:
        nu = int(input("Ingresa un numero: "))
        break
    except ValueError:
        print("Solo numero entero")

if nu % 2 == 0:
    print("Numero Par")
else:
    print("Numero Impar")