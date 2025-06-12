Peliculas = []
nuevaPelicula =""
while nuevaPelicula !="Parar":
    nuevaPelicula = input("ingresar la pelicula o escribir 'Parar': ")
    Peliculas.append(nuevaPelicula)

for Pelicula in  Peliculas:
    print(f"{-Peliculas.index(Pelicula)+10}.{Pelicula}")