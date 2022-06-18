from tkinter import *
import tkinter
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=3, sticky=W)
mainloop()