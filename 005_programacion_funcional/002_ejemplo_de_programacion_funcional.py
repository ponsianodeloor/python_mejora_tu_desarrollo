def lower(elementos): return elementos.lower()


lista = ["Ponsiano", "Jhair", "Eduardo", "Viviana"]
print(list(map(lower, lista)))

print([cad.lower() for cad in lista])


#funciones de orden superior
def saludo(idioma):
    def saludo_es():
        print("hola")

    def saludo_en():
        print("Hi")

    idioma_func = {"es": saludo_es(),
                   "en": saludo_en()
                   }

    return idioma_func[idioma]


saludar_en = saludo("en")
saludar_en

saludar_es = saludo("es")
saludar_es