# Parenthesis after the inner function are removed so that the outer function returns inner function.
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner   # Removed '()' to return 'inner' function itself

print("Invoking outer()")
print(outer()) #returns 'inner' function
print("Assigning outer() to a variable")
func = outer() 
print(type(func))
print(func()) # calling 'inner' function

