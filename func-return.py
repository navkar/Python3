# Parenthesis after the inner function are removed so that the outer function returns inner function.
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner   # Removed '()' to return 'inner' function itself

print(outer()) #returns 'inner' function
func = outer() 
print(type(func))
print(func()) # calling 'inner' function

