# graphicLogic.py

def guessLine (guess, x, y, win):
    dot = []
    for i in range (4):
        dot[i] = Circle (Point (x, y), 1)
        dot[i].setFill (guess[i])
        dot[i].draw (win)
        x = x + 4

def createPeg (bPeg, wPeg, x, y, win):
    peg = []
    pegCount = bPeg + wPeg

    for i in range (pegCount):
        peg[i] = Circle (Point (x, y), .25)
        if bPeg > 0:
            peg[i].setFill('black')
            bPeg -= 1
            peg[i].draw(win)
        elif wPeg > 0:
            peg[i].setFill ('white')
            wPeg -= 1
            peg[i].draw(win)
