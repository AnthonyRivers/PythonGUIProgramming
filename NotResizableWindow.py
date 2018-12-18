import tkinter as tk

win = tk.Tk()

win.title("Window Does Not Resize")

# call the geometry method to resize the window and set the location of where the window will appear on the screen.
win.geometry("300x500+300+100")

# call the resizable method and pass (0,0) as arguments to make the window not resizable.
win.resizable(0,0)

win.mainloop()
