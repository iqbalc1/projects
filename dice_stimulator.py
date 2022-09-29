import random
import tkinter
from tkinter import *


# toplevel widget which represents the main window of an application
root = Tk()
root.geometry("600x300")

label_1 = Label(root, text='', font=("arial",300) )

def roll_the_dice():
    num_code= ['\u2680', '\u2681','\u2682', '\u2683','\u2684', '\u2685']
    label_1.config(text=f'{random.choice(num_code)}')
    label_1.pack()
button_1 = Button(root, text='Roll the Dice', command=roll_the_dice)
button_1.place(x=250,y=0)

root.mainloop()

