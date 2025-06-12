#estructura de un metodo
#def NombreDelMetodo():
def MuestroNombres():
    print("José María")
    print("José María 2")
    print("José María 3")
    print("José María 4")
    print("José María 5")

#invocar función
#MuestroNombres()
#Funciones con parametros
#nom = input("Ingrese su nombre: ")
#ed = int(input("Ingrese su edad: "))
def NombreDeMetodo(nombre,edad):
    print(nombre)
    print(edad)
    if(edad >= 18):
        print("mayor de edad")
    else:
        print("Menor de edad")

#NombreDeMetodo(nom,ed)

def getEmpleado(Nombre,ine=None):
    print("Datos del empleado")
    print(Nombre)
    print(ine)

#getEmpleado("Jose")
#getEmpleado("Jose","IDOIJ5151DSA2")

def Calculadora(num1,num2,basicos=False):
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    divi=num1/num2
    
    cadena=""
    cadena+="Suma: "+str(suma)
    cadena+="\n"
    cadena+="resta: "+str(resta)
    cadena+="\n"
    if(basicos==True):
        cadena+="Multiplicacion: "+str(multi)
        cadena+="\n"
        cadena+="division: "+str(divi)
        cadena+="\n"
    return cadena

print(Calculadora(int(input("Ingrese sus numeros: ")),int(input("Ingrese su segundo numero: ")),bool(input("interactue si quiere calculadora avanzada: "))))
