lista = []
listas = ""
while listas != "Parar":
    listas = input("numero: ")
    lista.append(listas)

for i in range(len(lista)-2,-1,-1):
    print(lista[i])