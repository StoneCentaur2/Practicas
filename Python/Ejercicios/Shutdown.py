from lib2to3.pgen2.token import NEWLINE
import os
while True:
    try:
        decision = int(input("Ingrese 1 para apagar equipo \nIngrese 2 para salir: "))
        break
    except ValueError:
            print("Solo números.")
#Desición de la opción para apagar
if (decision == 1):
        os.system("shutdown /s /t 1")
elif(decision == 2):
        print("Usted esta saliendo...")
else:
        print("ingreso la opción mal.")