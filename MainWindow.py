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

    #def dropDownInit(self):
    #    self.selectedTheme = tkinter.StringVar()
    #    self.selectedTheme.set(self.themeNames[3]) #this one sets default theme

    def __init__(self):
        #self.themeNames = ["White", "Leprechaun Piss", "Cyan", "Magenta"]
        self.action = BF.ButtonFunctions()
        top = tkinter.Tk()
        top.title("Taylor Dictionary")
        top.geometry('500x300') # Size WxH

        #need frames to make it pretty and organized
        leftFrame = tkinter.Frame(top)

        #rightframe handles the list and scrollbar
        rightFrame = tkinter.Frame(top)
        
        #scrollbar is for my list of saved words
        scrollbar = tkinter.Scrollbar(rightFrame)

        #savedText is the text box/list of saved words obvi
        self.savedText = tkinter.Listbox(rightFrame, yscrollcommand = scrollbar.set)
        #start with previous list still there.
        self.initList()

        #this line makes the scrollbar actually work, the rest is build up/initializing   
        scrollbar.config(command = self.savedText.yview)

        #defined is the text box that hold definition / error message
        self.definitionBox = tkinter.Text(rightFrame)
        self.definitionBox.config(wrap=tkinter.WORD)
        self.definitionBox.insert(tkinter.INSERT, 'Definition here.')      
        
        #word entry and label
        wordLabel = tkinter.Label(leftFrame, text="Enter Word:",)
        self.wordEntry = tkinter.Entry(leftFrame, bd =5)

        #create button to save
        saveButton = tkinter.Button(leftFrame, text="Save", command= lambda: self.saveButton())

        #delete button
        deleteButton = tkinter.Button(leftFrame, text="Delete", command= lambda: self.action.deleteWord(self.savedText))

        #search button
        searchButton = tkinter.Button(leftFrame, text="Online Def", \
                            command= lambda: self.action.searchOnline(self.savedText.get(self.savedText.curselection()), self.definitionBox))
        

        #This code below will set up the word list for the random button
        randWord_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        randResponse = requests.get(randWord_site)
        WORDS = randResponse.content.splitlines()
        random.seed()

        #random search button
        randButton = tkinter.Button(leftFrame, text="Random", command= lambda: self.action.searchOnline(str(WORDS[random.randint(0, 25499)])[2:-1], self.definitionBox))

        #add button for random words?
        randButtonSave = tkinter.Button(leftFrame, text="Save Random", command= lambda: self.action.saveWord(str(WORDS[random.randint(0, 25499)])[2:-1], self.savedText, self.definitionBox))

        #Menu
        #self.dropDownInit()
        #Menu = tkinter.OptionMenu(leftFrame, self.selectedTheme, *self.themeNames, command= lambda : self.action.ChangeColor(self.selectedTheme.get(), top, leftFrame, rightFrame, wordLabel, self.savedText, self.definitionBox))

        #Other Menu?
        menuBar = tkinter.Menu(top)
        themesMenu = tkinter.Menu(menuBar, tearoff=0)
        themesMenu.add_command(label="White", command= lambda : self.action.ChangeColor("White", top, leftFrame, rightFrame, wordLabel, self.savedText, self.definitionBox))
        themesMenu.add_command(label="Leprechaun Piss", command= lambda : self.action.ChangeColor("Leprechaun Piss", top, leftFrame, rightFrame, wordLabel, self.savedText, self.definitionBox))
        themesMenu.add_command(label="Cyan", command= lambda : self.action.ChangeColor("Cyan", top, leftFrame, rightFrame, wordLabel, self.savedText, self.definitionBox))
        themesMenu.add_command(label="Magenta", command= lambda : self.action.ChangeColor("Magenta", top, leftFrame, rightFrame, wordLabel, self.savedText, self.definitionBox))
        menuBar.add_cascade(label="Themes", menu=themesMenu)

        #packing section
        leftFrame.pack(side = tkinter.LEFT)
        rightFrame.pack(side=tkinter.RIGHT)
        scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y) 
        self.savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
        self.definitionBox.pack(side = tkinter.RIGHT)
        #Menu.pack(side = tkinter.TOP)
        wordLabel.pack( anchor = tkinter.W)
        self.wordEntry.pack(anchor = tkinter.W)
        saveButton.pack(anchor = tkinter.W)
        deleteButton.pack(anchor = tkinter.W)
        searchButton.pack(anchor = tkinter.W)
        randButton.pack(anchor = tkinter.W)
        randButtonSave.pack(anchor = tkinter.W)

        top.config(menu=menuBar)
        top.mainloop()


#this is the line that runs it if you wanted to delete the dict.py file
#MainWindow()