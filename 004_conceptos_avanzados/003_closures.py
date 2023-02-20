def a(x):
    def b(y):
        return x + y
    return b


fn = a(5)
print(fn(3))

fn_ab = a(10)
print(fn_ab(20))