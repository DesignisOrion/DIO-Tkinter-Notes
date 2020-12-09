from tkinter import *
# import messagebox first
import tkinter.messagebox

root = Tk()

# printing out the title and the info of the messagebox
tkinter.messagebox.showinfo("Title", "This is awesome")


# Accepting responses with a message box

response = tkinter.messagebox.askquestion("Question1", "Do you like Coffee?")

if response == 'yes':
    print("Here is coffee for you from Coffee Code & Convo.")


root.mainloop()
