def smart_divide(func): 
    def wrapper(*args): 
        a, b = args 
        if b == 0: 
            print('oops! cannot divide') 
            return
        return func(*args)
    return wrapper

@smart_divide 

def divide(a, b):
    return a / b

print(divide.__name__) 
print(divide(4, 16))
print(divide(8,0))