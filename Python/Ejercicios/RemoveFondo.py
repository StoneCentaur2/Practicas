'''import numpy as np
import rembg
import io
from PIL import Image

def quitar_fondo(imagen):
    # Cargar la imagen
    with open(imagen, "rb") as f:
        imagen_bytes = f.read()

    # Procesar la imagen con rembg
    imagen_procesada = rembg.remove(imagen_bytes)

    # Convertir la imagen procesada a un objeto de tipo PIL Image
    imagen_pil = Image.open(io.BytesIO(imagen_procesada)).convert("RGBA")

    # Crear una máscara binaria utilizando el canal alfa de la imagen
    datos_imagen = np.array(imagen_pil)
    mascara = datos_imagen[:, :, 3]

    # Aplicar la máscara a la imagen original
    imagen_sin_fondo = datos_imagen[:, :, :3] * np.expand_dims(mascara, axis=2)

    # Guardar la imagen sin fondo
    imagen_sin_fondo_pil = Image.fromarray(imagen_sin_fondo.astype(np.uint8))
    imagen_sin_fondo_pil.save("imagen_sin_fondo.png")

    # Mostrar la imagen resultante
    imagen_sin_fondo_pil.show()

import os

# Obtener la ruta absoluta del archivo
ruta_absoluta = os.path.abspath("Drax.jpg")

# Llamar a la función quitar_fondo con la ruta absoluta
quitar_fondo(ruta_absoluta)
La mejor prueba
'''
import numpy as np
import rembg
import io
from PIL import Image

def quitar_fondo(imagen):
   # Cargar la imagen
   with open(imagen, "rb") as f:
       imagen_bytes = f.read()

   # Procesar la imagen con rembg
   imagen_procesada = rembg.remove(imagen_bytes)

   # Convertir la imagen procesada a un objeto de tipo PIL Image
   imagen_pil = Image.open(io.BytesIO(imagen_procesada)).convert("RGBA")

   # Ajustar la transparencia de la imagen
   datos_imagen = np.array(imagen_pil)
   mascara = datos_imagen[:, :, 3]
   nueva_transparencia = np.where(mascara > 0, 255, 0)
   datos_imagen[:, :, 3] = nueva_transparencia

   # Crear una nueva imagen con los colores ajustados
   imagen_ajustada = Image.fromarray(datos_imagen)

   # Guardar la imagen ajustada
   imagen_ajustada.save("Bad-batchSinFondo.png")

   # Mostrar la imagen resultante
   imagen_ajustada.show()

# Ejemplo de uso
quitar_fondo('Bad-batch.jpg')

