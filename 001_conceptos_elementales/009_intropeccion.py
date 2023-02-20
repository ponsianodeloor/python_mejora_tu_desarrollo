class Introspeccion:
    Intro = 9
    def __init__(self, valor):
        self.valor = valor

    def segundo(self):
        print("segundo")

    def tercero(self):
        print("tercero")


dato = Introspeccion("Valor")
dir(dato)
print(dir(dato))

print(isinstance(dato, Introspeccion))
print(hasattr(dato, "Intro"))
