import cv2
import numpy as np

# Crear una imagen en negro
image = np.zeros((500, 500, 3), dtype="uint8")

# Dibujar un círculo rojo
cv2.circle(image, (250, 250), 100, (0, 0, 255), -1)

# Mostrar la imagen
cv2.imshow("Imagen de prueba", image)

# Esperar a que se presione una tecla y cerrar
cv2.waitKey(0)
cv2.destroyAllWindows()
