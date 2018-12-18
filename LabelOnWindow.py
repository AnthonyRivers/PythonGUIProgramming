# we still need to import tkinter
import tkinter as tk
# we import a new module that provides advanced widgets to make the GUI look great.
from tkinter import ttk

win = tk.Tk()
win.title('Adding a Label')

# Adds a label to the window. We pass the Tk instance, and the text that will be display as a label. We also make use of the grid layout manager method to position the label on the window. This also allows for the GUI to epxand automatically when te text becomes longer. 
#
ttk.Label(win, text='Pythong Programming is AWESOME! Making the text longer expands the GUI automatically.').grid(column=0, row=0)
win.mainloop()
