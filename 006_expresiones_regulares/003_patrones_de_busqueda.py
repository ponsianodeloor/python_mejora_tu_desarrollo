import re

busqueda = re.search(r"K", "Kilometro")
print(busqueda)

#esto significa que estamos buscando 3 numeros y estanjuntos
busqueda = re.search(r"\d\d\d", "kilo912metro")
print(busqueda)

#group ayuda a devolver la cadena que estamos buscando
patron = re.compile("\d\d\d")
print(patron.search("kilo912metro").group())

if(re.search("\Aa[0-9].*(end|fin)$", "a4 es una marca de fin")):
    print("Se encontro el patron")