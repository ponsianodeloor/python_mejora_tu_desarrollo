import re

busqueda = re.sub(r"\d", "*", "mpang8uera990")
print(busqueda)

#a los primeros 2 numeros se los muestra de izquierda a derecha
busqueda = re.sub(r"\d", "*", "mpang8uera990", 2)
print(busqueda)