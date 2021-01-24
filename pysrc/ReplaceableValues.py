from .ListManager import *
from .HTMLManager import *


class ReplaceableValues:
    currentWord = getCurrentWord
    currentHelpWord = getCurrentHelpWord
    nextWord = getNextWord
    contentOfHTML = getContentOfHTML
    title = "Informatrix Random Word Generator"
    newRound = startNewRound
    newRoundButton = showNewRoundButton
