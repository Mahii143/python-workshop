
from tkinter import *
from tkinter import messagebox


def Ok():
    username = e1.get()
    password = e2.get()
    
    if username == "user123" and password == "12345":
        messagebox.showinfo("","Login Successfull")
        parent.destroy()
    else:
        messagebox.showinfo("","invalid user name and password")

def clear():
    e1.delete(0, END)
    e2.delete(0, END)

global parent
global e1
global e2

parent = Tk()

     parent.title("Login")
parent.geometry("300x200")



Label(parent,text = "Username: ").place(x = 20, y = 50)
Label(parent,text = "Password: ").place(x = 20, y = 80)


e1 = Entry(parent)
e1.place(x = 100, y = 50)

e2 = Entry(parent)
e2.place(x = 100, y = 80)

login = Button(parent, text = "Login",command= Ok)
login.place(x = 50 ,y = 150)

clearscreen = Button(parent, text = "Clear the screen", command = clear)
clearscreen.place(x = 100, y = 150)

parent.mainloop()
