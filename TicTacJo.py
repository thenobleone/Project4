# Tic-Tac-Jo.py
# Created by Jo Narvaez-Jensen & Shannon Poehlemn

# Tic Tac Toe GUI python game

#def player1 (gameGUI):

#def player2 (gameGUI):

#def scoreboard (gameGUI):

from graphics import *
import random


def whoWon (brd, move):
    if move == brd[0] and ((move == brd[1] == brd[2]) or (move == brd[3] == brd[6]) or (move == brd[4] == brd[8])):
        return move+"1"
    elif move == brd[1] and (move == brd[4] == brd[7]):
        return move+"2"
    elif move == brd[2] and ((move == brd[5] == brd[8]) or (move == brd[4] == brd[6])):
        return move+"3"
    elif move == brd[3] and (move == brd[4] == brd[5]):
        return move+"4"
    elif move == brd[6] and (move == brd[7] == brd[8]):
        return move+"5"
    else:
        return ''

def fullSqr ():
    print ("That piece has already been taken! Try again.")

def runGame (xP, oP, gWin):
    turn = 1
    board = [None] * 9
    winner = ''

    while winner == '':
        if turn % 2 != 0:
           gamePiece = xP.clone ()
           move  = 'x'
        elif turn % 2 == 0:
            gamePiece = oP.clone ()
            move = 'o'
        #board, turnCount = playPiece (move, gamePiece, board, turnCount, gWin)

        gridLoc = {
            'Sq1' : [0,0, 2,2, 0],
            'Sq2' : [0,2, 2,4, 1],
            'Sq3' : [0,4, 2,6, 2],
            'Sq4' : [2,0, 4,2, 3],
            'Sq5' : [2,2, 4,4, 4],
            'Sq6' : [2,4, 4,6, 5],
            'Sq7' : [4,0, 6,2, 6],
            'Sq8' : [4,2, 6,4, 7],
            'Sq9' : [4,4, 6,6, 8],
            }
        gridDraw = {
            'Sq1' : [0, 0],
            'Sq2' : [0, 2],
            'Sq3' : [0, 4],
            'Sq4' : [2, 0],
            'Sq5' : [2, 2],
            'Sq6' : [2, 4],
            'Sq7' : [4, 0],
            'Sq8' : [4, 2],
            'Sq9' : [4, 4],
        }
        click = gWin.getMouse ()
        x, y = click.getX (), click.getY ()

        for sqr, loc in gridLoc.items():
            if x > loc[0] and x < loc[2]:
                if y > loc[1] and y < loc[3]:
                    if board[loc[4]] == None:
                        turn += 1
                        gamePiece.move (gridDraw[sqr][0], gridDraw[sqr][1])
                        gamePiece.draw (gWin)
                        board[loc[4]] = move
                        gridLoc[sqr] = ''
                    else:
                        print (sqr)
                        fullSqr ()

        print (board)
        winner = whoWon (board, move)

        if turn > 9:
            winner = 'tie'

    print ("winner", winner)

def gamePieces ():
    xPiece = Polygon (Point(1,1), Point(.25,1.75), Point(1,1),P oint(1.75,1.75), Point(1,1), Point(1.75,.25), Point(1,1,), Point(.25,.25))
    xPiece.setWidth (8)
    xPiece.setOutline ('navy')

    oPiece = Circle (Point (1, 1), .65)
    oPiece.setWidth (8)
    oPiece.setOutline ('black')

    return  xPiece, oPiece

def drawGrid (gameGUI):
    gameGUI.setBackground('ivory')

    lines = [None] * 4
    for i in range (4):
        if i == 0:
            lines[i] = Line (Point (2, 0), Point (2, 6))
        elif i == 1:
            lines[i] = Line (Point (4, 0), Point (4, 6))
        elif i == 2:
            lines[i] = Line (Point (0, 2), Point (6, 2))
        elif i == 3:
            lines[i] = Line (Point (0, 4), Point (6, 4))
        lines[i].setWidth (4)
        lines[i].setFill ('navy')
        lines[i].draw(gameGUI)

def startScreen (window):
    startScreen = [None] * 3

    startScreen[0] = Text (Point(13.5,14),"WELCOME to Tic-Tac-Toe")
    startScreen[0].setSize (35)
    startScreen[0].setTextColor ("red4")
    startScreen[0].setFace ("arial")
    startScreen[0].draw (window)

    startScreen[1] = Rectangle (Point(9,4), Point(18,1))
    startScreen[1].setFill ("ivory")
    startScreen[1].setWidth (3)
    startScreen[1].draw (window)

    startScreen[2] = Text(Point (13.5, 2.5), "Click to Start Game")
    startScreen[2].setTextColor ("red")
    startScreen[2].setSize (20)
    startScreen[2].draw (window)

    nameField = []
    x, y = 13.5, 10

    for i in range (2):
        nameField.append (Entry(Point(x, y), 30))
        nameField[i].setStyle ("bold")
        nameField[i].setFace ("arial")
        nameField[i].setTextColor ("white")
        nameField[i].setText ("Player {0}".format (i+1))
        if i == 0:
            nameField[i].setFill ("navy")
        elif i == 1:
            nameField[i].setFill ("ivory")

    playerNames = []
    window.getMouse ()

    for i in range (len (nameField)):
        playerName.append (nameField[i].getText())

    clearFeature (nameField)
    clearFeature (startScreen)

    return playerName

def clearFeatures (feature):
    if type(feature) == list:
        for i in range (len (feature)):
            feature[i].undraw ()
    else:
        feature.undraw ()

def createWindow ():
    gameWin = GraphWin ('TicTacToe', 730, 530)
    gameWin.setCoords (0, 0, 8, 6)
    gameWin.setBackground ('peachpuff')
    return gameWin

def main ():
    gWindow = createWindow ()
    #players = startScreen (window)
    drawGrid (gWindow)
    #sideBoard (window)
    xGamePiece, oGamePiece = gamePieces ()
    runGame (xGamePiece, oGamePiece, gWindow)

main ()
