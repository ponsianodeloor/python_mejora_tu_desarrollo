class Person:

    # sirve para personalizar la creacion de las instancias de las clases y hacerlas inmutables
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    # este es encargado de las tareas de inicializacion
    def __init__(self):
        print("init")

    def __str__(self):
        pass


ponsiano = Person()
