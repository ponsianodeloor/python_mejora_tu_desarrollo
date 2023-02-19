class Person:
    age = 19

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return self.nombre + " " + self.nacionalidad


nueva_persona = Person("Ponsiano De Loor", "Ecuatoriana")

print(nueva_persona)

print (Person.age)