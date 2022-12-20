'''
    Dice Bag System
    Anthony Castillo
    12/18/2022
'''

from abc import abstractmethod
from abc import ABC

class NodeAbstract(ABC):
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def __str__(self):
        pass

    def clear(self):
        pass

    def getKey(self):
        pass

    def getValue(self):
        pass

    def getNext(self):
        pass

    def setKey(self, key):
        pass

    def setValue(self, value):
        pass

    def setNext(self, next):
        pass
# end NodeAbstract()

class LinkedListAbstract(ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass

    def __contains__(self, key):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, dice):
        pass

    def append(self, dice):
        pass

    def remove(self, key):
        pass

    def clear(self):
        pass
# end LinkedListAbstract()

class DiceAbstract(ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    def getFaces(self):
        pass

    def getPreviousRoll(self):
        pass

    def getName(self):
        pass

    def setFaces(self, number):
        pass

    def rollDice(self):
        pass
# end DiceAbstract()

class BagOfDiceAbstract(ABC):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    def getPreviousRoll(self):
        pass

    def getHistory(self):
        pass

    def addDice(self, faces):
        pass

    def standardDiceSet(self):
        pass
    
    def rollDice(self, diceFaces = None, quantity = None):
        pass

    def help(self):
        pass
# end BagOfDice()