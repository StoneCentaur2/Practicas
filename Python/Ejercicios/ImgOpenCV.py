import cv2

imagen = cv2.imread('Banner2_1.jpg') # Colocando una , y un numero cambia de colores
cv2.imshow('Prueba de imagen', imagen) # Con esto muestra la imagen
cv2.imwrite('Otraimagen.png',imagen) # Sirve para sobre escribir otra imagen
cv2.waitKey(0) # Son milisegundos, 0 = press keyboard
cv2.destroyAllWindows() # Cierra la ventana