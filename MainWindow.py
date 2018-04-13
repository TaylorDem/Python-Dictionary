import tkinter
import ButtonFunctions as BF
import random
import requests


class MainWindow():
    def initList(self):
        text_file = open("Current_Dict.txt","r")
        old_words = text_file.readlines()
        for lines in old_words:
    	    self.savedText.insert(self.savedText.size(), lines[:-1])
        text_file.close()
    
    def saveButton(self):
        self.action.saveWord(self.wordEntry.get(), self.savedText, self.definitionBox)
        self.wordEntry.delete(0, tkinter.END)
    
    def __init__(self):
        self.action = BF.ButtonFunctions()
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
        scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)      #savedText is the text box/list of saved words obvi
        self.savedText = tkinter.Listbox(rightFrame, yscrollcommand = scrollbar.set)

        #start with previous list still there.
        self.initList()
        self.savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

        #this line makes the scrollbar actually work, the rest is build up/initializing   
        scrollbar.config(command = self.savedText.yview)

        #defined is the text box that hold definition / error message
        self.definitionBox = tkinter.Text(rightFrame)
        self.definitionBox.config(wrap=tkinter.WORD)
        self.definitionBox.insert(tkinter.INSERT, 'Definition here.')
        self.definitionBox.pack(side = tkinter.RIGHT)       
        
        #word entry and label
        wordLabel = tkinter.Label(leftFrame, text="Enter Word:", fg='cyan', bg='black')
        wordLabel.pack( anchor = tkinter.W)
        self.wordEntry = tkinter.Entry(leftFrame, bd =5)
        self.wordEntry.pack(anchor = tkinter.W)

        #create button to save
        saveButton = tkinter.Button(leftFrame, text="Save", command= lambda: self.saveButton())
        saveButton.pack(anchor = tkinter.W)
        #must put the location after you pack it.
        #saveButton.place(x=10, y=100)

        #delete button
        deleteButton = tkinter.Button(leftFrame, text="Delete", command= lambda: self.action.deleteWord(self.savedText))
        deleteButton.pack(anchor = tkinter.W)

        #search button
        searchButton = tkinter.Button(leftFrame, text="Online Def", command= lambda: self.action.searchOnline(self.savedText.get(self.savedText.curselection()), self.definitionBox))
        searchButton.pack(anchor = tkinter.W)

        #This code below will set up the word list for the random button
        randWord_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        randResponse = requests.get(randWord_site)
        WORDS = randResponse.content.splitlines()
        random.seed()
        #random search button
        randButton = tkinter.Button(leftFrame, text="Random", command= lambda: self.action.searchOnline(str(WORDS[random.randint(0, 25499)])[2:-1], self.definitionBox))
        randButton.pack(anchor = tkinter.W)

        #add button for random words?
        randButtonSave = tkinter.Button(leftFrame, text="Save Random", command= lambda: self.action.saveWord(str(WORDS[random.randint(0, 25499)])[2:-1], self.savedText, self.definitionBox))
        randButtonSave.pack(anchor = tkinter.W)

        top.mainloop()

#this is the line that runs it if you wanted to delete the dict.py file
#MainWindow()