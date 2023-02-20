def primerD(fn):
    def fnDecorada(*args, **kwargs):
        print("Primer decorador")
    return fnDecorada

@primerD
def fn():
    print("Mi primer decorador")

fn()