# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface

from graphics import *
import random
from button import Button

def quitGame(ndow):
    quitButton = Button(ndow,Point(3,1),6,2, "Quit")
    quitButton.activate()
    pt = ndow.getMouse()
    if quitButton.clicked(pt):
            ndow.close()

def submitButton(win):
    submit = Button(win,Point(14.5,1),17,2, "Submit Your Answer")
    submit.activate()
    pt = win.getMouse()
    if submit.clicked(pt):
        return submit

# Graphic that 'hides' the mastercode from the user at the top of the board.
#       note: This is only a graphic to give the impression that the colors
#       are 'hidden'.
def masterBoard(g):
    hideMasterKey = Oval(Point(6,26),Point(23,29))
    hideMasterKey.draw(g)
    hideMasterKey.setFill("steelblue3")
    hideMasterKey.setWidth(3)
    hideMasterKey.setOutline("ivory")
    return hideMasterKey

def revealSolution (master, win):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    mColor = [None] * 4
    x, y = 8.5, 27.9

    for i in range (len (master)):
        mColor[i] = Circle (Point (x, y), .75)
        mColor[i].setFill (master[i])
        mColor[i].draw (win)
        x += 4

# Function a pop up window indicating whether the user was able to correctly guess the master code or not
def finishedCondition (score, win):

    popUp = Rectangle (Point (6,27), Point (23, 26))
    popUp.draw (win)

    message = Text (Point (15, 26.56), "")
    message.setFace("arial")
    message.setSize (20)

    if score == 'victory':
        message.setText ("!! Congratulations, You Win !!")
        message.setTextColor("yellow")
        popUp.setFill("navy")
        message.draw (win)
    else:
        message.setText ("Sorry, You Lose!")
        message.setTextColor("red")
        popUp.setFill("black")
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

    # For loop to determine all blacks first!
    for bp in range (len (master)):
        if guess[bp] == master[bp]:
            master[bp] = ''
            guess[bp] = 'black'

    # Second loop to determine white pegs AFTER ensure there are no black pegs
    #bp == black peg iteration thru list of master color list
    for bp in range (len (master)):
        #wp== wp peg iteration thru list of master color list
        for wp in range (len (master)):
            if master[bp] == guess[wp] and guess[wp] != 'black':
                master[bp] = ''
                guess[wp] = 'white'

    # each count sends int value of each type of peg to function call
    return guess.count ('black'), guess.count ('white')

# Replaces the 4 entry boxes with 4 circles filled with the colors guessed by the user
def drawGuess (win, boxes, turn, color):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    x, y = 8.5, 3.5
    if turn > 0:
        y = y + (3 * turn)

    # Draws 4 circles
    for i in range (len (boxes)):
        boxes[i].undraw ()
        guessDot = Circle (Point (x,y), .75)
        guessDot.setFill (color[i])
        guessDot.setOutline("azure")
        guessDot.draw (win)
        x += 4

#function to convert single letter inputs into the needed fill color strings
def colorConvert (text, win, turn):
    for i in range (len (text)):
        if text[i].lower () == 'o':
            text[i] = 'orangered'
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

# 4 pegs that tell user "B" or "W"
def createPegs (win, turn):
    pegDot = [None] * 4
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    x, y = 3.4, 2.80
    if turn > 0:
        y = y + (3 * turn)

    #Creates 4 small cirlces to represent the information pegs
    for i in range (4):
        pegDot[i] = Circle (Point (x, y), .5)
        pegDot[i].setFill ('azure4')
        pegDot[i].setOutline("azure")
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
    x, y = 8.5, 3.5
    if turn > 0:
        y = y + (3 * turn)
    # Creates 4 entry boxes for the user's guesses
    for i in range (4):
        entryBox[i] = Entry (Point (x, y), 3)
        entryBox[i].setSize(22)
        entryBox[i].setFill("azure")
        entryBox[i].setText ('')
        entryBox[i].draw (win)
        x += 4
    # Sends a list with the circles for futher manipulation
    return entryBox

