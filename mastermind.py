# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface

from graphics import *
import random

#
def revealSolution (master, win):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    mColor = [None] * 4
    x, y = 9, 28

    for i in range (len (master)):
        mColor[i] = Circle (Point (x, y), .75)
        mColor[i].setFill (master[i])
        mColor[i].draw (win)
        x += 4

# Function a pop up window indicating whether the user was able to correctly guess the master code or not
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

# Function sets peg colors to the indeed information
def drawPegs (black, white, peg, win):
    #runs 4 times, setting the fill colors as needed
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

    #bp == black peg iteration thru list of master color list
    for bp in range (len (master)):
        if guess[bp] == master[bp]:
            guess[bp] = 'black'
        else:
            #wp == white peg iteration comparing the value in master to the rest of the values in guess code
            for wp in range (len (master)):
                if master[bp] == guess[wp] and guess[wp] != 'black':
                    guess[wp] = 'white'

    # each count sends int value of each type of peg to function call
    return guess.count ('black'), guess.count ('white')

# Replaces the 4 entry boxes with 4 circles filled with the colors guessed by the user
def drawGuess (win, boxes, turn, color):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    x, y = 9, 3
    if turn > 0:
        y = y + (2 * turn)

    # Draws 4 cirlces
    for i in range (len (boxes)):
        boxes[i].undraw ()
        guessDot = Circle (Point (x,y), .75)
        guessDot.setFill (color[i])
        guessDot.draw (win)
        x += 4

#function to convert single letter inputs into the needed fill color strings
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
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    x, y = 6, 2.5
    if turn > 0:
        y = y + (3 * turn)

    #Creates 4 small cirlces to represent the information pegs
    for i in range (4):
        pegDot[i] = Circle (Point (x, y), .5)
        pegDot[i].setFill ('dimgray')
        pegDot[i].draw (win)

        # Adjusts the x & y values to create a 2 x 2 square of circles
        if i == 0 or i == 2:
            x += 1.25
        else:
            x -= 1.25
            y += 1.25

    # Sends a list with the circles for futher manipulation
    return pegDot

# Draws and creates entry boxes and sets them to a list that is returned to main
def entryBoxes (win, turn):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    entryBox = [None] * 4
    x, y = 9, 3
    if turn > 0:
        y = y + (2 * turn)

    # Creates 4 entry boxes for the user's guesses
    for i in range (4):
        entryBox[i] = Entry (Point (x, y), 4)
        entryBox[i].setText ('')
        entryBox[i].draw (win)
        x += 4

    # Sends a list with the circles for futher manipulation
    return entryBox

# randomly creates the 4 color code to be guessed by the user
def masterCode ():
    masterColors = []
    colorList = ['blue', 'green', 'orange', 'purple', 'red', 'yellow']

    # Creates a list of 4 random colors to be used as the master code for the user to guess
    for i in range (4):
        masterColors.append (random.choice (colorList))
    return masterColors

# Creates a submit button icon
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

#fucntion to clear graphic objects from the game window
def clearFeatures (feature):
    #tree to handle whether the graphic feature is a list of graphic objects or a single graphic object
    if type(feature) = list:
        for i in range (len (feature)):
            feature[i].undraw ()
    else:
        feature.undraw ()

#runs all the functions
def main():
    # Creates and setups the inital parameters needed for the game
    turnCount = 0
    gameWin = createWindow ()
    colorMasterList = masterCode ()
    print (colorMasterList) #<---- this line for testing only!!!

    # For loop set to the number of guesses a user is allowed
    for turnCount in range (10):
        pegCircles = createPegs (gameWin, turnCount)
        boxes = entryBoxes (gameWin, turnCount)
        guess = getGuess (gameWin, boxes)
        colorGuessList = colorConvert (guess, gameWin, turnCount)
        drawGuess (gameWin, boxes, turnCount, colorGuessList)
        bPeg, wPeg = ansCompare (list (colorMasterList), list (colorGuessList))

    # The decision tree determines whether the user has won, loss, or has another round of guessing
        if bPeg == 4:
            revealSolution (list (colorMasterList), gameWin)
            result = finishedCondition ('victory', gameWin)
            break
        elif turnCount == 9:
            result = finishedCondition ('lost', gameWin)
            break
        else:
            drawPegs (bPeg, wPeg, pegCircles, gameWin)

main()
