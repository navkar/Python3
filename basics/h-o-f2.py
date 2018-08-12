def outer(x, y):

    def inner1():
        return x+y

    def inner2(z):
        return inner1() + z

    return inner2


f = outer(10, 25)

print(f(15))