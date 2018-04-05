#Dictionary Project using Tkinter within python
#
#   pyinstaller dict.py in terminal will create a .exe
#in case its been far too long.. python dict.py runs program
#   

#These imports handle GUI
import tkinter
from tkinter import messagebox

#These imports will handle pulling from dictionary.com
import requests
import bs4  #beautifulsoup4

#top is the window that pops up.
top = tkinter.Tk()
top.title("Taylor Dictionary")
top.configure(bg='blue')
top.geometry('500x300') #size of window

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
savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

#defined is the text box that hold definition
definitionBox = tkinter.Text(rightFrame)
definitionBox.config(wrap=tkinter.WORD)
definitionBox.insert(tkinter.INSERT, 'Definition here.')
definitionBox.pack(side = tkinter.RIGHT)

#opens .txt file to save more permanently
text_file = open("Current_Dict.txt", "a")

#this function is the save button command
def saveWord():
    #if messagebox.askokcancel("Confirm", "You sure this is a word?"): #I don't think I like this. at all.
        savedText.insert(savedText.size(), wordEntry.get())
        savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
        
        #
        #Now this bit will save word to a .txt file
        text_file.write("%s\n" % (wordEntry.get()))

        wordEntry.delete(0, tkinter.END) #clear it for next word

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
        savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

#delete button
deleteButton = tkinter.Button(leftFrame, text="Delete", command=deleteWord)
deleteButton.pack(anchor = tkinter.W)

#search function
def searchOnline():
    dictionaryurl = 'http://www.dictionary.com/browse/' + savedText.get(savedText.curselection()) + '?s=t'
    searchWord = requests.get(dictionaryurl)
    definitionBox.delete(1.0, tkinter.END) #it was a hassle here. 1.0 is very important!
    #this line below makes it legible
    parsedText = bs4.BeautifulSoup(searchWord.text, 'html.parser')
    #the site dictionary.com has the definition in the 'meta' tag on its site with the name description 
    definition = parsedText.find('meta', attrs={'name':'description'})
    definitionBox.insert(tkinter.INSERT, definition["content"][:-10])   #this pulls content out of it.args
    #each content on the site ends with " see more." so with   ^^^^ I delete the last 10 characters
    definitionBox.pack(side = tkinter.BOTTOM)

#search button :)
searchButton = tkinter.Button(leftFrame, text="Online Def", command=searchOnline)
searchButton.pack(anchor = tkinter.W)


top.mainloop()