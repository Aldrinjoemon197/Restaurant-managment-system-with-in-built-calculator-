from tkinter import *
import tkinter as tk
from tkinter import ttk
from book import *
from order import *

window = Tk()
window.title("User Authentication")
window.geometry("400x150")
l=Label(window, text=" Welcome to restaurant management system\n\n->Click here to book a table\n\n\n->Click here to order food")
l.place(x=10, y=10)

b1=Button(window, text="Book", command=ex_8)
b1.place(x=230, y=40)

b2=Button(window, text="Order", command=ex_10)
b2.place(x=230, y=80)

window.mainloop()