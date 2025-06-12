# Tabla de multiplicación con input
def main():
    n = int(input("Ingrese un número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

if __name__ == "__main__":
    main()
