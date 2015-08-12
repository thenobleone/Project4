from graphics import *

def main():
          win = GraphWin(730,530)
          win.setCoords(0,0,8,6)
          
          x = Polygon(Point(1,1),Point(.25,1.75),Point(1,1),Point(1.75,1.75),Point(1,1),Point(1.75,.25),Point(1,1,),Point(.25,.25))
          x.draw(win)
main()
