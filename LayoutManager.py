# Section 2 - Layout Manager
# - Arrange several labels witin a label frame
# - Using padding to add space around widgets
# - Expanding the GUI dynamically using widgets
# - Align the GUI widgets by embedding frames within frames


import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Arranging Labels')

# Create a container to hold labels.
labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
# using padx and pady adds padding to the label
labelsFrame.grid(column=0, row=7, padx=20,pady=40)

# Place Labels into the container element
ttk.Label(labelsFrame, text='Label1').grid(column=0,row=0, sticky=tk.W)
ttk.Label(labelsFrame, text='Label2').grid(column=1,row=0, sticky=tk.W)
ttk.Label(labelsFrame, text='Label3').grid(column=2,row=0, sticky=tk.W)
ttk.Label(labelsFrame, text='Label4').grid(column=3,row=0, sticky=tk.W)


ttk.Label(labelsFrame, text='Label1').grid(column=0,row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=0,row=1)
ttk.Label(labelsFrame, text='Label3').grid(column=0,row=2)
ttk.Label(labelsFrame, text='Label4').grid(column=0,row=3)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8,pady=4)

win.mainloop()

