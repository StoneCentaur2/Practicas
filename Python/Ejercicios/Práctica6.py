while True:
    try:
        ed = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Dato Invalido")
if ed < 4:
    print("Edad : "+str(ed))
    print("Su entrada es gratis" )
if ed >= 4 and ed <=18:
    print("Edad : "+str(ed))
    print("Su costo de entrada es de: $50 Rupias" )
if ed > 18:
    print("Edad : "+str(ed))
    print("Su costo de entrada es de: $100 Rupias" )