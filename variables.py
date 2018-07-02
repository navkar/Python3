# variables
f="GlobalVariable"
# print(f)

# f="This is string"
# print(f)

# f=0
# print("This is a string"+ str(123))

def localVariable():
    global f # This is using f global variable
    f="StringLocalVariable"
    print(f)

localVariable()
print(f)  

# Delete the declaration of a global variable
del f

# print(f) - This will not work.
