def numbers():
    n = 1
    while True:
        # se encarga de detener la ejecucion
        yield n
        n = n + 1


i = numbers()
print(i)
print(i.__next__())
print(i.__next__())
