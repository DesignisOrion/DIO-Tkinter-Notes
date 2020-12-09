from tkinter import *


# Create a class called myButtons

class MyButtons:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        # Create the buttons in classes so use self.button name

        self.printbutton = Button(
            frame, text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(
            frame, text="Exit App", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    # want to make the buttons work
    # Create the function for print button

    def printmessage(self):
        print("Button Clicked")


root = Tk()

# create object of the class
# we will name the object "b"

b = MyButtons(root)


root.mainloop()
