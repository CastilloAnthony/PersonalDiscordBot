'''
    Dice Bag System
    Anthony Castillo
    12/18/2022
'''

from abstractClasses_Dice import LinkedListAbstract, NodeAbstract, DiceAbstract, BagOfDiceAbstract
import random

class BagOfDice(BagOfDiceAbstract):
    def __init__(self):
        self.__diceList = LinkedList_Dice()
        self.__previousDice = 'd6'
        self.__history = []

    def __del__(self):
        del self.__diceList

    def __str__(self):
        return str(self.__diceList)

    def getPreviousRoll(self): # Gets the most recent dice roll
        return self.__diceList[self.__previousDice].getPreviousRoll()

    def getHistory(self):
        return self.__history

    def addDice(self, faces): # Adds a dice to the bag
        newDice = Dice()
        if (newDice.setFaces(faces)):
            if (newDice.getName() in self.__diceList): # We don't want duplicates
                return False 
            else:
                if (self.__diceList.append(newDice)):
                    return True
                else:
                    return False
        else: 
            return False 

    def removeDice(self, faces):
        name = 'd' + str(faces)
        return self.__diceList.remove(name)

    def emptyBag(self):
        return self.__diceList.clear()

    def standardDiceSet(self): # Adds the standard DnD dice to the bag.
        self.addDice(4)
        self.addDice(6)
        self.addDice(8)
        self.addDice(10)
        self.addDice(12)
        self.addDice(20)

    def rollDice(self, faces = None, quantity = None): # Rolls a dice multiple times or rolls a d6 (multiple times)
        if (quantity != None):
            results = []
            if (faces != None):
                dice = 'd' + str(faces)
                if (dice in self.__diceList):
                    for i in range(0,quantity):
                        results.append(self.__diceList[dice].rollDice())
                    self.__previousDice = dice
                    self.__history.append(results)
                    return results
                else:
                    for i in range(0,quantity):
                        results.append(self.__diceList['d6'].rollDice())
                    self.__previousDice = 'd6'
                    self.__history.append(results)
                    return results
            else:
                for i in range(0,quantity):
                    results.append(self.__diceList['d6'].rollDice())
                self.__previousDice = 'd6'
                self.__history.append(results)
                return results
        elif (faces != None):
            dice = 'd' + str(faces)
            self.__previousDice = dice
            value = self.__diceList[dice].rollDice()
            self.__history.append(value)
            return value
        else:
            self.__previousDice = 'd6'
            value = self.__diceList['d6'].rollDice()
            self.__history.append(value)
            return value

    def help(self): # Returns a string of the list of commands for the bag of dice
        information = 'getPreviousRoll() - Retrieves the last rolled dice\'s value. \ngetHistory() - Returns a list of all the dice roll results that have been rolled in this bag. \naddDice(faces) - Adds a new dice with the the quantity of faces, cannot add multiple of the same dice. \nremoveDice(name) - Removes the specified dice from the bag. \nemptyBag() - Empties the entire bag. \nstandardDiceSet() - Adds the standard DnD dice set to the bag. \nrollDice(faces, quantity) - Rolls a dice with the requested number of faces the quantity of times. \nhelp() - Displays this help message.'
        return information
# end BagOfDice()

class Dice(DiceAbstract):
    def __init__(self):
        self.__faces = 6
        self.__name = 'd' + str(self.__faces)
        self.__value = 0

    def __del__(self):
        del self.__name
        del self.__faces
        del self.__value

    def __str__(self):
        information = self.__name + '\'s last roll was a ' +  str(self.__value)
        return information

    def getFaces(self):
        return self.__faces

    def getPreviousRoll(self):
        return self.__value

    def getName(self):
        return self.__name

    def setFaces(self, number):
        if (isinstance(number, int)):
            self.__faces = number
            self.__name = 'd' + str(self.__faces)
            return True
        else:
            return False

    def rollDice(self):
        self.__value = random.randint(1, self.__faces)
        return self.__value
# end Dice()

class Node(NodeAbstract):
    def __init__(self):
        self.__key = None
        self.__value = None
        self.__next = None
    
    def __del__(self):
        self.clear()
        del self.__next
        del self.__value
        del self.__key

    def __str__(self):
        return str(self.__value)

    def clear(self):
        self.__key = None
        self.__value = None
        self.__next = None

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def getNext(self):
        return self.__next

    def setKey(self, key):
        self.__key = key

    def setValue(self, value):
        self.__value = value

    def setNext(self, next):
        self.__next = next
# end NodeAbstract()

class LinkedList_Dice(LinkedListAbstract):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def __del__(self):
        self.clear()
        del self.__tail
        del self.__head
        del self.__size

    def __len__(self):
        return self.__size

    def __str__(self):
        current = self.__head
        information = ''
        while (current != None):
            if (current.getNext() == None):
                information = information + str(current.getValue())
                break
            information = information + str(current.getValue()) + ', '
            current = current.getNext()
        return information

    def __contains__(self, key):
        current = self.__head
        while (current != None):
            if (current.getKey() == key):
                return True
            current = current.getNext()
        return False

    def __getitem__(self, key):
        current = self.__head
        while (current != None):
            if (current.getKey() == key):
                return current.getValue()
            current = current.getNext()
        return None

    def __setitem__(self, dice):
        newNode = Node()
        newNode.setKey(dice.getName())
        newNode.setValue(dice)
        if (self.__head == None):
            self.__head = newNode
            return True
        else:
            newNode.setNext(self.__head)
            self.__head = newNode
            return True
        return False

    def append(self, dice):
        newNode = Node()
        newNode.setKey(dice.getName())
        newNode.setValue(dice)
        if (self.__head == None):
            self.__head = newNode
            self.__size = self.__size + 1
            return True
        else:
            newNode.setNext(self.__head)
            self.__head = newNode
            self.__size = self.__size + 1
            return True
        return False

    def remove(self, name):
        current = self.__head
        previous = current
        while (current != None):
            if (current.getValue().getName() == name):
                previous.setNext(current.getNext())
                del current
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def clear(self):
        while (self.__head != None):
            temp = self.__head
            self.__head = temp.getNext()
            del temp
        return True
