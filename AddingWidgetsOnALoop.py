import tkinter as tk
from tkinter import ttk
from tkinter import IntVar


win = tk.Tk()
win.title('Create Radio Button With a Loop')
colors = ['Blue','Gold','Red']

def radCall():
    radSel = radVar.get()

    if      radSel == 0: win.configure(background=colors[0])
    elif    radSel == 1: win.configure(background=colors[1])
    elif    radSel == 2: win.configure(background=colors[2])

#create 3 Radiobuttons using one variable
radVar = tk.IntVar()

# next select a non-existing index value for radVar.
radVar.set(99)

# now create all 3 Radiobuttons widgets with one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


win.mainloop()
