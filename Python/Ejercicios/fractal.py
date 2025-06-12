import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la imagen
ancho = 800
alto = 800
max_iter = 256

# Crear una imagen vacía
imagen = np.zeros((alto, ancho))

# Definir el rango del conjunto de Mandelbrot
re_min, re_max = -2, 1
im_min, im_max = -1.5, 1.5

# Mapear cada pixel a una coordenada del plano complejo
for y in range(alto):
    for x in range(ancho):
        # Escalar las coordenadas de píxeles a las coordenadas del plano complejo
        c_re = re_min + (x / ancho) * (re_max - re_min)
        c_im = im_min + (y / alto) * (im_max - im_min)
        c = complex(c_re, c_im)
        
        # Iteración de Mandelbrot
        z = 0
        for i in range(max_iter):
            if abs(z) > 2:
                break
            z = z*z + c
        
        # Guardar el número de iteraciones en la imagen
        imagen[y, x] = i

# Mostrar la imagen generada
plt.imshow(imagen, cmap="twilight", extent=(re_min, re_max, im_min, im_max))
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()
