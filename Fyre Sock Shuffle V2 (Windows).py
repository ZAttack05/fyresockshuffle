"""
Author: Zach Nichols
Version : 2.0
Name: Fyre Sock Suffle
"""

"""Imports some stuff in. Like we aren't letting the Chinese do to our country."""
import subprocess as sp
import random
from tkinter import *
from tkinter import messagebox

def Next():
    DoneButton.config(state=NORMAL)
    name = Input.get()
    if name == "" or name == "\n":
        ierror()
    else:
        namelist.append(name)
        print(namelist)
        Input.delete(0, END)

def eNext(e):
    DoneButton.config(state=NORMAL)
    name = Input.get()
    if name == "" or name == "\n":
        ierror()
    else:
        namelist.append(name)
        print(namelist)
        Input.delete(0, END)


def ierror():
    messagebox.showinfo("Name error", "Please enter a name first.")

def Reset():
    namelist = []
    DoneButton.config(state=DISABLED)

def Done():
    for i in range(5):
        random.shuffle(namelist)

    s = ""
    for i in range(len(namelist)):
        s = s + namelist[i]
        s = s + " > "
    s =s + namelist[0]

    f = open("Order.txt", "w")
    f.write(s)
    f.close

    sp.Popen(["notepad.exe", "Order.txt"])


root = Tk()

"""Initializes the labels for the GUI"""
root.title("FYRE Sock Shuffle")
Label1 = Label(root, text = "Enter name here. Once you are done entering names, click done.", font = ("Calibri", 20))
Label1.grid(row = 0, column=0)
ResetButton = Button(root, text = "Reset", pady=10, state=NORMAL, command=Reset)
ResetButton.grid(row = 2, column = 1)
DoneButton = Button(root, text = "Done", pady=10, state=DISABLED, command=Done)
DoneButton.grid(row = 2, column = 2)
Input = Entry(root, width = 20)
Input.grid(row = 1, column = 0)
NextButton = Button(root, text = "Next", pady=10, state=NORMAL, command = Next)
NextButton.grid(row = 2, column = 0)
namelist = []

root.bind('<Return>', eNext)

root.mainloop()






