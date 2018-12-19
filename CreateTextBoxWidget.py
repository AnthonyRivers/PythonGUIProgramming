import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Creating a Text Box')

aLabel = ttk.Label(win, text='A Label')
aLabel.grid(column=0, row=0)

# We are not using OOP yet, but we can still access the value
# of a variable that has not even been declared.

# This works because the button click event is a call back function
# and by the time the button is clicked by a user the variables
# reference in this function are known and exist. 

#Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get())


# Changing our Label
ttk.Label(win, text='Enter a name:').grid(column=0,row=0)

#Adding a TextBox Entry widget
# Using tkinter we have to declare the type tk.StringVar before we can use it
# successfully even though Python is a dynamically typed language.

# Tkinter is not the same language as Python, but we can use it from Python.
name = tk.StringVar()

# We are hardcoding the width so the widget will not expand.
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0,row=1)

# Adding a Button
action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=1, row=1)

win.mainloop()
