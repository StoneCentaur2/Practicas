import sqlite3
cn = sqlite3.connect("prueba.db")#Conexión y creación de la base de datos en sqlite
cursor=cn.cursor()#conección de la base de datos
cursor.execute("CREATE TABLE IF NOT EXISTS usuario(Nombre VARCHAR(45), Contraseña VARCHAR(20));")#Crear tabla si no existe
cn.commit()
cursor.execute("SELECT * FROM usuario;")#consulta de los usuarios existentes
dato = cursor.fetchall()  #fetchall() se usa para mostrar el contenido de la tabla de la consulta
print("Usuarios en existencia: ")
print(dato) #impresión de los usuarios con su contraseña
prin = True
while prin: # un mini menú
    sw = int(input("ingresar usuario = 1 \n"+
    "Logearte = 2 \n"+
    "Salir = 3 \n"))
    if(sw == 1):
        nom = input("Ingrese su nombre de usuario para un nuevo usuario: ")
        Password = input("Ingrese su contraseña para un nuevo usuario: ")
        cursor.execute("INSERT INTO usuario VALUES('"+nom+"','"+Password+"');") #Para ingresar un nuevo usuario a la bd
        cn.commit()
    if(sw == 2):    # segunda opción logea al usuario
        print("Login para iniciar sesión")
        validador = True # inicia en true para que pueda entrar al ciclo
        while validador:
            nombre= input("Ingrese su usuario: ")
            Passwd= input("Ingrese su contraseña: ")
            consulta = f"SELECT Nombre FROM usuario WHERE Nombre = '"+nombre+"' AND Contraseña = '"+Passwd+"';"
            cursor.execute(consulta) # se aplica en el cursor la consulta
            if not cursor.fetchone(): # sino encuentra nada entrará a este if con la ayuda del fetchone()
                print("Su usuario no se encontro registrado, intente nuevamente")
                validador = True
            else:
                print("Bienvenid@ \n")
                validador = False # Para romper el ciclo
                prin = False # Para romper el ciclo del mini menú
    if(sw == 3):
        prin=False
cn.close()