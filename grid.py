from tkinter import *

root = Tk()

# Creating Labels

label1 = Label(root, text="Firstname")
label2 = Label(root, text="Lastname")

# Creating Text fields
entry1 = Entry(root)
entry2 = Entry(root)

# Arrange in the grid format

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

# Want to have the labels place in front of the entry level respectively.add()
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


root.mainloop()
