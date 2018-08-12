# A Closure is a function returned by a higher order function, 
# whose return value depends on the data associated with the higher order function.
# 
def multiple_of(x):
    def multiple(y):
        return x * y
    return multiple

m5 = multiple_of(5) # 'm5' is a closure
m6 = multiple_of(6) # 'm6' is a closure

print(m5(4))
print(m6(4))