# randomly creates the 4 color code to be guessed by the user
def masterCode ():
    masterColors = []
    colorList = ['blue', 'green', 'orangered', 'purple', 'red', 'yellow']
    # Creates a list of 4 random colors to be used as the master code for the user to guess
    for i in range (4):
        masterColors.append (random.choice (colorList))
    return masterColors

# Creates a submit button icon
###################################
### NOT IN USE AT THIS TIME ####
def createButton (win):
    subButton = Rectangle (Point (6, 1.75), Point (23, .25))
    subButton.setFill ('azure')
    subButton.setOutline ('dodgerblue3')
    subButton.draw (win)

    submit = Text (Point (15, 1), "Submit")
    submit.setSize(20)
    submit.setStyle("bold")
    submit.setFace("arial")
    submit.setFill ('dodgerblue3')
    submit.draw (win)


 #### Far Right LINE SECTIONS ####
def rightLines(gameW):
        # Vertical lines
        fRvL1 = Line(Point(25,2),Point(25,26))
        fRvL1.setFill("ivory")
        fRvL1.setWidth(1)
        fRvL1.draw(gameW)
        fRvL2 = Line(Point(23,2),Point(23,29))
        fRvL2.setFill("ivory")
        fRvL2.setWidth(2.5)
        fRvL2.draw(gameW)
        # Horizontal Lines
        x,y = 23,-3
        x1, y1 = 23,5
        x2, y2 = 28,5
        # Loop the creates lines on far right side
        for i in range(8):
            farRightHorzLines = Line(Point(x1,y1),Point(x2,y2))
            farRightHorzLines.setFill("ivory")
            farRightHorzLines.setWidth(5)
            farRightHorzLines.draw(gameW)
            y+=3
            farRightHorzLines.move(0,y)


#####NUMBERS FOR FR SECTION
def Numbers(gameWind):
          x,y = 21,-3
          x1,y1 = 24,3.5
          # loop to generate numbers on right side of board
          for i in range(1,9):
              numbers = Text(Point(x1,y1),[i])
              numbers.setFace("arial")
              numbers.setTextColor("azure3")
              numbers.setSize(25)
              numbers.draw(gameWind)
              y+=3
              numbers.move(0,y)

# Colorful ball game key with letters to indicate which letter represents
#       which color.
def ballGraphics(gaWin):
    colorGuide = [['blue', 'B'], ['green', 'G'], ['orangered', 'O'], ['purple', 'P'], ['red', 'R'], ['yellow', 'Y']]
    x, y = 26.6, 3.5

    for c in range (len (colorGuide)):
        kBall = Circle (Point (x, y), .8)
        kText = Text (Point (x, y), '')
        kText.setSize(20)
        kText.setFace("arial")
        kBall.draw (gaWin)
        kBall.setFill (colorGuide[c][0])
        kBall.setOutline (colorGuide[c][0])
        kText.setText (colorGuide[c][1])
        kText.draw(gaWin)
        y += 3


# Black and White pegs on Right Side of board with info.
def info(gameW):
    infoList = ["Right Color","Right Place", "Wrong Color"]
    EB = Circle(Point(26.5,22.25),.3)
    EB.draw(gameW)
    EB.setFill("black")

    EW = Circle(Point(26.5,25.25),.3)
    EW.draw(gameW)
    EW.setFill("white")
    EW.setOutline("white")

    ebText1 = Text(Point(26.5,21),infoList[0]+"\n"+infoList[1])
    ebText1.draw(gameW)
    ebText1.setFace("arial")
    ebText1.setSize(11)

    ewText2 = Text(Point(26.5,24),infoList[0]+"\n"+infoList[2])
    ewText2.setFace("arial")
    ewText2.setTextColor("white")
    ewText2.draw(gameW)
    ewText2.setSize(11)


# FAR LEFT SIDE GRID and VERTICAL LINES
def leftLines(gaW):
    # Vertical Lines on Far left
    vLfL = Line(Point(6,2),Point(6,29))
    vLfL.setFill("ivory")
    vLfL.setWidth(2.5)
    vLfL.draw(gaW)
    x,y = 2,-3
    x1,y1 = 2,5
    x2,y2 = 6,5
    for i in range(8):
        leftLines = Line(Point(2,5),Point(6,5))
        leftLines.setFill("ivory")
        leftLines.setWidth(5)
        leftLines.draw(gaW)
        y+=3
        leftLines.move(0,y)

