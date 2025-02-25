from tkinter import *
from tkinter import ttk

###
from appFunc import *

def newCards(data):
    category = getCategory()
    phraseList = getPhraseList(data, category)
    selection = genSelection(phraseList)
    phrase = getPhrase(phraseList, selection)

    czechList = getCzechList(data, category)
    answer = czechList[selection]
    guessList = generateGuessList(answer, czechList)
    phraseLabel.configure(text=phrase)
    guessButton0.configure(text=guessList[0])
    guessButton1.configure(text=guessList[1])
    guessButton2.configure(text=guessList[2])

    return answer, guessList

# DATA
data = getData()

# GUI
root = Tk()
root.title("English - Czech")

mainframe = ttk.Frame(root, borderwidth=5)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

phraseLabel = ttk.Label(mainframe)
phraseLabel.grid(column=2, row=1)

guessButton0 = ttk.Button(mainframe, command=lambda:[checkAnswer(answer, guessList[0]), newCards(data)])
guessButton0.grid(column=1, row=2)

guessButton1 = ttk.Button(mainframe, command=lambda:[checkAnswer(answer, guessList[1]), newCards(data)])
guessButton1.grid(column=2, row=2)

guessButton2 = ttk.Button(mainframe, command=lambda:[checkAnswer(answer, guessList[2]), newCards(data)])
guessButton2.grid(column=3, row=2)

answer, guessList = newCards(data)

root.mainloop()
