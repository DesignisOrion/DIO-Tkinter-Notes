# Working with Drop Downs


from tkinter import *

# create the function to make the submenu work


def function1():
    print('Menu Item Clicked')


root = Tk()
# Create a menu with built in functions of tkinter
# Create a menu object

mymenu = Menu(root)

# lets the python know this is the menu we are using.
root.config(menu=mymenu)

# creating a sub menu and connect to the menu used.
submenu = Menu(mymenu)

# config the menu
mymenu.add_cascade(label="File", menu=submenu)

# create the actual submenu items

submenu.add_command(label="New Project...", command=function1)
submenu.add_command(label="Open Project...", command=function1)

# adding a seperartor within the menu to categorize the submenu

submenu.add_separator()


# adding the next submenu item cateory
submenu.add_command(label="Exit", command=function1)

# adding another menu on the main menu  called "mymenu"

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)

# item under the new menu is
newmenu.add_command(label="Undo", command=function1)


root.mainloop()
