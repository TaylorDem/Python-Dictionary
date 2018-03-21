#Dictionary Project using Tkinter within python

#!/usr/bin/python

import tkinter
top = tkinter.Tk()

# Code to add widgets will go here...

def alertMe():
    alertWindow = tkinter.Tk()
    alertText = tkinter.Text(alertWindow)
    alertText.insert(tkinter.INSERT, "Why did you think this was real?")
    alertText.pack()
    alertWindow.mainloop()

UselessAlert = tkinter.Button(top, text="Alert", command=alertMe)
UselessAlert.pack()
top.mainloop()
