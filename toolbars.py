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


# Creating a Toolbar

toolbar = Frame(root, bg="pink")


# adding toolbar buttons
insertbutton = Button(toolbar, text="Insert Files", command=function1)
# padx = X side, pady = Y side for padding
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="Print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)


# add the toolbar to the menu itself.
# fill=X will responsively run the toolbar to the window
toolbar.pack(side=TOP, fill=X)


root.mainloop()
