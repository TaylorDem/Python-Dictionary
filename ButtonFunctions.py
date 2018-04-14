import tkinter
from tkinter import messagebox
import requests
import bs4  #beautifulsoup4



class ButtonFunctions():
    
    #this function is the save button command
    def saveWord(self, wordToSave, savedText, definitionBox):
        #i wanna check to see if the word is already there.
        dupe = False
        for x in range(0, savedText.size()):
            if savedText.get(x) == wordToSave:
                dupe = True

        if dupe == False: #if not already there save
            savedText.insert(savedText.size(), wordToSave)
            self.sortAZ(savedText)
            savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

            #opens .txt file to save
            text_file = open("Current_Dict.txt", "w") #a lets you append instead
            #Now this bit will save word list to a .txt file
            for x in range(0, savedText.size()):
                text_file.write("%s\n" % (savedText.get(x)))
            text_file.close()

        if dupe == True: #show error message in definition box for now
            definitionBox.delete(1.0, tkinter.END)
            definitionBox.config(fg = 'red')
            definitionBox.insert(tkinter.INSERT, "That word already exists in the dictionary!")
            definitionBox.pack(side = tkinter.BOTTOM)

    #search function
    def searchOnline(self, word, definitionBox):
        dictionaryurl = 'http://www.dictionary.com/browse/' + word + '?s=t'
        searchWord = requests.get(dictionaryurl)
        #this line clears old text
        definitionBox.delete(1.0, tkinter.END) #it was a hassle here. 1.0 is very important!
        #this line below makes it legible
        parsedText = bs4.BeautifulSoup(searchWord.text, 'html.parser')
        #the site dictionary.com has the definition in the 'meta' tag on its site with the name description 
        definition = parsedText.find('meta', attrs={'name':'description'})
        definitionBox.insert(tkinter.INSERT, definition["content"][:-10])   #this pulls content out of it.args
        #each content on the site ends with " see more." so with   ^^^^ I delete the last 10 characters
        definitionBox.config(fg='black')
        definitionBox.pack(side = tkinter.BOTTOM)
    
   
    #alphabetize function
    def sortAZ(self, savedText):
        #pull whole list
        temp_list = list(savedText.get(0, tkinter.END))
        #apparently sorting is inherent with lists
        temp_list.sort(key=str.lower)
        #delete contents of present listbox
        savedText.delete(0, tkinter.END)
        #load listbox with sorted data
        for item in temp_list:
            savedText.insert(tkinter.END, item)

    #delete function
    def deleteWord(self, savedText):
        if messagebox.askokcancel("Confirm", "You sure this isn't a word?"):
            markedWord = savedText.get(savedText.curselection()) #put the word here for legibility
    
            #this first bit here opens and reads the file
            text_file = open("Current_Dict.txt","r")
            words = text_file.readlines()
            text_file.close()
    
            #now rewriting file to contain every line except the deleted one
            text_file = open("Current_Dict.txt", "w")
            for line in words:
                if line != markedWord+"\n":
                    text_file.write(line)
            text_file.close()
    
            #now delete the visual one
            savedText.delete(savedText.curselection())
            savedText.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

    #this is the Menu button function that is ran 
    def ChangeColor(self, chosenTheme, top, leftFrame, rightFrame, wordLabel, listBox, definitionBox):
        #self.top.config(fg='cyan') #there is no foreground on frames for the root?
        print("value of selection is " + chosenTheme)
        if chosenTheme == 'Cyan':
            top.configure(bg='black')
            leftFrame.configure(bg='black')
            rightFrame.configure(bg='black')
            wordLabel.configure(bg='black', fg='cyan')
            listBox.configure(bg='black')
            listBox.configure(fg='cyan')
            definitionBox.configure(bg='black')
            definitionBox.configure(fg='cyan')
        elif chosenTheme == 'White':
            top.configure(bg='black')
            leftFrame.configure(bg='black')
            rightFrame.configure(bg='black')
            wordLabel.configure(bg='black', fg='white')
            listBox.configure(bg='black')
            listBox.configure(fg='white')
            definitionBox.configure(bg='black')
            definitionBox.configure(fg='white')
        elif chosenTheme == 'Leprechaun Piss':
            top.configure(bg='black')
            leftFrame.configure(bg='black')
            rightFrame.configure(bg='black')
            wordLabel.configure(bg='black', fg='green')
            listBox.configure(bg='black')
            listBox.configure(fg='green')
            definitionBox.configure(bg='black')
            definitionBox.configure(fg='green')
        elif chosenTheme == 'Magenta':
            top.configure(bg='black')
            leftFrame.configure(bg='black')
            rightFrame.configure(bg='black')
            wordLabel.configure(bg='black', fg='magenta')
            listBox.configure(bg='black')
            listBox.configure(fg='magenta')
            definitionBox.configure(bg='black')
            definitionBox.configure(fg='magenta')
    