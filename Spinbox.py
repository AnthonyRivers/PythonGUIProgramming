import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox
from tkinter import scrolledtext

win = tk.Tk()
win.title('Spin Box')

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# I find the argument name from_ unusual.
#spin = Spinbox(win, from_=0, to=10, width=5, bd=8, command=_spin)
# We can spicify values by using the values parameter
spin = Spinbox(win, values=(1,2,4,42,100), from_=0, to=10, width=5, bd=8, command=_spin)

spin.grid(column=0,row=2)

# adding a second spinbox widget
spin = Spinbox(win, values=(0,50,100), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=1, row=2)

# Using a scrolled text control
scrolW = 30
scrolH = 3

# adding a spinbox widget
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)

win.mainloop()
