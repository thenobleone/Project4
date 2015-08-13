# tttL.py
# Created by Jo Narvaez-Jensen & Shannon Poehlemn

# Tic Tac Toe GUI python game

#def player1 (gameGUI):

#def player2 (gameGUI):

#def scoreboard (gameGUI):

from graphics import *
import random

def whoWon (winner):
    print (winner)

def winCheck (board, piece):
    if board[0] == piece:
        if board[4] == piece and board[8] == piece:
            whoWon(piece)
        elif board[4] == piece and board[8] == piece:
            whoWon(piece)
        elif board[3] == piece and board [6] == piece:
            whoWon(piece)
    elif board[1] == piece:
        if board[4] == piece and board[7] == piece:
            whoWon(piece)
    elif board[2] == piece:
        if board [5] == piece and board[8] == piece:
            whoWon(piece)
        elif board[4] == piece and board[6] == piece:
            whoWon(piece)

def filledPiece ():
    print ("That piece has already been taken! Try again.")

def placePiece (gamePiece, xo, storeMove, playingSquare, win):
    click = win.getMouse ()
    x, y = click.getX (), click.getY ()
    print (xo)
    if x > 0 and x < 2:
        if y > 0 and y < 2:
            if storeMove[0] == None:
                storeMove[0] = xo
                playingSquare[0] = gamePiece
                playingSquare[0].draw (win)
            else:
                filledPiece ()
        elif y > 2 and y < 4:
            if storeMove[1] == None:
                storeMove[1] = xo
                playingSquare[1] = gamePiece
                playingSquare[1].draw (win)
                playingSquare[1].move (0, 2)
            else:
                filledPiece ()
        elif y > 4 and y < 6:
            if storeMove[2] == None:
                storeMove[2] = xo
                playingSquare[2] = gamePiece
                playingSquare[2].draw (win)
                playingSquare[2].move (0, 4)
            else:
                filledPiece ()
    elif x > 2 and x < 4:
        if y > 0 and y < 2:
            if storeMove[3] == None:
                storeMove[3] = xo
                playingSquare[3] = gamePiece
                playingSquare[3].draw (win)
                playingSquare[3].move (2, 0)
            else:
                filledPiece ()
        elif y > 2 and y < 4:
            if storeMove[4] == None:
                storeMove[4] = xo
                playingSquare[4] = gamePiece
                playingSquare[4].draw (win)
                playingSquare[4].move (2, 2)
            else:
                filledPiece ()
        elif y > 4 and y < 6:
            if storeMove[5] == None:
                storeMove[5] = xo
                playingSquare[5] = gamePiece
                playingSquare[5].draw (win)
                playingSquare[5].move (2, 4)
            else:
                filledPiece ()
    elif x > 4 and x < 6:
        if y > 0 and y < 2:
            if storeMove[6] == None:
                storeMove[6] = xo
                playingSquare[6] = gamePiece
                playingSquare[6].draw (win)
                playingSquare[6].move (4, 0)
            else:
                filledPiece ()
        elif y > 2 and y < 4:
            if storeMove[7] == None:
                storeMove[7] = xo
                playingSquare[7] = gamePiece
                playingSquare[7].draw (win)
                playingSquare[7].move (4, 2)
            else:
                filledPiece ()
        elif y > 4 and y < 6:
            if storeMove[8] == None:
                storeMove[8] = xo
                playingSquare[8] = gamePiece
                playingSquare[8].draw (win)
                playingSquare[8].move (4, 4)
            else:
                filledPiece ()
    print (storeMove)
    if storeMove.count ('O') >= 3:
        print (storeMove.count ('O'))
        winCheck (storeMove, 'O')
    elif storeMove.count ('X') >= 3:
        print (storeMove.count ('X'))
        winCheck (storeMove, 'X')

def runGame (xP, oP, turn, squarePiece, win):
    storeMove = [None] * 9
    for i in range (9):
        if turn % 2 != 0: #Odd numbered turn
           turn += 1
           gamePiece = xP.clone ()
           move = 'X'
        elif turn % 2 == 0: # Even numbered turn
            turn += 1
            gamePiece = oP.clone ()
            move = 'O'
        placePiece (gamePiece, move, storeMove, squarePiece, win)
    winner = tie
    whoWon ()

def fieldPieces ():
    field = [None] * 9
    for s in range (9):
        if s < 3:
            x1, y1, x2, y2 = 0, 0, 2, 2
            for p in range (3):
                field[s] = Rectangle (Point (x1, y1), Point (x2, y2))
                y1 += 2
                y2 += 2
        elif s < 6:
            x1, y1, x2, y2 = 2, 0, 4, 2
            for p in range (3):
                field[s] = Rectangle (Point (x1, y1), Point (x2, y2))
                y1 += 2
                y2 += 2
        elif s < 9:
            x1, y1, x2, y2 = 4, 0, 6, 2
            for p in range (3):
                field[s] = Rectangle (Point (x1, y1), Point (x2, y2))
                y1 += 2
                y2 += 2

    xPiece = Polygon(Point(1,1),Point(.25,1.75),Point(1,1),Point(1.75,1.75),Point(1,1),Point(1.75,.25),Point(1,1,),Point(.25,.25))
    xPiece.setWidth (8)
    xPiece.setOutline ('navy')

    oPiece = Circle (Point (1, 1), .65)
    oPiece.setWidth (8)
    oPiece.setOutline ('black')

    return  xPiece, oPiece, field

def gameBoard (gameGUI):
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

def clearFeatures (feature):
    if type(feature) == list:
        for i in range (len (feature)):
            feature[i].undraw ()
    else:
        feature.undraw ()

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

def createWindow ():
    gameWin = GraphWin ('TicTacToe', 730, 530)
    gameWin.setCoords (0, 0, 8, 6)
    gameWin.setBackground ('peachpuff')
    return gameWin

def main ():
    turnCount = 0
    window = createWindow ()
    #players = startScreen (window)
    gameBoard (window)
    #sideBoard (window)
    xGamePiece, oGamePiece, squarePiece = fieldPieces ()
    runGame (xGamePiece, oGamePiece, turnCount, squarePiece, window)

main ()
