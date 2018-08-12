def main():
    # w+ = write and create, a = append only
    f = open("newfile.txt", "w+")
    #f = open("newfile.txt", "a")
    for i in range(1,100):
        f.write("This is on line " + str(i) + "\r\n")

    f.close()
    # Read and print out the contents of the file
    f = open("newfile.txt", "r")
    if (f.mode == 'r'):
        contents = f.read()
        # f.readlines()
        print(contents)


if __name__ == "__main__":
    main()