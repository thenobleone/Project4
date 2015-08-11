# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface

from graphics import *
import random

def revealSolution (master, win):
    mColor = [None] * 4
    x, y = 9, 28

    for i in range (len (master)):
        mColor[i] = Circle (Point (x, y), .75)
        mColor[i].setFill (master[i])
        mColor[i].draw (win)
        x += 4

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

def drawPegs (black, white, peg, win):
    print ("black", black)
    print ("white", white)

    for i in range (len (peg)):
        if black > 0:
            peg[i].setFill ('black')
            black -= 1
        elif white > 0:
            peg[i].setFill ('white')
            white -= 1

# fucntion to determine number of black and white pegs
def ansCompare (master, guess):
    bCount = 0
    wCount = 0

    for i in range (len (guess)):
        if guess[i] == master[i]:
            guess[i] = 'black'
        else:
            for j in range (len (guess)):
                if master[j] == guess[i] and guess[i] != 'black':
                    guess[i] = 'white'
                print ("g{0} = {1}".format (i, guess))
                print ("m{0} = {1}".format (i, master))

    return guess.count ('black'), guess.count ('white')

def drawGuess (win, boxes, turn, color):
    x, y = 9, 3
    if turn > 0:
        y = y + (2 * turn)

    for i in range (len (boxes)):
        boxes[i].undraw ()
        guessDot = Circle (Point (x,y), .75)
        guessDot.setFill (color[i])
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

# Create 4 pegs
def createPegs (win, turn):
    pegDot = [None] * 4
    x, y = 6, 2.5
    if turn > 0:
        y = y + (3 * turn)

    for i in range (4):
        pegDot[i] = Circle (Point (x, y), .5)
        pegDot[i].setFill ('dimgray')
        pegDot[i].draw (win)
        if i == 0 or i == 2:
            x += 1.25
        else:
            x -= 1.25
            y += 1.25
    return pegDot

# creates the 4 needed entry boxes
def entryBoxes (win, turn):
    entryBox = [None] * 4
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

# Creates submit button
def createButton (win):
    subButton = Rectangle (Point (14, 1.5), Point (16, .5))
    subButton.setFill ('lightgray')
    subButton.setOutline ('darkgray')
    subButton.draw (win)

    submit = Text (Point (15, 1), "Submit")
    submit.setFill ('black')
    submit.draw (win)

# creates the base window
def createWindow ():
    win = GraphWin('Mastermind', 700, 700)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('tan')
    return win

#runs all the functions
def main():
    turnCount = 0
    gameWin = createWindow ()
    colorMasterList = masterCode ()
    print (colorMasterList)

    for turnCount in range (10):
        pegCircles = createPegs (gameWin, turnCount)
        boxes = entryBoxes (gameWin, turnCount)
        guess = getGuess (gameWin, boxes)
        colorGuessList = colorConvert (guess, gameWin, turnCount)
        drawGuess (gameWin, boxes, turnCount, colorGuessList)
        bPeg, wPeg = ansCompare (list (colorMasterList), list (colorGuessList))

        if bPeg == 4:
            revealSolution (list (colorMasterList), gameWin)
            result = finishedCondition ('victory', gameWin)
            break
        elif turnCount == 9:
            result = finishedCondition ('lost', gameWin)
        else:
            drawPegs (bPeg, wPeg, pegCircles, gameWin)

main()
