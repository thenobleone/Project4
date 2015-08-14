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



def guideKey(gWin):
          ####HORIZONTAL LINE SECTIONS#####
          ###FR section 1
          s1fr = Line(Point(23,5),Point(28,5))
          s1fr.setFill("ivory")
          s1fr.setWidth(5)
          s1fr.draw(gWin)

          ###FR section 2
          s2fr = Line(Point(23,8),Point(28,8))
          s2fr.setFill("ivory")
          s2fr.setWidth(5)
          s2fr.draw(gWin)

          ###FR section 3
          s3fr = Line(Point(23,11),Point(28,11))
          s3fr.setFill("ivory")
          s3fr.setWidth(5)
          s3fr.draw(gWin)

          ###FR section 4
          s4fr = Line(Point(23,14),Point(28,14))
          s4fr.setFill("ivory")
          s4fr.setWidth(5)
          s4fr.draw(gWin)

          ###FR section 5
          s5fr = Line(Point(23,17),Point(28,17))
          s5fr.setFill("ivory")
          s5fr.setWidth(5)
          s5fr.draw(gWin)

          ###FR section 6
          s6fr = Line(Point(23,20),Point(28,20))
          s6fr.setFill("ivory")
          s6fr.setWidth(5)
          s6fr.draw(gWin)

          ###FR section 7
          s7fr = Line(Point(23,23),Point(28,23))
          s7fr.setFill("ivory")
          s7fr.setWidth(5)
          s7fr.draw(gWin)

          ###FR section 8
          s8fr = Line(Point(23,26),Point(28,26))
          s8fr.setFill("ivory")
          s8fr.setWidth(5)
          s8fr.draw(gWin)

          #####VERTICAL LINE SECTIONs

          fRvL1 = Line(Point(25,2),Point(25,26))
          fRvL1.setFill("ivory")
          fRvL1.setWidth(1)
          fRvL1.draw(gWin)

          fRvL2 = Line(Point(23,2),Point(23,29))
          fRvL2.setFill("ivory")
          fRvL2.setWidth(2.5)
          fRvL2.draw(gWin)

          #########################
          #####NUMBERS FOR FR SECTION

          # number 1
          t1 = Text(Point(24,3.5),'1')
          t1.setFace("arial")
          t1.setTextColor("azure3")
          t1.setSize(25)
          t1.draw(gWin)
          # number 2
          t2 = Text(Point(24,6.5),'2')
          t2.setFace("arial")
          t2.setTextColor("azure3")
          t2.setSize(25)
          t2.draw(gWin)
          # number 3
          t3 = Text(Point(24,9.5),'3')
          t3.setFace("arial")
          t3.setTextColor("azure3")
          t3.setSize(25)
          t3.draw(gWin)
          #number 4
          t4 = Text(Point(24,12.5),'4')
          t4.setFace("arial")
          t4.setTextColor("azure3")
          t4.setSize(25)
          t4.draw(gWin)
          # number 5
          t5 = Text(Point(24,15.5),'5')
          t5.setFace("arial")
          t5.setTextColor("azure3")
          t5.setSize(25)
          t5.draw(gWin)
          # number 6
          t6 = Text(Point(24,18.5),'6')
          t6.setFace("arial")
          t6.setTextColor("azure3")
          t6.setSize(25)
          t6.draw(gWin)
          # number 7
          t7 = Text(Point(24,21.5),'7')
          t7.setFace("arial")
          t7.setTextColor("azure3")
          t7.setSize(25)
          t7.draw(gWin)
          # number 8
          t8 = Text(Point(24,24.5),'8')
          t8.setFace("arial")
          t8.setTextColor("azure3")
          t8.setSize(25)
          t8.draw(gWin)

          ######################################################
          #################  ROUND GAME PEGS   ################
          #REFER TO THESE PIECES FOR ANY LOOP/ANMATION ACTIONS#
          #########  INVOLVING THE PIECE OF THE GAME  #########
          ########################################################

          ## blue
          blueBall = Circle(Point(26.5,3.5),.8)
          blueBall.draw(gWin)
          blueBall.setFill("blue")
          blueBall.setOutline("blue")
          ## B on ball text
          Bball = Text(Point(26.5,3.5),"B")
          Bball.setSize(20)
          Bball.setFace("arial")
          Bball.draw(gWin)

          ## red
          redBall  = Circle(Point(26.5,6.5),.8)
          redBall.draw(gWin)
          redBall.setFill("red")
          redBall.setOutline("red")
          ##R on ball text
          Rball = Text(Point(26.5,6.5),"R")
          Rball.setSize(20)
          Rball.setFace("arial")
          Rball.draw(gWin)

          ## purple
          purpleBall = Circle(Point(26.5,9.5),.8)
          purpleBall.draw(gWin)
          purpleBall.setFill("purple")
          purpleBall.setOutline("purple")
          ##P on ball text
          Pball = Text(Point(26.5,9.5),"P")
          Pball.setSize(20)
          Pball.setFace("arial")
          Pball.draw(gWin)

          ## orange
          orangeBall = Circle(Point(26.5,12.5),.8)
          orangeBall.draw(gWin)
          orangeBall.setFill("orangered")
          orangeBall.setOutline("orange")
          ##O on ball text
          Oball = Text(Point(26.5,12.5),"O")
          Oball.setSize(20)
          Oball.setFace("arial")
          Oball.draw(gWin)

          ## green
          greenBall = Circle(Point(26.5,15.5),.8)
          greenBall.draw(gWin)
          greenBall.setFill("green")
          greenBall.setOutline("green")
          ##G on ball text
          Gball = Text(Point(26.5,15.5),"G")
          Gball.setSize(20)
          Gball.setFace("arial")
          Gball.draw(gWin)

          ## yellow
          yellowBall = Circle(Point(26.5,18.5),.8)
          yellowBall.draw(gWin)
          yellowBall.setFill("yellow")
          yellowBall.setOutline("yellow")
          ##Y on ball text
          Yball = Text(Point(26.5,18.5),"Y")
          Yball.setSize(20)
          Yball.setFace("arial")
          Yball.draw(gWin)

