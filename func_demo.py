# define a function
def first():
    print("This is a default function")



# function that takes arguments
def second(arg1, arg2):
    print(arg1 , " " , arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

def multiply(*args2):
    result = 1
    for x in args2:
        result = result * x
    return result

first()
print (first()) # 'None' is returned by the print()
second(10,20)
print("Cube of 9 is " + str(cube(9)))
print("Cube of 2 is " + str(cube(2)))

print("2 ^ 1 is " + str(power(2)))
print("2 ^ 3 is " + str(power(2,3)))
print("3 ^ 2 is " + str(power(x=2,num=3)))

print("adding (1 + 2 + 7) : " + str(multi_add(1, 2, 7)))

print("multiply (111 * 222 * 333) : " + str(multiply(111, 222, 333)))

