from tkinter import *


def cl1():
    greenbutton.configure(bg = "green")

def cl2():
    bluebutton.configure(bg = "blue")

def cl3():
    redbutton.configure(bg = "red")
    
global parent

parent = Tk()

parent.geometry("300x300")

greenbutton = Button(parent, text  = "Green", fg = "black", command = cl1)
greenbutton.place(x = 125,y = 100)
bluebutton = Button(parent, text  = "Blue", fg = "black", command = cl2 )
bluebutton.place(x = 125 ,y = 150)
redbutton = Button(parent, text  = "Red", fg = "black", command = cl3)
redbutton.place(x = 125 ,y = 200 )


parent.mainloop()

