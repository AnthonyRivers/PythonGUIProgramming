import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox

# Create instance
win = tk.Tk()

# Add a title
win.title('Python GUI')

# tab control ---------------------
tabControl = ttk.Notebook(win)      # create tab control

tab1 = ttk.Frame(tabControl)        # create a tab
tabControl.add(tab1, text='Tab 1')   # add the tab

tab2 = ttk.Frame(tabControl)        # add a second tab
tabControl.add(tab2, text='Tab 2')   # Make second tab visible

tabControl.pack(expand=1, fill='both') # Pack to make visible

containerFrame = ttk.LabelFrame(tab1, text='Container Frame to Hold Widgets')

spin = Spinbox(tab1, from_=0,to=10)
spin.grid(column=0, row=2)

#create menu bar
menuBar = Menu(tab1)
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_separator()
fileMenu.add_command(label='Exit')
menuBar.add_cascade(label='File', menu=fileMenu)

# Add another menu to the menu bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=helpMenu)


# change the main windows icon
win.iconbitmap(r'c:\Python34\DLLs\pyc.ico')

win.mainloop()

