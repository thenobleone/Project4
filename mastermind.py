# mastermindJS.py
# Created by Jo Narvaez-Jesen & Shannon Poehlemn

<<<<<<< Updated upstream
# Here was the idea I had for graphics. Colors will be changed once we
#         decide on a design.

##############################################################
################   BACKGROUND GRAPHICS   ##################
##############################################################
from graphics import*

def main():

          #window
          win = GraphWin('Mastermind',700,700)
          win.setCoords(0,0,30,30)
          win.setBackground('tan')

          ### Board background- FR side where colors with coorispoding letters are.
          background = Rectangle(Point(2,29),Point(28,2))
          background.draw(win)
          background.setFill("brown")

          ##############################################################
          ##############################################################
          # MIDDLE AREA WHERE 4 COLOR GUESSES WILL BE SUBMITTED
          # AND SAVED FOR 8 GUESSES OR UNTIL PUZZLE IS SOLVED.
          ##############################################################

          ##################################################
          # Section 1 guess storage-- A, B, C, D columns
          #1A
          s1a = Circle(Point(8.5,3.5),1)
          s1a.draw(win)
          #1B
          s1b = s1a.clone()
          s1b.draw(win)
          s1b.move(4,0)
          #1C
          s1c = s1b.clone()
          s1c.draw(win)
          s1c.move(4,0)
          #1D
          s1d = s1c.clone()
          s1d.draw(win)
          s1d.move(4,0)

          #################################################
          #Section 2 guess storage-- A, B, C, D columns
          #2A
          s2a = Circle(Point(8.5,6.5),1)
          s2a.draw(win)
          #2B
          s2b = s2a.clone()
          s2b.draw(win)
          s2b.move(4,0)
          #2C
          s2c = s2b.clone()
          s2c.draw(win)
          s2c.move(4,0)
          #2D
          s2d = s2c.clone()
          s2d.draw(win)
          s2d.move(4,0)

          #################################################
          #Section 3 guess storage-- A, B, C, D columns
          #3A
          s3a = Circle(Point(8.5,9.5),1)
          s3a.draw(win)
          #3B
          s3b = s3a.clone()
          s3b.draw(win)
          s3b.move(4,0)
          #3C
          s3c = s3b.clone()
          s3c.draw(win)
          s3c.move(4,0)
          #3D
          s3d = s3c.clone()
          s3d.draw(win)
          s3d.move(4,0)

          #################################################
          #Section 4 guess storage-- A, B, C, D columns
          #4A
          s4a = Circle(Point(8.5,12.5),1)
          s4a.draw(win)
          #4B
          s4b = s4a.clone()
          s4b.draw(win)
          s4b.move(4,0)
          #4C
          s4c = s4b.clone()
          s4c.draw(win)
          s4c.move(4,0)
          #4D
          s4d = s4c.clone()
          s4d.draw(win)
          s4d.move(4,0)

          #################################################
          #Section 5 guess storage-- A, B, C, D columns
          #5A
          s5a = Circle(Point(8.5,15.5),1)
          s5a.draw(win)
          #5B
          s5b = s5a.clone()
          s5b.draw(win)
          s5b.move(4,0)
          #5C
          s5c = s5b.clone()
          s5c.draw(win)
          s5c.move(4,0)
          #5D
          s5d = s5c.clone()
          s5d.draw(win)
          s5d.move(4,0)

          #################################################
          #Section 6 guess storage-- A, B, C, D columns
          #6A
          s6a = Circle(Point(8.5,18.5),1)
          s6a.draw(win)
          #6B
          s6b = s6a.clone()
          s6b.draw(win)
          s6b.move(4,0)
          #6C
          s6c = s6b.clone()
          s6c.draw(win)
          s6c.move(4,0)
          #6D
          s6d = s6c.clone()
          s6d.draw(win)
          s6d.move(4,0)

          #################################################
          #Section 7 guess storage-- A, B, C, D columns
          #7A
          s7a = Circle(Point(8.5,21.5),1)
          s7a.draw(win)
          #7B
          s7b = s7a.clone()
          s7b.draw(win)
          s7b.move(4,0)
          #7C
          s7c = s7b.clone()
          s7c.draw(win)
          s7c.move(4,0)
          #7D
          s7d = s7c.clone()
          s7d.draw(win)
          s7d.move(4,0)

          #################################################
          #Section 8 guess storage-- A, B, C, D columns
          #8A
          s8a = Circle(Point(8.5,24.5),1)
          s8a.draw(win)
          #8B
          s8b = s8a.clone()
          s8b.draw(win)
          s8b.move(4,0)
          #8C
          s8c = s8b.clone()
          s8c.draw(win)
          s8c.move(4,0)
          #8D
          s8d = s8c.clone()
          s8d.draw(win)
          s8d.move(4,0)

          ######################################################
          ##########END GUESS STORAGE GRAPHICS############
          ######################################################

          ####
          ####
          ####

          ######################################################
          #######MASTERMIND ANSWER AREA#######
          ######################################################

          answer = Oval(Point(6,29),Point(23,26))
          answer.draw(win)
          answer.setFill("lightskyblue")

          #####################################################
          #FAR LEFT SIDE AREA WHERE BLACK AND WHITE PEGS WILL APPEAR.
          #######FOR ANY ANIMATION/LOOPS THAT UTILIZE WHITE AND BLACK
          ############PEGS, REFER TO THIS SECTION.

          #####SECTION BOXES 1-8 : AREAS WHERE WHITE AND BLACK PEGS
          ####### ARE STORED AS 'HINTS'

          #HORIZONTAL LINE SECTIONS
          #FL section 1
          s1fl = Line(Point(2,5),Point(6,5))
          s1fl.draw(win)

          #FL section 2
          s2fl = Line(Point(2,8),Point(6,8))
          s2fl.draw(win)

          #FL section 3
          s3fl = Line(Point(2,11),Point(6,11))
          s3fl.draw(win)

           #FL section 4
          s4fl = Line(Point(2,14),Point(6,14))
          s4fl.draw(win)

          #FL section 5
          s5fl = Line(Point(2,17),Point(6,17))
          s5fl.draw(win)

          #FL section 6
          s6fl = Line(Point(2,20),Point(6,20))
          s6fl.draw(win)

          #FL section 7
          s7fl = Line(Point(2,23),Point(6,23))
          s7fl.draw(win)

          #FL section 8
          s8fl = Line(Point(2,26),Point(6,26))
          s8fl.draw(win)

          ######VERTICAL LINE SECTION
          vLfL = Line(Point(6,2),Point(6,29))
          vLfL.draw(win)


          #########################################################
          #FAR RIGHT SIDE AREA WHERE GAME PEGS ARE LOCATED.
          #########################################################


          ####HORIZONTAL LINE SECTIONS#####
          ###FR section 1
          s1fr = Line(Point(23,5),Point(28,5))
          s1fr.draw(win)

          ###FR section 2
          s2fr = Line(Point(23,8),Point(28,8))
          s2fr.draw(win)

          ###FR section 3
          s3fr = Line(Point(23,11),Point(28,11))
          s3fr.draw(win)

          ###FR section 4
          s4fr = Line(Point(23,14),Point(28,14))
          s4fr.draw(win)

          ###FR section 5
          s5fr = Line(Point(23,17),Point(28,17))
          s5fr.draw(win)

          ###FR section 6
          s6fr = Line(Point(23,20),Point(28,20))
          s6fr.draw(win)

          ###FR section 7
          s7fr = Line(Point(23,23),Point(28,23))
          s7fr.draw(win)

          ###FR section 8
          s8fr = Line(Point(23,26),Point(28,26))
          s8fr.draw(win)

          #####VERTICAL LINE SECTIONs

          fRvL1 = Line(Point(25,2),Point(25,29))
          fRvL1.draw(win)

          fRvL2 = Line(Point(23,2),Point(23,29))
          fRvL2.draw(win)

          #########################
          #####NUMBERS FOR FR SECTION

          # number 1
          t1 = Text(Point(24,3.5),'1')
          t1.draw(win)

          # number 2
          t2 = Text(Point(24,6.5),'2')
          t2.draw(win)
          # number 3
          t3 = Text(Point(24,9.5),'3')
          t3.draw(win)
          #number 4
          t4 = Text(Point(24,12.5),'4')
          t4.draw(win)
          # number 5
          t5 = Text(Point(24,15.5),'5')
          t5.draw(win)
          # number 6
          t6 = Text(Point(24,18.5),'6')
          t6.draw(win)
          # number 7
          t7 = Text(Point(24,21.5),'7')
          t7.draw(win)
          # number 8
          t8 = Text(Point(24,24.5),'8')
          t8.draw(win)

          ######################################################
          #################  ROUND GAME PEGS   ################
          #REFER TO THESE PIECES FOR ANY LOOP/ANMATION ACTIONS#
          #########  INVOLVING THE PIECE OF THE GAME  #########
          ########################################################

          ## blue
          blueBall = Circle(Point(26.5,3.5),.8)
          blueBall.draw(win)
          blueBall.setFill("blue")
          ## B on ball text
          Bblue = Text(Point(26.5,3.5),"B")
          Bblue.draw(win)

          ## red
          redBall  = Circle(Point(26.5,6.5),.8)
          redBall.draw(win)
          redBall.setFill("red")
          ##R on ball text
          Rball = Text(Point(26.5,6.5),"R")
          Rball.draw(win)

          ## purple
          purpleBall = Circle(Point(26.5,9.5),.8)
          purpleBall.draw(win)
          purpleBall.setFill("purple")
          ##P on ball text
          Pball = Text(Point(26.5,9.5),"P")
          Pball.draw(win)

          ## orange
          orangeBall = Circle(Point(26.5,12.5),.8)
          orangeBall.draw(win)
          orangeBall.setFill("orange3")
          ##O on ball text
          Oball = Text(Point(26.5,12.5),"O")
          Oball.draw(win)

          ## green
          greenBall = Circle(Point(26.5,15.5),.8)
          greenBall.draw(win)
          greenBall.setFill("green")
          ##G on ball text
          Gball = Text(Point(26.5,15.5),"G")
          Gball.draw(win)

          ## yellow
          yellowBall = Circle(Point(26.5,18.5),.8)
          yellowBall.draw(win)
          yellowBall.setFill("yellow")
          ##Y on ball text
          Yball = Text(Point(26.5,18.5),"Y")
          Yball.draw(win)

          ####################################################
          #### BLACK AND WHITE PEGS WITH EXPLAINATION ##
          #### OF PEG MEANING    ############################
          ####################################################

          EB = Circle(Point(26.5,22.5),.3)
          EB.draw(win)
          EB.setFill("black")

          ebText1 = Text(Point(26.5,21.5),"Right Color")
          ebText1.draw(win)
          ebText1.setSize(10)
          ebText2 = Text(Point(26.5,20.5),"Right Place")
          ebText2.draw(win)
          ebText2.setSize(10)

          EW = Circle(Point(26.5,25.5),.3)
          EW.draw(win)
          EW.setFill("white")

          ewText3 = Text(Point(26.5,24.5),"Right Color")
          ewText3.draw(win)
          ewText3.setSize(10)
          ewText4 = Text(Point(26.5,23.5),"Wrong Place")
          ewText4.draw(win)
          ewText4.setSize(10)


main()
