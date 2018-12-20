import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Create Radio Button Widgets')
win.geometry('300x100')

# RadioButton Globals
COLOR1 = 'Blue'
COLOR2 = 'Gold'
COLOR3 = 'Red'

# RadioButton Callback
def radCall():
    radSel = radVar.get()
    if      radSel == 1: win.configure(background=COLOR1)
    elif    radSel == 2: win.configure(background=COLOR2)
    elif    radSel == 3: win.configure(background=COLOR3)


# create three RadioButtons using one variable
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=1, sticky=tk.W)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=1, sticky=tk.W)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=1, sticky=tk.W)


win.mainloop()
