import os
from os import path
import shutil
from zipfile import ZipFile

def main():
    if path.exists("newfile.txt"):
        src = path.realpath("newfile.txt")

        dst = src + ".bak"

        shutil.copy(src, dst)
        shutil.copystat(src, dst)
        print("File copy complete")
        os.rename("newfile.txt.bak", "data.txt")
        print("File rename complete")

    with ZipFile("archive.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("data.txt")

    print("Zip file complete. Verify!")

if __name__ == "__main__":
    main()