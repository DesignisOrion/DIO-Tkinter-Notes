from tkinter import *


root = Tk()

# create the canvas we will draw on

canvas = Canvas(root, width=200, height=100)
canvas.pack()


# draw a line with the line name

newline = canvas.create_line(0, 0, 50, 100)
otherline = canvas.create_line(10, 10, 100, 100, fill="green")


root.mainloop()
