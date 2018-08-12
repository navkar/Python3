# function as an argument

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def prod(x, y):
    return x * y

def do(func, x, y):
    return func(x, y)

print(do(add, 12, 4))  # 'add' as arg

print(do(sub, 12, 4))  # 'sub' as arg

print(do(prod, 12, 4))  # 'prod' as arg
