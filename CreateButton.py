import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Create a Button and Add to the GUI Window")

# Modify adding a label
aLabel = ttk.Label(win, text="A label")
aLabel.grid(column=0, row=0)

# Button click Event function
def clickMe():
    action.configure(text="** I have been clicked! **")
    aLabel.configure(foreground="red")
    aLabel.configure(text='A Red Label')

# Adding a Button
action = ttk.Button(win, text='Click Me', command=clickMe)
action.grid(column=1,row=0)

win.mainloop()
