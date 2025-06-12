def imagen_a_hexadecimal():
    # Solicitar al usuario la ruta de la imagen
    ruta_imagen = input("Ingrese la ruta de la imagen: ")

    try:
        # Abrir la imagen en modo lectura de bytes
        with open(ruta_imagen, "rb") as f:
            # Leer los bytes de la imagen
            bytes_imagen = f.read()

        # Convertir los bytes a una cadena hexadecimal
        hexadecimal = bytes_imagen.hex()

        # Mostrar la representación hexadecimal de la imagen
        print("La imagen en formato hexadecimal:")
        print(hexadecimal)
    except FileNotFoundError:
        print("Error: No se pudo encontrar la imagen en la ruta especificada.")

# Ejemplo de uso
imagen_a_hexadecimal()
