"""Code I stole."""
import subprocess as sp
import random
from tkinter import *
programName = "notepad.exe"

"""
By Zach Nichols
Name: FYRE 2022 Naame Sock Shuffle
Purpose: Shuffle the names of individuals
"""

def main():
    '''This initilaizes the names of everyone in the group into a list.'''
    names = ["das", "sda", "fdsaodas", "dsa"]

    """This shuffles the names like a deck of cards 5 times. Doing it 5 times because it was just an arbritrary number."""
    for i in range(5):
        random.shuffle(names)

    """All this does is open/create a new text file for your viewing pleasure."""
    f = open("Order.txt", "w")

    """This converts the list to something called a string. Not important, just makes it easier and cleaner to view later."""
    s = ""
    for i in range(len(names)):
        s = s + names[i]
        s = s + " > "
    s =s + names[0]

    """This takes the previously mentioned string and writes to the text file you'll hopefully be seeing."""
    f.write(s)
    f.close

    """Wow, it just opened, only for you! ;)"""
    filename = "Order.txt"
    sp.Popen([programName, filename])

"""This just runs everything"""
if __name__ == '__main__':
    main()
