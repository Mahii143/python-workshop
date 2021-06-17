from tkinter import Tk, Canvas

parent = Tk()
parent.geometry("300x300")
can = Canvas(parent, width = 300, height = 300)
can.pack()
can.create_rectangle(10,100,100,200,fill = "blue")
can.create_oval(30, 30 , 100, 100, fill = "yellow")
can.create_lineoval(30, 30 , 100, 100, fill = "yellow")
parent.mainloop()
