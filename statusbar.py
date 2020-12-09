from tkinter import *

# create the function to make the submenu work


def function1():
    print('Menu Item Clicked')


root = Tk()


mymenu = Menu(root)


root.config(menu=mymenu)


submenu = Menu(mymenu)


mymenu.add_cascade(label="File", menu=submenu)


submenu.add_command(label="New Project...", command=function1)
submenu.add_command(label="Open Project...", command=function1)


submenu.add_separator()


submenu.add_command(label="Exit", command=function1)


newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)

newmenu.add_command(label="Undo", command=function1)


toolbar = Frame(root, bg="pink")


insertbutton = Button(toolbar, text="Insert Files", command=function1)

insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="Print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)


toolbar.pack(side=TOP, fill=X)


# Creating the Status Bar
status = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()
