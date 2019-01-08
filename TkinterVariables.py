import tkinter as tk

# Create instance of tkinter.
win = tk.Tk()

# Assign tkinter Variable to strData variable
strData = tk.StringVar()

# set strData variable
strData.set('Hello Mantonio!')

# Get value of strData variable
varData = strData.get()

# Print out current value of strData
print(varData)

# Print out the default tkinter variable values
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())
