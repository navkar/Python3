def factory(n=0):
    
    def current():
        return n

    def counter():
        nonlocal n
        n += 1
        return n       
    return (current, counter)        

f_current, f_counter = factory(99)

print(f_current())
print(f_counter())