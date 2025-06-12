import random
num1 = int(input("Ingrese su numero: "))
while(True):
    num = random.randint(0,6)
    if num1 != num:
        print("Su numero ganador fue:", num,"perdiste")
    else:
        print("Su numero ganador fue:", num,"ganaste")
        break