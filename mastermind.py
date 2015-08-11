# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface

from graphics import *
import random

def finishedCondition (score, win):
    popUp = Rectangle (Point (5, 10), Point (25, 20,))
    popUp.setFill ('lightskyblue')
    popUp.draw (win)

    message = Text (Point (15, 15), "")
    message.setStyle("bold")
    message.setSize (32)
    message.setTextColor ("white")

    if score == 'victory':
        message.setText ("!! Congrats You Win !!")
        message.draw (win)
    else:
        message.setText ("Sorry, you lose!")
        message.draw (win)


# fucntion to determine number of black and white pegs
def ansCompare (master, guess):
    bCount = 0
    wCount = 0

    for i in range (len (master)):
        if master[i] == guess[i]:
            guess[i] = 'black'
        else:
            for j in range (len (guess)):
                if master[j] == guess[i]:
                    guess[i] = 'white'
                    master[j] = 'white'

    return guess.count ('black'), guess.count ('white')

def drawGuess (win, boxes, turn, guessColor):
    x, y = 9, 3
    if turn > 0:
        y = y + (2 * turn)

    for i in range (len (boxes)):
        boxes[i].undraw ()
        guessDot = Circle (Point (x,y), .75)
        guessDot.setFill (guessColor[i])
        guessDot.draw (win)
        x += 4

#function to convert single letter inputs into the needed fill color values
def colorConvert (text, win, turn):
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
        elif text[i].lower () == 'b':
            text[i] = 'blue'
        else:
            entryBoxes (win, turn)

    return text

# gets the user inputed color letters
def getGuess (win, info):
    color = []
    win.getMouse ()

    for i in range (len (info)):
        color.append (info[i].getText ())
    return color

    # Figuring out way to set the click to the submit button area only
    #click = win.getMouse ()
    #x, y = click.getX (), click.getY ()
    #if x >=14 and x <= 16:
    #    if y <= 1.5 and y >= .5:
    #        for i in range (len (info)):
    #            color.append (info[i].getText ())
    #        return color
    #else:
    #    getGuess(win, info)

# creates the 4 needed entry boxes
def entryBoxes (win, turn):
    entryBox = [None]*4
    x, y = 9, 3
    if turn > 0:
        y = y + (2 * turn)

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
        masterColors.append (random.choice (colorList))
    return masterColors

# creates the base window
def createWindow ():
    win = GraphWin('Mastermind', 700, 700)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('tan')

    subButton = Rectangle (Point (14, 1.5), Point (16, .5))
    subButton.setFill ('lightgray')
    subButton.setOutline ('darkgray')
    subButton.draw (win)

    submit = Text (Point (15, 1), "Submit")
    submit.setFill ('black')
    submit.draw (win)
    return win

#runs all the functions
def main():
    turnCount = 0
    gameWin = createWindow ()
    colorMasterList = masterCode ()

    print ("mc:", colorMasterList)

    for turnCount in range (10):
        boxes = entryBoxes (gameWin, turnCount)
        guess = getGuess (gameWin, boxes)
        colorGuessList = colorConvert (guess, gameWin, turnCount)
        drawGuess (gameWin, boxes, turnCount, colorGuessList)
        bPeg, wPeg = ansCompare (list (colorMasterList), list (colorGuessList))

        if bPeg == 4:
            result = finishedCondition ('victory', gameWin)
            break
        elif turnCount == 9:
            result = finishedCondition ('lost', gameWin)
        else:
            givePegs ()

main()
