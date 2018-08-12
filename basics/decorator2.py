def outer(func):
    def inner():
        print("Accessing :", func.__name__)
        return func()
    return inner

@outer

def greet():
    return 'Hello!'

greet()
print(greet())

# output
# Accessing : greet
# Accessing : greet
# Hello!