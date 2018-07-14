def decorator_func(func):
    def wrapper(*args, **kwdargs):
        return func(*args, **kwdargs)
    wrapper.__name__ = func.__name__
    return wrapper


@decorator_func
def square(x):
    return x**2

print(square.__name__)