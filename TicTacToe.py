# TicTacToe.py

from graphics import *

def main():
          # Welcome, PLAYER 1, PLAYER 2, and submit. 
          gameWin = GraphWin('TicTacToe',730,530)
          gameWin.setCoords(0,0,27,18)
          gameWin.setBackground("peachpuff")

          welcome = Text(Point(13.5,14),"WELCOME to Tic-Tac-Toe")
          welcome.setSize(35)
          welcome.setTextColor("red4")
          welcome.setFace("arial")
          welcome.draw(gameWin)

          name1 = Entry(Point(13.5,10),30)
          name1.setSize(18)
          name1.setFill("navy")
          name1.setText("Player 1")
          name1.setStyle("bold")
          name1.setFace("arial")
          name1.setTextColor("white")
          name1.draw(gameWin)

          name2 = Entry(Point(13.5,7),30)
          name2.setSize(18)
          name2.setFill("ivory")
          name2.setStyle("bold")
          name2.setFace("arial")
          name2.setText("Player 2")
          name2.draw(gameWin)

          submitBox = Rectangle(Point(9,4),Point(18,1))
          submitBox.setFill("ivory")
          submitBox.setWidth(3)
          submitBox.draw(gameWin)
          submitText = Text(Point(13.5,2.5),"Click to Start Game")
          submitText.setTextColor("red")
          submitText.setSize(20)
          submitText.draw(gameWin)
          gameWin.getMouse()
         

          welcome.undraw()
          name1.undraw()
          name2.undraw()
          submitText.undraw()
          submitBox.undraw()

          ###########################################################

          # TIC TAC TOE BOARD
          gameWin.setBackground("ivory")

          vertLineLeft = Line(Point(6.5,0),Point(6.5,17.8))
          vertLineLeft.setWidth(4)
          vertLineLeft.setFill("navy")
          vertLineLeft.draw(gameWin)

          vertLineRight = Line(Point(12.9,0),Point(12.9,17.8))
          vertLineRight.setWidth(4)
          vertLineRight.setFill("navy")
          vertLineRight.draw(gameWin)

          HorzLineTop = Line(Point(0.3,12),Point(19.3,12))
          HorzLineTop.setWidth(4)
          HorzLineTop.setFill("navy")
          HorzLineTop.draw(gameWin)

          HorzLineBottom = Line(Point(0.3,6),Point(19.3,6))
          HorzLineBottom.setWidth(4)
          HorzLineBottom.setFill("navy")
          HorzLineBottom.draw(gameWin)

          ###########################################################

          ##### PLAYER 1 INFO AND GAME PIECE
          # Player 1 area- RT side of game board
          play1Shelf = Rectangle(Point(19.5,18),Point(26.5,11.5))
          play1Shelf.setFill("navy")
          play1Shelf.setOutline("black")
          play1Shelf.draw(gameWin)
          # X game piece
          xGamePiece = Line(Point(21,17.4),Point(25,13.4))
          xGamePiece.draw(gameWin)
          xGamePiece.setFill("white")
          xGamePiece.setWidth(3)
          xGamePiece2 = Line(Point(21,13.4),Point(25,17.4))
          xGamePiece2.setFill("white")
          xGamePiece2.setWidth(3)
          xGamePiece2.draw(gameWin)
         # Player 1 name entry
          playr1 = Text(Point(23,12.7),"Player 1:  {0} ".format(name1.getText()))
          playr1.setSize(14)
          playr1.setFace("arial")
          playr1.setStyle("bold")
          playr1.setTextColor("white")
          playr1.draw(gameWin)
          
          #### PLAYER 2 INFO AND GAME PIECE
           # Player 2 area- RT side of game board
          play2Shelf = Rectangle(Point(19.5,11.5),Point(26.5,4.8))
          play2Shelf.setFill("white")
          play2Shelf.draw(gameWin)
          # Team O
          oGamePiece = Circle(Point(23,8.7),2)
          oGamePiece.setWidth(3)
          oGamePiece.draw(gameWin)
          # Player 2 name entry
          playr2 = Text(Point(23,6),"Player 2:  {0} ".format(name2.getText()))
          playr2.setSize(14)
          playr2.setFace("arial")
          playr2.setStyle("bold")
          playr2.setTextColor("black")
          playr2.draw(gameWin)

          # Player Scores
          # Score Shelf
          scoreShelf = Rectangle(Point(19.5,4.8),Point(26.5,0))
          scoreShelf.setFill("peachpuff")
          scoreShelf.draw(gameWin)
          Score = Text(Point(23,4.2), "SCOREBOARD")
          Score.setFace("arial")
          Score.setStyle("bold")
          Score.setTextColor("red")
          Score.setSize(17)
          Score.draw(gameWin)
          # PLAYER 1 AND PLAYER 2 SCORES
          PL1 = Text(Point(21.5,3.4),"{0}".format(name1.getText()))
          PL1.setTextColor("navy")
          PL1.setStyle("bold")
          PL1.setSize(14)
          PL1.draw(gameWin)
          PL2 = Text(Point(24.6,3.4),"{0}".format(name2.getText()))
          PL2.setStyle("bold")
          PL2.setSize(14)
          PL2.draw(gameWin)

          
main()
          
