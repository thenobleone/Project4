# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface


from graphics import *
import random
#from collections import Counter

# fucntion to determine number of black and white pegs
def ansCompare (master, guess):
    bCount = 0
    wCount = 0

    for i in range ( len(master)):
        if master[i] == guess [i]:
            bCount += 1

    for i in range (len (colorCount)):
        masterCount.append (master.count(colorCount[i]))
        guessCount.append (guess.count (colorCount[i]))

    for i in range (len (colorCount)):
        if masterCount[i] == 0 or guessCount[i] == 0:
            wCount += 0
        elif masterCount[i] > guessCount[i]:
            wCount += guessCount[i]
        elif masterCount[i] < guessCount[i]:
            wCount += masterCount[i]


    print ("guess:", guess)
    print ("white", wCount)
    print ("black", bCount)


#def drawGuess (win, guessColor)

#function to convert single letter inputs into the needed fill color values
def colorConvert (text):
    for i in range (len (text)):
        if text[i].lower () == 'o':
            text[i] = 'orange'
        elif text[i].lower () == 'r':
            text[i] = 'red'
        elif text[i].lower () == 'p':
            text[i] = 'purple'
        elif text[i].lower () == 'g':
            text[i] = 'green'
        elif text[i].lower () == 'y':
            text[i] = 'yellow'
        else:
            text[i] = 'blue'

    return text

# gets the user inputed color letters
def getGuess (win, info):
    color = []
    win.getMouse ()

    for i in range (len (info)):
        color.append (info[i].getText ())
    return color

# creates the 4 needed entry boxes
def entryBoxes (win, y):
    entryBox = [None]*4
    x = 8.5

    for i in range (4):
        entryBox[i] = Entry (Point (x, y), 4)
        entryBox[i].setText ('')
        entryBox[i].draw (win)
        x += 4

    return entryBox

# randomly creates the 4 color code to be guessed by the user
def masterCode ():
    masterColors = []
    colorList = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']

    for i in range (4):
        masterColors.append (random.choice(colorList))
    return masterColors

# creates the base window
def gameWindow ():
    win = GraphWin('Mastermind',700,700)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('gray')

    return win

#runs all the functions
def main():
    win = gameWindow ()
    #colorMasterList = masterCode ()
    colorMasterList = ['yellow', 'orange', 'yellow', 'red']
    print ("mc:", colorMasterList)
    boxes = entryBoxes (win, 3.5)
    guess = getGuess (win, boxes)
    colorGuessList = colorConvert (guess)
    results = ansCompare (colorMasterList, colorGuessList)

main()
