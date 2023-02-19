class Person:
    age = 19

    def __init__(self):
        pass

    def despedir(self):
        print("Adios")

    @classmethod
    def saludar(cls, nombre):
        print("Estoy saludando ", nombre)


    def __str__(self):
        return self.nombre + " " + self.nacionalidad


Person.saludar("Ponsiano")
