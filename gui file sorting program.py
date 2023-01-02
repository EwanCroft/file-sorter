import os
from tkinter import *
import shutil

def getInputBoxValue():
    userInput = Path_Input.get()
    return userInput


def Sort():
    path = Path_Input.get()
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path + "/" + extension):
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)
        else:
            os.makedirs(path + "/" + extension)
            shutil.move(path + "/" + file, path + "/" + extension + "/" + file)


def GotoFolder():
    userInput = Path_Input.get()
    os.startfile(userInput)


root = Tk()

root.geometry('290x80')
root.configure(background='#808080')
root.title('File Sorter')
Label(root, text='Path to Folder', bg='#808080', font=('arial', 12, 'normal')).place(x=15, y=5)
Path_Input = Entry(root)
Path_Input.place(x=125, y=5)
Button(root, text='Sort', bg='#FFFFFF', font=('arial', 12, 'normal'), command=Sort).place(x=15, y=35)
Button(root, text='Go to Folder', bg='#FFFFFF', font=('arial', 12, 'normal'), command=GotoFolder).place(x=75, y=35)

root.mainloop()
