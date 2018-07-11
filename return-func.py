# The return value of 'outer' function is the return value of 'inner' function i.e 'Hello world!'.
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner()    
print(outer())