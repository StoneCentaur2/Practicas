from PIL import Image

def ajustar_resolucion(imagen, nueva_resolucion):
    # Abrir la imagen
    img = Image.open(imagen)

    # Ajustar la resolución
    img = img.resize(nueva_resolucion)

    # Guardar la imagen ajustada
    img.save("imagen_ajustada.png")

    # Mostrar información sobre la nueva resolución
    print("La imagen se ha ajustado a la resolución:", img.size)

# Ejemplo de uso
ajustar_resolucion('foto.png', (800, 600))
