#Write detecter implementation
def detecter(element):
    def isIn(sequence):
        if element in sequence:
            return True
        else:
            return False
    return isIn
    #Write isIn implementation    

#Write closure function implementation for detect30 and detect45
detect30 = detecter(30)
detect45 = detecter(45)

print("Detect 30 in sequence")
print(detect30([1,34,45,50]))
print("Detect 45 in sequence")
print(detect45([30,45,30,1,20]))