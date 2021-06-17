from tkinter import *
parent = Tk()

#buttons

bluebutton = Button(parent, text = "Blue", fg = "blue")
bluebutton.pack(side = TOP)

blackbutton = Button(parent, text = "Black", fg = "black")
blackbutton.pack(side = BOTTOM)

redbutton = Button(parent, text = "Red", fg = "red")
redbutton.pack(side = LEFT)

greenbutton = Button(parent, text = "Green", fg = "green")
greenbutton.pack(side = RIGHT)

parent.mainloop()

#no errors ran successfully
