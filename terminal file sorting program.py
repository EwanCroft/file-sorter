import os
import shutil
import sys

path = input("Enter path: ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + "/" + extension):
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
    else:
        os.makedirs(path + "/" + extension)
        shutil.move(path + "/" + file, path + "/" + extension + "/" + file)

print(f"\"{path}\" has been sorted.")
go = input("Do you want to go to the folder? (y/n): ")

if go == "y":
    os.startfile(path)
elif go == "n":
    sys.exit()
