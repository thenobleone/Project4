# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

# Program design to recreate the game Mastermind with a GUI interface

from graphics import *
import random

def revealSolution (master, win):
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    mColor = [None] * 4
    x, y = 8.5, 28

    for i in range (len (master)):
        mColor[i] = Circle (Point (x, y), .75)
        mColor[i].setFill (master[i])
        mColor[i].draw (win)
        x += 4

# Function a pop up window indicating whether the user was able to correctly guess the master code or not
def finishedCondition (score, win):

    popUp = Rectangle (Point (6,27), Point (23, 26))
    popUp.setFill("black")
    popUp.draw (win)

    message = Text (Point (15, 26.56), "")
    message.setFace("arial")
    message.setSize (20)
    message.setTextColor ("navy")

    if score == 'victory':
        message.setText ("!! Congrats You Win !!")
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
        guessDot = Circle (Point (x,y), .80)
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
    # ENTRY BOXES
    # Sets the base x and y coordinate values, uses the turn count to increase the y value so that it's on a newline
    entryBox = [None] * 4
    x, y = 8.5, 3.5
    if turn > 0:
        y = y + (3 * turn)

    # Creates 4 entry boxes for the user's guesses
    for i in range (4):
        entryBox[i] = Entry (Point (x, y), 4)
        entryBox[i].setSize(17)
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

# creates the base window
def createWindow ():
    win = GraphWin('Mastermind', 700, 700)
    win.setCoords(0, 0, 30, 30)
    win.setBackground('royalblue4')
    return win

# BACKGROUND PICTORIAL SPACE
def background(gW):
    background = Rectangle(Point(2,29),Point(28,2))
    background.setWidth(5)
    background.setOutline("ivory3")
    background.draw(gW)
    background.setFill("steelblue")


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
          for i in range(1,9):
              numbers = Text(Point(x1,y1),[i])
              numbers.setFace("arial")
              numbers.setTextColor("azure3")
              numbers.setSize(25)
              numbers.draw(gameWind)
              y+=3
              numbers.move(0,y)


def ballGraphs(gaWind):
          ######################################################
          #################  ROUND GAME PEGS   ################
          #REFER TO THESE PIECES FOR ANY LOOP/ANMATION ACTIONS#
          #########  INVOLVING THE PIECE OF THE GAME  #########
          ########################################################

          ## blue
          blueBall = Circle(Point(26.5,3.5),.8)
          blueBall.draw(gaWind)
          blueBall.setFill("blue")
          blueBall.setOutline("blue")
          ## B on ball text
          Bball = Text(Point(26.5,3.5),"B")
          Bball.setSize(20)
          Bball.setFace("arial")
          Bball.draw(gaWind)

          ## red
          redBall  = Circle(Point(26.5,6.5),.8)
          redBall.draw(gaWind)
          redBall.setFill("red")
          redBall.setOutline("red")
          ##R on ball text
          Rball = Text(Point(26.5,6.5),"R")
          Rball.setSize(20)
          Rball.setFace("arial")
          Rball.draw(gaWind)

          ## purple
          purpleBall = Circle(Point(26.5,9.5),.8)
          purpleBall.draw(gaWind)
          purpleBall.setFill("purple")
          purpleBall.setOutline("purple")
          ##P on ball text
          Pball = Text(Point(26.5,9.5),"P")
          Pball.setSize(20)
          Pball.setFace("arial")
          Pball.draw(gaWind)

          ## orange
          orangeBall = Circle(Point(26.5,12.5),.8)
          orangeBall.draw(gaWind)
          orangeBall.setFill("orangered")
          orangeBall.setOutline("orange")
          ##O on ball text
          Oball = Text(Point(26.5,12.5),"O")
          Oball.setSize(20)
          Oball.setFace("arial")
          Oball.draw(gaWind)

          ## green
          greenBall = Circle(Point(26.5,15.5),.8)
          greenBall.draw(gaWind)
          greenBall.setFill("green")
          greenBall.setOutline("green")
          ##G on ball text
          Gball = Text(Point(26.5,15.5),"G")
          Gball.setSize(20)
          Gball.setFace("arial")
          Gball.draw(gaWind)

          ## yellow
          yellowBall = Circle(Point(26.5,18.5),.8)
          yellowBall.draw(gaWind)
          yellowBall.setFill("yellow")
          yellowBall.setOutline("yellow")
          ##Y on ball text
          Yball = Text(Point(26.5,18.5),"Y")
          Yball.setSize(20)
          Yball.setFace("arial")
          Yball.draw(gaWind)


