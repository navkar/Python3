def main():
    print("Loops")
    x = 0


    while(x < 5):
        print("Loop " + str(x))
        x = x + 1

    # There are iterators
    for x in range(5, 100):
        print("For loop :" + str(x))

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for d in days:
        print(d)

    for x in range(5,10):
        #if (x == 7): break
        if (x % 2 == 0 ): continue
        print (x)

    # index, value = enumerate function
    dow = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for i,d in enumerate(dow):
        print (i,d)


if __name__ == "__main__":
    main()
