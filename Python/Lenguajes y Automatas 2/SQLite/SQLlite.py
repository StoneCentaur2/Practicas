import sqlite3
cn = sqlite3.connect("prueba.db") #Creación y conexión de la base de datos
cursor=cn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS demo("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(45),"+
"descripción text)")#Creación de la tabla demo
cn.commit()
cursor.execute("INSERT INTO demo VALUES(null, 'Titulo del producto', 'Descripcion')")
cn.commit()
cursor.execute("SELECT * FROM demo")
print(cursor)
datos = cursor.fetchall()
print(datos)
for dato in datos:
    print("id: ", dato[0])
    print("titulo: ", dato[0])
    print("descripcion: ", dato[0])
    print("\n")
cursor.execute("SELECT * FROM demo")
dato=cursor.fetchone()
print(dato)
cn.close()