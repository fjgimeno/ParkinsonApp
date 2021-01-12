#Este arxiu es un test per importar imatges directament, ja que segons la web que habia vist, la variable img com a tal
#podria guardarse directament a la BD, pero el exemple era per a altre tipus de BD, aixi que faltaria buscar-ho,
#si trobares algo, comentameu y me pose a fer-ho.

#Load and show an image with Pillow


from PIL import Image
import os
import sys

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEPARATOR = os.path.sep
print(SEPARATOR)

#Load the image
img = Image.open(APP_PATH + SEPARATOR + "res" + SEPARATOR + "shrek.jpg")

#Get basic details about the image
print(img.format)
print(img.mode)
print(img.size)

#show the image
img.show()