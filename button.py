# button.py
# SHANNON MADE DIS! 
# Creating class Button for Mastermind.####

from graphics import *

class Button:

          def __init__(self, win, center, width, height, label):
                    """ Creates a rectangle button, eg:
                    qb = Button(myWin, centerPoint, width, height, 'Quit')"""
                    w, h = width/2.0, height/2.0
                    x, y = center.getX(), center.getY()
                    self.xmax, self.xmin = x+w, x-w
                    self.ymax, self.ymin = y+h, y-h
                    p1 = Point(self.xmin, self.ymin)
                    p2 = Point(self.xmax, self.ymax)
                    self.rect = Rectangle(p1,p2)
                    self.rect.setFill('azure')
                    self.rect.setOutline('dodgerblue3')
                    self.rect.draw(win)
                    self.label = Text(center, label)
                    self.label.setSize(20)
                    self.label.setStyle("bold")
                    self.label.setFace("arial")
                    self.label.setTextColor("dodgerblue3")
                    self.label.draw(win)
                    self.deactivate()

          def clicked(self, p):
                    "Returns true if button is active and p is inside"
                    return (self.active and
                           self.xmin <= p.getX() <= self.xmax and
                           self.ymin <= p.getY() <=self.ymax)

          def getLable(self):
                    "Returns the label string of this button."
                    return self.label.getText()

          def activate(self):
                    "Sets this button to 'active'."
                    self.label.setFill('dodgerblue3')
                    self.rect.setWidth(2)
                    self.active = True

          def deactivate(self):
                    "Sets this button to 'inactive'."
                    self.label.setFill('darkgrey')
                    self.rect.setWidth(1)
                    self.active = False

### this will create a button that will be positioned at a center point (like text), with a width and height.
###  objectName =  Button(windowName, Point( centerOfButtonX, centerOfButtonY ), width, height)
          