# FAR LEFT SIDE-- 4 hole GREY CLUE graphic drawn in vertically.
def cluePegBoard(window):
    x,y = 0,-2
    xA, yA = 3.4,5.83
    x1,y1 = 2,4
    x2,y2 = 6,7
    for i in range(1,8):
        for i in range(4):
            pegHole = Circle(Point(xA,yA),.5)
            pegHole.draw(window)
            pegHole.setFill("azure4")
            pegHole.setOutline("azure")
            if i == 1 or i == 3:
                pegHole.move(1.25,0)
            if i == 2 or i == 3:
                pegHole.move(0,1.25)
        y+=3
        yA+=3

#######################################################
# guessBoard and GuessBoard2 draw the circle graphics in the middle
#       of the board.
# Vertical CENTER guess pegs on far left side- graphics only
def guessBoard(gam):
    x,y = 8.5,5.5
    y1,x1 = 1,1
    for i in range(7):
        board = Circle(Point(x,y),.75)
        board.draw(gam)
        board.setFill("azure3")
        board.setOutline("ivory")
        board.move(0,y1)
        y1+=3
    return board

# Horizontal CENTER guess pegs - graphics only-
def GuessBoard2(w,v):
    x,y= 12.5, 6.5
    x1 = 0
    for i in range(7):
        for i in range(3):
            boardH = Circle(Point(x,y),.75)
            boardH.draw(w)
            boardH.setFill("azure3")
            boardH.setOutline("ivory")
            boardH.clone()
            boardH.move(x1,0)
            x1+=4
        y = y+3
        x1 = x1 - x1

# BACKGROUND PICTORIAL SPACE
def background(gW):
    background = Rectangle(Point(2,29),Point(28,2))
    background.setWidth(5)
    background.setOutline("ivory3")
    background.draw(gW)
    background.setFill("steelblue")

# Creates the base window
def createWindow ():
    win = GraphWin('Mastermind', 700, 700)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('royalblue4')
    return win

#runs all the functions
def main():
    # Creates and setups the inital parameters needed for the game
    turnCount = 0
    gameWin = createWindow ()
    #functions for graphics
    background(gameWin)
    rightLines(gameWin)
    leftLines(gameWin)
    info(gameWin)
    Numbers(gameWin)
    cluePegBoard(gameWin)
    ballGraphics(gameWin)

    #createBalls = ballGraphs(gameWin)
    middleVertical = guessBoard(gameWin)
    middleHorz = GuessBoard2(gameWin,middleVertical)
    hideMaster = masterBoard(gameWin)
    colorMasterList = masterCode ()
 #   createQuit = quitGame(gameWin) <------------#### NEEDS WORK
#    submit = submitButton(gameWin)< ----------- ### NEEDS WORK



    print (colorMasterList) #<---- this line for testing only!!!
        #    For loop set to the number of guesses a user is allowed
    for turnCount in range (8):
        submit = createButton(gameWin)
        pegCircles = createPegs (gameWin, turnCount)
        boxes = entryBoxes (gameWin, turnCount)
        guess = getGuess (gameWin, boxes)
        colorGuessList = colorConvert (guess, gameWin, turnCount)
        drawGuess (gameWin, boxes, turnCount, colorGuessList)
        bPeg, wPeg = ansCompare (list (colorMasterList), list (colorGuessList))
 #       createQuit = quitGame(gameWin) < -------- NEEDS WORK
#        submit = submitButton(gameWin)<----------NEEDS WORK

        # The decision tree determines whether the user has won, loss, or has another round of guessing
        if bPeg == 4:
            hideMaster.undraw()
            revealSolution (list (colorMasterList), gameWin)
            result = finishedCondition ('victory', gameWin)
            break
        elif turnCount == 7:
            hideMaster.undraw()
            revealSolution (list (colorMasterList), gameWin)
            result = finishedCondition ('lost', gameWin)
            break
        else:
            drawPegs (bPeg, wPeg, pegCircles, gameWin)



main()
