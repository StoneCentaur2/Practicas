import datetime
def calculadora(año, mes, dia):
    nacimiento = datetime.datetime(año, mes, dia)
    dia = datetime.datetime.now()
    fechaUsuario = datetime.datetime(dia.year, dia.month, dia.day)
    edad = fechaUsuario - nacimiento
    return "Tu edad es: " + str(int(edad.days/365.242199))