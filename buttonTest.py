# buttonTest.py

from graphics import *
from button import Button

def main():
          win = GraphWin()
          win.setCoords(0,0,10,10)
          win.setBackground("green2")

          quitButton = Button(win,Point(5,1),2,1,"Quit")
          quitButton.activate()
          pt = win.getMouse()
          if quitButton.clicked(pt):
                    win.close()
                            
main()
          
          

          
          