# Black and White pegs on Right Side of board with info.
def guessBoard(gameW):

    # Shannon tried to make a change: I wanted to have a list,
    # info = ["Right Color","Right Place","Wrong Color"]
    # and I tried to cancatinate the elements in the list to create
    #   the phrases to explain the black and white pegs.
    #   info[0]+ " "+info[1] for RCRP
    #   info[0]+ " "+ info[2] for RCWP
    ####
    # I tried to do this with 2 seperate loops and with a nested loop, but the loops
    # made the text look weird. I was able to get it to work, but I compared it to my original
    # and my versions were both LONGER then the original.

          EB = Circle(Point(26.5,22.5),.3)
          EB.draw(gameW)
          EB.setFill("black")

          EW = Circle(Point(26.5,25.5),.3)
          EW.draw(gameW)
          EW.setFill("white")
          EW.setOutline("white")

          ebText1 = Text(Point(26.5,21.5),"Right Color")
          ebText1.draw(gameW)
          ebText1.setFace("arial")
          ebText1.setSize(11)
          ebText2 = Text(Point(26.5,20.5),"Right Place")
          ebText2.draw(gameW)
          ebText2.setFace("arial")
          ebText2.setSize(11)

          ewText3 = Text(Point(26.5,24.5),"Right Color")
          ewText3.setFace("arial")
          ewText3.setTextColor("white")
          ewText3.draw(gameW)
          ewText3.setSize(11)
          ewText4 = Text(Point(26.5,23.5),"Wrong Place")
          ewText4.setFace("arial")
          ewText4.setTextColor("white")
          ewText4.draw(gameW)
          ewText4.setSize(11)



# FAR LEFT SIDE GRID and VERTICAL LINE
# Fancy modular thingy!
def leftLines(gaW):
    vLfL = Line(Point(6,2),Point(6,29))
    vLfL.setFill("ivory")
    vLfL.setWidth(2.5)
    vLfL.draw(gaW)

    x,y = 2,-3
    x1,y1 = 2,5
    x2,y2 = 6,5
    for i in range(9):
          leftLines = Line(Point(2,5),Point(6,5))
          leftLines.setFill("ivory")
          leftLines.setWidth(5)
          leftLines.draw(gaW)
          y+=3
          leftLines.move(0,y)

 ##########WORK IN PROGRESS#########
######STILL BROKEN
# FAR LEFT SIDE 4 hole peg grid graphic
def clueBoard(window):
    x,y = 0,-2
    xA, yA = 3.3,3.3
    x1,y1 = 2,4
    x2,y2 = 6,1
    for i in range(1,9):
        pegBox = Rectangle(Point(x1,y1),Point(x2,y2))
        pegBox.draw(window)
        pegBox.setOutline("ivory")
        pegBox.setWidth(3)
        y+=3
        pegBox.move(0,y)
        for i in range(4):
            pegHole = Circle(Point(xA,yA),.5)
            pegHole.draw(window)
            pegHole.setFill("azure4")
            pegHole.setOutline("azure")
            yA+=.70
            if i == 1 or i == 3:
                pegHole.move(1,0)
            if i == 2 :
                pegHole.move(-.25,.35)


#runs all the functions
def main():
    # Creates and setups the inital parameters needed for the game
    turnCount = 0
    gameWin = createWindow ()
    #functions for graphics
    createBackB = background(gameWin)
    createRightLineGrid = rightLines(gameWin)
    createLeftLineGrid = leftLines(gameWin)
    createNumbers = Numbers(gameWin)
 #   createClue = clueBoard(gameWin) ### WORK IN PROGRESS
    createBalls = ballGraphs(gameWin)
    createInfo = guessBoard(gameWin)
#    createGuessB = guessBoard(gameWin)
#    createMastB = masterBoard()
#    colorMasterList = masterCode ()
    colorMasterList = ['purple', 'orangered', 'orangered', 'red']
    print ('orangered' == 'red')
    print (colorMasterList) #<---- this line for testing only!!!

    # For loop set to the number of guesses a user is allowed
    for turnCount in range (10):

        submit = createButton(gameWin)
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
        elif turnCount == 7:
            result = finishedCondition ('lost', gameWin)
            break
        else:
            drawPegs (bPeg, wPeg, pegCircles, gameWin)

main()
