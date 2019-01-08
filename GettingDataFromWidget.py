import tkinter as tk
from tkinter import Spinbox

win = tk.Tk()
win.title('Get Data From Widget')


def _spin():
    value = spin.get()
    print('Spinbox value: ' + value)
    
spin = Spinbox(win, width=5, bd=8, command=_spin)
spin['values'] = (1,2,4,42,100)
spin.grid(column=0,row=2)


win.mainloop()

