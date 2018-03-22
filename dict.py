#Dictionary Project using Tkinter within python
#
#   pyinstaller dict.py in terminal will create a .exe
#in case its been far too long.. python dict.py runs program
#   
import tkinter
from tkinter import messagebox

#top is the window that pops up.
top = tkinter.Tk()
top.title("Taylor Dictionary")
top.configure(bg='blue')
top.geometry('350x200') #size of window

#need frames to make it pretty and organized
leftFrame = tkinter.Frame(top)
leftFrame.configure(bg='blue')
leftFrame.pack(side = tkinter.LEFT)
#rightframe handles the list and scrollbar
rightFrame = tkinter.Frame(top)
rightFrame.pack(side=tkinter.RIGHT)

#scrollbar is for my list of saved words
scrollbar = tkinter.Scrollbar(rightFrame)
scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)

#savedText is the text box/list of saved words obvi
savedText = tkinter.Listbox(rightFrame, yscrollcommand = scrollbar.set)

#this function is the save button command
def saveWord():
    if messagebox.askokcancel("Confirm", "You sure this is a word?"):
        savedText.insert(savedText.size(), wordEntry.get())
        savedText.pack(anchor = tkinter.NE, fill = tkinter.BOTH)
        wordEntry.delete(0, tkinter.END)

#this line makes the scrollbar actually work, the rest is build up/initializing   
scrollbar.config(command = savedText.yview)

#word entry and label
wordLabel = tkinter.Label(leftFrame, text="Enter Word:", fg='cyan', bg='black')
wordLabel.pack( anchor = tkinter.W)
wordEntry = tkinter.Entry(leftFrame, bd =5)
wordEntry.pack(anchor = tkinter.W)

#definition entry and label
defineLabel = tkinter.Label(leftFrame, text="Definition:", fg='cyan', bg='black')
defineLabel.pack(anchor = tkinter.W)
defineEntry = tkinter.Entry(leftFrame, bd =5)
defineEntry.pack(anchor = tkinter.W)

#create button to save
saveButton = tkinter.Button(leftFrame, text="Save", command=saveWord)
saveButton.pack(anchor = tkinter.W)
#must put the location after you pack it.
#saveButton.place(x=10, y=100)

#delete function
def deleteWord():
    if messagebox.askokcancel("Confirm", "You sure this isn't a word?"):
        savedText.delete(savedText.curselection())
        savedText.pack(anchor = tkinter.NE, fill = tkinter.BOTH)

#delete button
deleteButton = tkinter.Button(leftFrame, text="Delete", command=deleteWord)
deleteButton.pack(anchor = tkinter.W)

top.mainloop()