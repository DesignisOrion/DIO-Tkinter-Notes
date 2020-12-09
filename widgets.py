# Self Adjusting Widgets
# Responsive Widgets is this chapter.


from tkinter import *

root = Tk()

label1 = Label(root, text="First", bg="Red", fg="White")
# fill=X means its going to fill the width of the window
label1.pack(fill=X)


# increase label of the window size.
label2 = Label(root, text="Second", bg="blue", fg="Green")
label2.pack(side=LEFT, fill=Y)


root.mainloop()


# App should show the two labels responsive to the window.
