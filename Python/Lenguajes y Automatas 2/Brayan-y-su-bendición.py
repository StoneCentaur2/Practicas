n = int(input("Ingrese el año de nacimiento de la bendición: "))
ed = 2017 - n
if n >= 1900 and n <= 2017:
    {
        print("La edad de su bendición es de: " f"{ed}")
    }
#Bebé
    if ed>=0 and ed <= 5:
        print("Su bendición es un bebé")
#Bebé de meses
    if ed == 0:
        print("Todavía tiene meses")
#niño
    if ed>=5 and ed <= 11:
        print("Su bendición es un niño")
#adolecente
    if ed>=12 and ed <= 18:
        print("Su bendición es un adolecente")
#adulto
    if ed>=18 and ed <= 59:
        print("Su bendición es un adulto")
#3era edad
    if ed>=60 and ed <= 117:
        print("Su bendición es un adulto de la 3ra edad")
#Por si se quieren pasar de listos    
if n > 2017:
    {
    print("Su bendición todavía no nace.")
    }
#Por si tiene más de 118 años    
if n < 1900:
    {
    print("Su bendición debe estar muerta... porque su edad es de: " f"{ed}")
    }