# Tic-Tac-Jo.py
# Created by Jo Narvaez-Jensen & Shannon Poehlemn

# Tic Tac Toe GUI python game

#def player1 (gameGUI):

#def player2 (gameGUI):

#def scoreboard (gameGUI):

from graphics import *
import random

def results (order, winner, gWin):
    if winner == 'x':
        wPlayer = order[0]
    else:
        wPlayer = order[1]  #3, 4

    WinBox = Rectangle (Point (2.5, 2.5), Point (4.5, 4.5))
    WinBox.setFill ('lightslateblue')
    WinBox.setOutline ('black')
    WinBox.setWidth (3)
    WinBox.draw (gWin)

    winMessage = Text (Point (4, 3), "{0} wins!".format(wPlayer))
    winMessage.setFace ('arial')
    winMessage.setFill ('dodgerblue')
    winMessage.setOutline ('steelblue')
    winMessage.setSize (25)
    winMessage.draw (gWin)

    playAgain = Text (Point (4, 2.5), "Press Any to Key To Continue\nClick to Close")
    playAgain.draw (gWin)

def whoWon (brd, move, gWin):
    winLine = {
        'd1' : Line (Point (.15, .15), Point (5.85, 5.85)),
        'd2' : Line (Point (.15, 5.85), Point (5.85, .15)),
        'v1' : Line (Point (1, .15), Point (1, 5.85)),
        'v2' : Line (Point (3, .15), Point (3, 5.85)),
        'v3' : Line (Point (5, .15), Point (5, 5.85)),
        'h1' : Line (Point (.15, 1), Point (5.85, 1)),
        'h2' : Line (Point (.15, 3), Point (5.85, 3)),
        'h3' : Line (Point (.15, 5), Point (5.85, 5)),
        }

    for wl, dl in winLine.items():
        dl.setFill('#FF9912')
        dl.setWidth ('10')

    if move == brd[0] and (move == brd[1] == brd[2]):
            winLine['v1'].draw (gWin)
            return move
    elif move == brd[0] and (move == brd[3] == brd[6]):
            winLine['h1'].draw (gWin)
            return move
    elif move == brd[0] and (move == brd[4] == brd[8]):
            winLine['d1'].draw (gWin)
            return move
    elif move == brd[1] and (move == brd[4] == brd[7]):
        winLine['h2'].draw (gWin)
        return move
    elif move == brd[2] and (move == brd[5] == brd[8]):
            winLine['h3'].draw (gWin)
            return move
    elif move == brd[2] and (move == brd[4] == brd[6]):
            winLine['d2'].draw (gWin)
            return move
    elif move == brd[3] and (move == brd[4] == brd[5]):
        winLine['v2'].draw (gWin)
        return move
    elif move == brd[6] and (move == brd[7] == brd[8]):
        winLine['v3'].draw (gWin)
        return move
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
        winner = whoWon (board, move, gWin)
        if turn > 9:
            winner = 'tie'
    return winner

def playerCard (name, p1score, p2score, gWin):
    y = 4.15
    color = ['navy', 'black']
    for i in range (2):
        card = Text (Point (7, y), name[i])
        card.setTextColor(color[i])
        card.setSize(15)
        card.setStyle ('bold')
        card.setFace ('arial')
        card.draw (gWin)
        y -= 2

    scoreText1 = Text (Point (6.5, .75), p1score)
    scoreText1.setTextColor ('navy')
    scoreText1.setSize (20)
    scoreText1.draw (gWin)

    scoreText2 = Text (Point (7.5, .75), p2score)
    scoreText2.setTextColor ('black')
    scoreText2.setSize (20)
    scoreText2.draw (gWin)

def gamePieces ():
    xPiece = Polygon (Point(1, 1), Point(.25, 1.75), Point(1, 1), Point(1.75, 1.75), Point(1, 1), Point(1.75, .25), Point(1, 1), Point(.25, .25))
    xPiece.setWidth (8)
    xPiece.setOutline ('navy')

    oPiece = Circle (Point (1, 1), .65)
    oPiece.setWidth (8)
    oPiece.setOutline ('black')

    return  xPiece, oPiece

def playerOrder (players):
    random.shuffle(players)
    return players

def sidebar (players, xP, oP, gWin):
    bgc = ['slategray', 'darkcyan', 'lightcoral']
    y = 0
    for i in range (3):
        bar = Rectangle (Point (6, y), Point (8, y + 2))
        bar.draw (gWin)
        bar.setOutline ('black')
        bar.setWidth(2)
        bar.setFill(bgc[i])
        y += 2

    p1Card = xP.clone ()
    p1Card.move (6,4)
    p1Card.draw (gWin)

    p2Card = oP.clone()
    p2Card.move (6,2)
    p2Card.draw (gWin)

    txt = ["SCORECARD", players [0][:9], players[1][:9]]
    colorName = ['red','navy', 'black']
    SCLoc = [[7, 1.75], [6.5, 1.5], [7.5,1.5]]

    for i in range (3):
        sideTxt = Text (Point (SCLoc[i][0], SCLoc[i][1]), txt[i])
        sideTxt.setFace ('arial')
        sideTxt.setStyle('bold')
        sideTxt.setTextColor(colorName[i])
        sideTxt.setSize(15)
        sideTxt.draw(gWin)

    scoreLine = Line (Point (7,.15), Point (7, 1.6))
    scoreLine.setWidth(2)
    scoreLine.draw (gWin)

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

    startScreen[0] = Text (Point(4, 4.5),"WELCOME to Tic-Tac-Toe")
    startScreen[0].setSize (35)
    startScreen[0].setTextColor ('red4')
    startScreen[0].setFace ('arial')
    startScreen[0].draw (window)

    startScreen[1] = Rectangle (Point (2.5, 2.45), Point (5.5, 3.6))
    startScreen[1].setFill ('ivory')
    startScreen[1].setWidth (3)
    startScreen[1].draw (window) # 4, 3 is center

    startScreen[2] = Text(Point (4, 1.8), "Click to Start Game")
    startScreen[2].setTextColor ('red')
    startScreen[2].setSize (20)
    startScreen[2].draw (window)

    nameField = []
    x, y = 4, 3.3

    for i in range (2):
        nameField.append (Entry(Point(x, y), 25))
        nameField[i].setSize (17)
        nameField[i].setStyle ('bold')
        nameField[i].setFace ('arial')
        nameField[i].setTextColor ('white')
        nameField[i].setText ('Player Name')
        if i == 0:
            nameField[i].setFill ('navy')
            nameField[i].draw (window)
        elif i == 1:
            nameField[i].draw (window)
            nameField[i].move (0, -.55)
            nameField[i].setFill ('ivory')
            nameField[i].setTextColor ('black')

    window.getMouse()

    playerName = []
    i = 0
    for n in nameField:
        playerName.append (nameField[i].getText())

    clearFeature (nameField)
    clearFeature (startScreen)
    return playerName

def clearFeature (feature):
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
    p1score, p2score, again = 0, 0, ''
    gWindow = createWindow ()
    players = startScreen (gWindow)
    xGamePiece, oGamePiece = gamePieces ()
    sidebar (players, xGamePiece, oGamePiece, gWindow)

    while again == '':
        drawGrid (gWindow)
        order = playerOrder (list (players))
        playerCard (order, p1score, p2score, gWindow)
        status = runGame (xGamePiece, oGamePiece, gWindow)
        again = results (order, status, gWindow)


main ()
