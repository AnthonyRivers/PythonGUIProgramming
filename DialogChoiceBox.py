
# add a menu bar to the main window
# add menus to the menu bar
# add menu items to the menus

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title('Create Menu Bar')

# exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

#create a menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

# add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New')
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',underline=1, command=_quit)

menuBar.add_cascade(label='File', menu=fileMenu)

def _msgBox():
   #mBox.showinfo('Python Info Box','Creating message dialogs is way easier in Python!') 
   #mBox.showwarning('Python Warning Box', 'I love how easy it is to create dialog messages in Python!')
   mBox.showerror('Error', 'User error -\nPlease replace user.')
   

def randError():
    #mBox.showerror('Error', 'Random Error just to annoy you.')
    mBox.askyesno('Dual choice message', 'Are you sure you want to do this?')

# adding a second menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About',command=_msgBox)
helpMenu.add_command(label='Random Error', command=randError)
menuBar.add_cascade(label='Help', menu=helpMenu)

win.mainloop()
