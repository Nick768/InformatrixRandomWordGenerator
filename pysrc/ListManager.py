from os import getcwd
from random import shuffle

def createList():                                                                                             
    try:                         
        list = []                   
        file = open(getcwd() + '/WordList.txt', 'r')
        lines = file.readlines()
        for line in lines:
            list.append(line.replace('\\n', '').split(','))
        file.close()
        shuffle(list)
        return list
    except:                                                                                             
        return [["Keine Liste vorhanden!"]]

list = createList()
wordIndex = 0
helpWordIndex = 1

def getCurrentWord():
    try:
        return list[wordIndex][0]
    except:
        return "Kein weiteres Wort vorhanden!"

def getCurrentHelpWord():
    try:
        if list[wordIndex].__len__() > 1:
            return list[wordIndex][helpWordIndex]
        return "Kein Hilfswort vorhanden!"
    except:
        return "Kein Hilfswort vorhanden!"

def getNextWord():
    global wordIndex
    wordIndex += 1
    try:
        return getCurrentWord()
    except:
        return "Kein weiteres Wort vorhanden!"