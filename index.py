from tkinter import *

w0, h0 = 1920, 1080
w1, h1 = 1920, 1080

window_root =  Tk()

# width x height 
#  To display on main (1st) window 
window_root.geometry("646x512")

# To display on second window 
# window_root.geometry(f"{w1}x{h1}-{w0}-0")

window_root.minsize(644,512)

window_root.maxsize(644,512)

lable = Label(text="Hello World")

lable.pack()

window_root.mainloop()
