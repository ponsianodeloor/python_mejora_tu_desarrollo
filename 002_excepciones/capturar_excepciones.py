lista = [2, 4]

try:
    print(lista[0])
except(IndexError):
    print("No existe dentro del rango")
else:
    print("no existe ningun error")
finally:
    print("Se ejecuto con exito")