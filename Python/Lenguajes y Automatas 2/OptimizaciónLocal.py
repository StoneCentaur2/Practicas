#Primero deben de ir las funciones para poder usarlas en cualquier otra continuación.
#funcion para las preguntas de las personas
def preguntas():
    nom = input("Nombre de la persona: ")#pregunta el nombre para diferenciar
    ed = int(input("Edad de la persona: "))#Edad para el calculo
    #Imprimira el nombre para que se distingan las personas
    if(ed < 18):
        print(nom + ", persona con menoría de edad \n")
    else:
        print(nom + ", persona con mayoría de edad \n")

def calcular():
    #Flotantes por los decimales que se pueden usar
    a = float(input ("Su altura en metros por favor (ej: 1.70): "))
    m = float(input("Su masa en kilogramos por favor (ej: 80): "))
    IMC = m / a**2 #Calculo del IMC
    #Comparaciones con las aproximaciones que tiene cada IMC
    if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99 :
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    
    print("Su IMC es de: " + str(IMC) + "\n") #Para mostrar el IMC

personas = int(input("Cantidad de personas a verificar su IMC: "))
#Ciclo while para usar la cantidad de personas hasta llegar a cero
#Se pone cantidad para que no se cicle en lo mismo
while personas > 0:
    print("Persona #"+ str(personas) +" a responder")
    #Funciones a usar para optimizar el proceso
    preguntas()
    calcular()
    #Para evitar el bucle se usa una resta de la cantidad de personas
    personas = personas - 1
