def main():
    # w+ = write and create 
    f = open("newfile.txt", "w+")
    
    for i in range(1,100):
        f.write("This is on line " + str(i) + "\r\n")