def guessBoard(gameW):
          ####################################################
          #### BLACK AND WHITE PEGS WITH EXPLAINATION ##
          #### OF PEG MEANING ON RS   ######################
          ####################################################
          EB = Circle(Point(26.5,22.5),.3)
          EB.draw(gameW)
          EB.setFill("black")

          ebText1 = Text(Point(26.5,21.5),"Right Color")
          ebText1.draw(gameW)
          ebText1.setFace("arial")
          ebText1.setSize(11)
          ebText2 = Text(Point(26.5,20.5),"Right Place")
          ebText2.draw(gameW)
          ebText2.setFace("arial")
          ebText2.setSize(11)

          EW = Circle(Point(26.5,25.5),.3)
          EW.draw(gameW)
          EW.setFill("white")
          EW.setOutline("white")

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

          #####################################################
          #FAR LEFT SIDE AREA WHERE BLACK AND WHITE PEGS WILL APPEAR.
          #######FOR ANY ANIMATION/LOOPS THAT UTILIZE WHITE AND BLACK
          ############PEGS, REFER TO THIS SECTION.

          #####SECTION BOXES 1-8 : AREAS WHERE WHITE AND BLACK PEGS
          ####### ARE STORED AS 'HINTS'

          #HORIZONTAL LINE SECTIONS
          #FL section 1
          s1fl = Line(Point(2,5),Point(6,5))
          s1fl.setFill("ivory")
          s1fl.setWidth(5)
          s1fl.draw(gameW)

          #FL section 2
          s2fl = Line(Point(2,8),Point(6,8))
          s2fl.setFill("ivory")
          s2fl.setWidth(5)
          s2fl.draw(gameW)

          #FL section 3
          s3fl = Line(Point(2,11),Point(6,11))
          s3fl.setFill("ivory")
          s3fl.setWidth(5)
          s3fl.draw(gameW)

           #FL section 4
          s4fl = Line(Point(2,14),Point(6,14))
          s4fl.setFill("ivory")
          s4fl.setWidth(5)
          s4fl.draw(gameW)

          #FL section 5
          s5fl = Line(Point(2,17),Point(6,17))
          s5fl.setFill("ivory")
          s5fl.setWidth(5)
          s5fl.draw(gameW)

          #FL section 6
          s6fl = Line(Point(2,20),Point(6,20))
          s6fl.setFill("ivory")
          s6fl.setWidth(5)
          s6fl.draw(gameW)

          #FL section 7
          s7fl = Line(Point(2,23),Point(6,23))
          s7fl.setFill("ivory")
          s7fl.setWidth(5)
          s7fl.draw(gameW)

          #FL section 8
          s8fl = Line(Point(2,26),Point(6,26))
          s8fl.setFill("ivory")
          s8fl.setWidth(5)
          s8fl.draw(gameW)

          ######VERTICAL LINE SECTION
          vLfL = Line(Point(6,2),Point(6,29))
          vLfL.setFill("ivory")
          vLfL.setWidth(2.5)
          vLfL.draw(gameW)


 
def clueBoard(window):
    # starting location = rectangle
    x,y = 0,-2
    # starting location = X4 pegHole circle
    xA, yA = 3.3,3.3
    # rectangle 
    x1,y1 = 2,4
    x2,y2 = 6,1
   

    
    #first loop for 8 boxes
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
    createGuideB = guideKey(gameWin)
    #createGuessB = guessBoard(gameWin)
    
#    createMastB = masterBoard()
    colorMasterList = masterCode ()
    print (colorMasterList) #<---- this line for testing only!!!

    # For loop set to the number of guesses a user is allowed
    for turnCount in range (10):
        createClue = clueBoard(gameWin)
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
