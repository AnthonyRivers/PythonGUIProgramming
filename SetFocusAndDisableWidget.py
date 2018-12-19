import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Set Focus and Disable Widgets')

aLabel = ttk.Label(win, text='A label')
aLabel.grid(column=0, row=0)

# Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get())

# Changing the label
ttk.Label(win, text='Enter a name:').grid(column=0,row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12,textvariable=name)
nameEntered.grid(column=0,row=1)

# Adding a Button
action = ttk.Button(win, text='Click Me!', command=clickMe)
action.configure(state='disabled')
action.grid(column=1,row=1)

nameEntered.focus()
win.mainloop()
