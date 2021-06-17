from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#back_end

#getting input from combobox:
global box1
global box2
global curr1
global curr2
global val1
global val2
global currencies

#conversions:
#1 currency is equals to :
ame_val = {'American Dollar':1,"Indian Rupee": 72.69 , 'Chinese Yuan':11.17, 'Japanese Yen':0.67, 'Euro':86.89,'Pound Sterling':101.18 ,'Singapore Dollar':54.06,
           'Malaysian Dollar':17.65 , 'Saudi Riyal':19.38,'Qatar Riyal':19.96 }
inr_val = {'American Dollar':0.014,"Indian Rupee": 1 , 'Chinese Yuan':0.090, 'Japanese Yen':1.50, 'Euro':0.012,'Pound Sterling':0.0099 , 'Singapore Dollar':0.018,
           'Malaysian Dollar':0.057 , 'Saudi Riyal':0.052,'Qatar Riyal':0.050 }
chi_val = {'American Dollar':0.15,"Indian Rupee": 11.17, 'Chinese Yuan':1, 'Japanese Yen':16.75, 'Euro':0.13,'Pound Sterling':0.11 , 'Singapore Dollar':0.21,
           'Malaysian Dollar':0.6333 , 'Saudi Riyal':0.58,'Qatar Riyal':0.56 }
jap_val = {'American Dollar':0.0092,"Indian Rupee": 0.67, 'Chinese Yuan':0.060, 'Japanese Yen':1, 'Euro':0.0077,'Pound Sterling':0.0066 , 'Singapore Dollar':0.012,
           'Malaysian Dollar':0.038, 'Saudi Riyal':0.038,'Qatar Riyal':0.033 }
eur_val = {'American Dollar':1.20,"Indian Rupee": 86.89, 'Chinese Yuan':7.78, 'Japanese Yen':130.27, 'Euro':1,'Pound Sterling':0.86, 'Singapore Dollar':1.61,
           'Malaysian Dollar':4.92, 'Saudi Riyal':4.48,'Qatar Riyal':4.35}
pou_val = {'American Dollar':1.39,"Indian Rupee": 101.18, 'Chinese Yuan':9.06, 'Japanese Yen':151.71, 'Euro':1.16,'Pound Sterling':1, 'Singapore Dollar':1.87,
           'Malaysian Dollar':5.73, 'Saudi Riyal':5.22,'Qatar Riyal':5.07}
sin_val = {'American Dollar':0.74,"Indian Rupee": 54.06, 'Chinese Yuan':4.84, 'Japanese Yen':81.06, 'Euro':0.62,'Pound Sterling':0.53, 'Singapore Dollar':1,
           'Malaysian Dollar':3.06, 'Saudi Riyal':2.79,'Qatar Riyal':2.71}
mal_val = {'American Dollar':0.24,"Indian Rupee": 17.65, 'Chinese Yuan':1.58, 'Japanese Yen':26.55, 'Euro':0.20,'Pound Sterling':0.17, 'Singapore Dollar':0.33,
           'Malaysian Dollar':1, 'Saudi Riyal':0.91,'Qatar Riyal':0.88}
sau_val = {'American Dollar':0.27,"Indian Rupee": 19.38, 'Chinese Yuan':1.74, 'Japanese Yen':29.06, 'Euro':0.22,'Pound Sterling':0.19, 'Singapore Dollar':0.36,
           'Malaysian Dollar':1.10, 'Saudi Riyal':1,'Qatar Riyal':0.97}
qat_val = {'American Dollar':0.27,"Indian Rupee": 19.96, 'Chinese Yuan':1.79, 'Japanese Yen':29.93, 'Euro':0.23,'Pound Sterling':0.20, 'Singapore Dollar':0.37,
           'Malaysian Dollar':1.03, 'Saudi Riyal':1.03,'Qatar Riyal':1}

currencies = {'American Dollar':ame_val,'Indian Rupee':inr_val,'Chinese Yuan':chi_val,'Japanese Yen':jap_val, 'Euro':eur_val,'Pound Sterling':pou_val,
              'Singapore Dollar':sin_val, 'Malaysian Dollar':mal_val, 'Saudi Riyal':sau_val,'Qatar Riyal':qat_val}
#conversion
def conv():
    #getting user choices and values
    perm_currency = box1.get()
    converted_currency = box2.get()
    value = int(e1.get())
    #accessing the values and keys from currencies dictionary
    for i,j in currencies.items():
        if i == perm_currency:
            value1 = j
            #accessing the values and keys from specific currency value
            for val,key in value1.items():
                if val == converted_currency:
                    result = value*key
                    label = Label(win, text = result, font =("Times New Roman", 20), fg = "blue")
                    label.place(x = 250, y = 250)
                    
                    
#front_end

win = Tk()
win.geometry("500x300")
win.title("Currency Converter")

#Heading

head = Label(win,text = "CURRENCY CONVERTER", bg = "violet", fg = 'white',
             font = ("Times New Roman", 15))
head.pack()

#convert button

conv = Button(win, text = 'CONVERT', fg = "blue",command  = conv)
conv.place(x = 275, y = 145)

#entry1

e1 = Entry(win, width  = 20)
e1.place(x = 250 ,y = 100)

#label names
name1 = Label(win, text = "Choose your currency :")
name1.place(x = 100, y = 80)

name2 = Label(win, text = "Convert into :")
name2.place(x = 100, y =130)

name3 = Label(win, text = "Result: ")
name3.place(x = 250, y =230)

#combox 1

n1= tk.StringVar()

box1 = ttk.Combobox(win, width = 20, textvariable = n1)
box1['values'] = ('American Dollar','Indian Rupee','Chinese Yuan','Japanese Yen', 'Euro','Pound Sterling',
                  'Singapore Dollar', 'Malaysian Dollar', 'Saudi Riyal','Qatar Riyal')
box1.place(x = 100, y = 100)
box1.current()

#combobox 2

n2 = tk.StringVar()


box2 = ttk.Combobox(win, width = 20, textvariable = n2)
box2['values'] = ('American Dollar','Indian Rupee','Chinese Yuan','Japanese Yen', 'Euro','Pound Sterling',
                  'Singapore Dollar', 'Malaysian Dollar', 'Saudi Riyal','Qatar Riyal')
box2.place(x = 100, y = 150)
box2.current()
win.mainloop()
