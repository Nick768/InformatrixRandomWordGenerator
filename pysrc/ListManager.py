from os import getcwd
from random import shuffle
from .PathManager import *


def createList():
    try:
        list = []
        file = open(getcwd() + '/WordList.txt', 'r')
        lines = file.readlines()
        for line in lines:
            list.append(line.replace('\n', '').split(','))
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
    global helpWordIndex
    try:
        if list[wordIndex].__len__() > 1:
            helpWordIndex += 1
            return list[wordIndex][helpWordIndex - 1]
    except:
        pass
    return "Kein Hilfswort vorhanden!"


def getNextWord():
    from .HTTPServer import requestedPath
    global wordIndex, helpWordIndex
    if requestedPath == "/nextWord/":
        wordIndex += 1
        helpWordIndex = 1
    return ""


def startNewRound():
    from .HTTPServer import requestedPath
    global wordIndex, helpWordIndex, list
    if requestedPath == "/newRound/":
        wordIndex = 0
        helpWordIndex = 1
        shuffle(list)
    return ""
