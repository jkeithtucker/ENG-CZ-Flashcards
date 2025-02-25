import pandas as pd
import numpy as np
from random import randint, shuffle

categories = \
    {
        0:'BASIC',
        1:'BASIC QUESTIONS',
        2:'FOOD',
        3:'COOKING',
        4:'SHOP/RESTAURANT',
        5:'SHOP/RESTAURANT QUESTIONS',
    }


def getCategory():
    category = categories[randint(0, 5)]
    return category


def getData():
    langData = pd.read_csv('EngCz.csv', encoding="cp1250")
    return langData


def getPhraseList(langData, category):
    categoryData = langData[category]
    presentData = pd.notnull(categoryData)
    phraseList = categoryData[presentData].to_list()
    return phraseList


def genSelection(phraseList):
    selection = randint(0, len(phraseList) - 1)
    return selection

def getPhrase(phraseList, selection):
    phrase = phraseList[selection]
    return phrase


def getCzechList(langData, category):
    czechColumn = category + str(" CZ")
    czechData = langData[czechColumn]
    presentCzechData = pd.notnull(czechData)
    czechList = czechData[presentCzechData].to_list()
    return czechList


def generateGuessList(answer, czechList):
    list = [answer, ]
    while len(list) < 3:
        index = randint(0, len(czechList) - 1)
        if czechList[index] == answer:
            continue
        elif czechList[index] in list:
            continue
        else:
            list.append(czechList[index])
    shuffle(list)
    return list

def checkAnswer(answer, userInput):
    if answer == userInput:
        print("Correct!")
    else:
        print("Incorrect!")

