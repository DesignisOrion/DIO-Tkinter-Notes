from tkinter import *

root = Tk()

# frame on the top
newframe = Frame(root)
newframe.pack()


otherframe = Frame(root)
# places the otherframe to the bottom
otherframe.pack(side=BOTTOM)

# adding widgets

# button = (which frame, text desired, font color)
button1 = Button(newframe, text="Click Here", fg="Red")
button2 = Button(newframe, text="Click Here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()
