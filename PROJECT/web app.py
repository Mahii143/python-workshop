from tkinter import *
from tkinter import Tk, Menu
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


#front end



'''
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

'''    

win=tk.Tk()

win.geometry("500x300")
win.title("Virtual Notes")

#menu bar
menu_bar= Menu(win)
#submenu
fileMenu = Menu(menu_bar, tearoff=0)


fileMenu.add_command(label="exit", command=win.destroy)
fileMenu.add_command(label="kill", command=win.destroy)
fileMenu.add_command(label="stop", command=win.destroy)

menu_bar.add_cascade(label="File", menu=fileMenu)
win.config(menu=menu_bar)

login_label = Label(win, text = "Login", fg="blue",
                    font = ("Poppins", 15)).place(x=210,y=50)

name = Label(win, text = "Name :").place(x=150,y=100)
e1 = Entry(win).place(x=220,y=100)
password = Label(win, text = "Password :").place(x=132,y=150)
e2 = Entry(win).place(x=220,y=150)

submit = Button(win, text = "Submit").place(x=210,y=200)
    
win.mainloop()

    















