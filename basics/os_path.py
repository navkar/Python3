
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print("OS Utilities\r\n")
    print(os.name)
    file_name = "newfile.txt"
    print("Item real path: " + str(path.realpath(file_name)))
    print("Item path and name: " + str(path.split(path.realpath(file_name))))
    print("Item found ? " + str(path.exists(file_name)))
    print("File ? " + str(path.isfile(file_name)))
    print("Directory ? " + str(path.isdir(file_name)))

    t = time.ctime(path.getmtime(file_name))
    print("Last modified time: " + t)
    print(datetime.datetime.fromtimestamp(path.getmtime(file_name)))

    # how long ago was the file modified
    time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(file_name))

    print("Modified since: " + str(time_diff) + " or seconds " + str(time_diff.total_seconds()))



if __name__ == "__main__":
    main()