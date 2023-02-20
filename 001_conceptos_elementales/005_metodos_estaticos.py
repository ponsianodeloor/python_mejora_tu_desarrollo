class Person:

    def __init__(self):
        pass

    def brincar(self):
        print("Brinco")

    @classmethod
    def correr(cls):
        print("Corro")

    @staticmethod
    def nadar():
        print("Nado")

    def __str__(self):
        pass


ponsiano = Person()
ponsiano.nadar()

