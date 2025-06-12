# Ejercicio con ciclos de una pramide

def main():
    # n = int(input("Ingrese la altura de la piramide: "))
    for i in range(0,7):
        for j in range(7-i):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()