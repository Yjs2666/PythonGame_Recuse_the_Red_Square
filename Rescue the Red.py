# Project Name：Rescue the Red Square
# programName.py
# Jishuo Yang
# M002 
# Jyang98@syr.edu



from graphics import *
from random import randrange
import time
import math

# (GW)  a GraphWin
def setWin():  # this function is to make the graphics window.
    win = GraphWin("Rescue the Red Square",800,800) 
    win.setCoords(0,0,24,24) # this is the coordinate of the game
    win.setBackground("silver") # background color -- silver
    return win

# Lab18 Bouncing Ball
# This one is use to draw the 6X6 squares as the game board.
def mainBackBoard(win):
    x = 6 # this is X-axis for the bottom left square 
    y = 4 # this is Y-axis for the bottom left square
    # the loop is use to draw the other 35 squares. just use loop to keep adding the X and Y values. 
    for i in range(0,11,4):
        for n in range(0,11,4):
            recDark = Rectangle(Point(x+n,y+i), Point(x+2+n,y+2+i))
            recDark.setFill("olive")
            recDark.setWidth(0)
            recDark.draw(win)
            recLight = Rectangle(Point(x+2+n,y+i), Point(x+4+n,y+2+i))
            recLight.setFill("yellowgreen")
            recLight.setWidth(0)
            recLight.draw(win)
    for i in range(0,11,4):
        for n in range(0,11,4):
            recDark = Rectangle(Point(x+n,y+i-2), Point(x+2+n,y+i))
            recDark.setFill("yellowgreen")
            recDark.setWidth(0)
            recDark.draw(win)
            recLight = Rectangle(Point(x+2+n,y-2+i), Point(x+4+n,y+i))
            recLight.setFill("olive")
            recLight.setWidth(0)
            recLight.draw(win)



#(CLOD)  At least one class of your own design with objects and methods that are used.
# this is the class for the Hero Block which is the main Block. It has some unique feature. 
class Hero(): 
#(LOOD)  A list of objects of a class of your own design. 
    # we use the leftLowerX and leftLowerY as the left lower point of the square
    # then the X+length and Y+Width are the top right Point. So we can draw the square
    def __init__(self,length,width,leftLowerX,leftLowerY,color,dir=0):
        self.color = color
        self.length = length
        self.width = width
        self.leftLowerX = leftLowerX
        self.leftLowerY = leftLowerY
        # this is how to draw the rectangle.
        self.hero = Rectangle(Point(leftLowerX,leftLowerY),Point(leftLowerX+length,leftLowerY+width))
        # this are the features
        # eye Part1 
        self.eyeP1 = Circle(Point(8.95,9.2),0.1)
        # eye Part2
        self.eyeP2 = Circle(Point(9.15,9.2),0.1)
        # eye Part3
        self.eyeP3 = Polygon(Point(8.85,9.2),Point(9.235,9.2),Point(9.05,8.97))
        self.noise = Oval(Point(9.3,9),Point(9.4,8.8))
        self.mouse = Oval(Point(9.05,8.6),Point(9.65,8.7))      
    # Those are the colors of the Hero Block and the features 
    def drawHero(self,win):
        self.hero.draw(win)
        self.hero.setFill(self.color)
        self.eyeP1.setWidth(0)
        self.eyeP2.setWidth(0)
        self.eyeP3.setOutline("lightcoral")
        self.eyeP1.draw(win).setFill("lightcoral")
        self.eyeP2.draw(win).setFill("lightcoral")
        self.eyeP3.draw(win).setFill("lightcoral")
        self.eyeP4 = self.eyeP1.clone()
        self.eyeP5 = self.eyeP2.clone()
        self.eyeP6 = self.eyeP3.clone()
        self.eyeP4.draw(win).move(0.6,0)
        self.eyeP5.draw(win).move(0.6,0)
        self.eyeP6.draw(win).move(0.6,0)
        self.noise.draw(win).setFill("black")
        self.mouse.draw(win).setFill("black")
    # when we moce the Hero, everything moves with it        
    def heroMoveRight(self,win):
        self.dir = 2
        self.hero.move(self.dir,0)
        self.eyeP1.move(self.dir,0)
        self.eyeP2.move(self.dir,0)
        self.eyeP3.move(self.dir,0)
        self.eyeP4.move(self.dir,0)
        self.eyeP5.move(self.dir,0)
        self.eyeP6.move(self.dir,0)
        self.noise.move(self.dir,0)
        self.mouse.move(self.dir,0)
        # here we need to return the direction because we will need it to keep track the movement(more details later)
        return self.dir
    # also when move left
    def heroMoveLeft(self,win):
        self.dir = -2
        self.hero.move(self.dir,0)
        self.eyeP1.move(self.dir,0)
        self.eyeP2.move(self.dir,0)
        self.eyeP3.move(self.dir,0)
        self.eyeP4.move(self.dir,0)
        self.eyeP5.move(self.dir,0)
        self.eyeP6.move(self.dir,0)
        self.noise.move(self.dir,0)
        self.mouse.move(self.dir,0)
        # here we need to return the direction because we will need it to keep track the movement(more details later)
        return self.dir
    # those 4 functions are used to GET the values of the hero.    
    def getLength(self):
        return self.length
    def getWidthHero(self):
        return self.width
    def getLeftLowerX(self):
        return self.leftLowerX
    def getLeftLowerY(self):
        return self.leftLowerY

#(CLOD)  At least one class of your own design with objects and methods that are used.
class Blocks():
    # This class is pretty much the same thing as the Hero Class.
    # The difference is that one is only work for that one square, This Class use to all the rest of them.
#(LOOD)  A list of objects of a class of your own design. 
    def __init__(self,length,width,leftLowerX,leftLowerY,color,dir=0):
        self.color = color
        self.length = length
        self.width = width
        self.leftLowerX = leftLowerX
        self.leftLowerY = leftLowerY
        self.rectangle = Rectangle(Point(leftLowerX,leftLowerY),Point(leftLowerX+length,leftLowerY+width))
        self.rectangle.setFill(self.color)
        self.dir=dir
        # the arrow is giving the palyer an idea of what to click. when you click the arrow and surrouding, the block will move.
        self.arrowVerUp = Polygon(Point((leftLowerX+leftLowerX+length)/2,leftLowerY+width-0.2),Point((leftLowerX+leftLowerX+length)/2-0.2,leftLowerY+width-0.4),Point((leftLowerX+leftLowerX+length)/2-0.1,leftLowerY+width-0.4),Point((leftLowerX+leftLowerX+length)/2-0.1,leftLowerY+width-0.8),Point((leftLowerX+leftLowerX+length)/2+0.1,leftLowerY+width-0.8),Point((leftLowerX+leftLowerX+length)/2+0.1,leftLowerY+width-0.4),Point((leftLowerX+leftLowerX+length)/2+0.2,leftLowerY+width-0.4))
        self.arrowVerLow = Polygon(Point((leftLowerX+leftLowerX+length)/2,leftLowerY+0.2),Point((leftLowerX+leftLowerX+length)/2-0.2,leftLowerY+0.4),Point((leftLowerX+leftLowerX+length)/2-0.1,leftLowerY+0.4),Point((leftLowerX+leftLowerX+length)/2-0.1,leftLowerY+0.8),Point((leftLowerX+leftLowerX+length)/2+0.1,leftLowerY+0.8),Point((leftLowerX+leftLowerX+length)/2+0.1,leftLowerY+0.4),Point((leftLowerX+leftLowerX+length)/2+0.2,leftLowerY+0.4))
        self.arrowHorLeft = Polygon(Point(leftLowerX+0.2,(leftLowerY+leftLowerY+width)/2),Point(leftLowerX+0.4,(leftLowerY+leftLowerY+width)/2-0.2),Point(leftLowerX+0.4,(leftLowerY+leftLowerY+width)/2-0.1),Point(leftLowerX+0.8,(leftLowerY+leftLowerY+width)/2-0.1),Point(leftLowerX+0.8,(leftLowerY+leftLowerY+width)/2+0.1),Point(leftLowerX+0.4,(leftLowerY+leftLowerY+width)/2+0.1),Point(leftLowerX+0.4,(leftLowerY+leftLowerY+width)/2+0.2))
        self.arrowHorRight = Polygon(Point(leftLowerX+length-0.2,(leftLowerY+leftLowerY+width)/2),Point(leftLowerX+length-0.4,(leftLowerY+leftLowerY+width)/2-0.2),Point(leftLowerX+length-0.4,(leftLowerY+leftLowerY+width)/2-0.1),Point(leftLowerX+length-0.8,(leftLowerY+leftLowerY+width)/2-0.1),Point(leftLowerX+length-0.8,(leftLowerY+leftLowerY+width)/2+0.1),Point(leftLowerX+length-0.4,(leftLowerY+leftLowerY+width)/2+0.1),Point(leftLowerX+length-0.4,(leftLowerY+leftLowerY+width)/2+0.2))
        # this is only to the princess Block. Itt's the special characteristic for the princess
        self.princessEye = Circle(Point(19,9),0.15)
        self.princessMouse = Rectangle(Point(18.5,8.5), Point(18.9,8.6))
        self.princessBlusher =  Oval(Point(18.05,8.7), Point(18.4,8.8))

    # this is use to draw the rectangles.
    def draw(self,win):
        self.rectangle.draw(win)
    # the vertical can only move UP and Down
    # if the length is smaller than the width, we know it is a vertical rectangle. 
        if self.length < self.width:
            self.arrowVerUp.draw(win)
            self.arrowVerUp.setFill("black")
            self.arrowVerLow.draw(win)
            self.arrowVerLow.setFill("black")
    # the Horizontal can only move Left and Right
    # if the length is greater than the width, we know it is a Horizontal rectangle. 
        if self.length > self.width:
            self.arrowHorLeft.draw(win)
            self.arrowHorLeft.setFill("black")
            self.arrowHorRight.draw(win)
            self.arrowHorRight.setFill("black")
    # the princess block is the only one that has same Length and width.
        if self.length == self.width:
            self.princessEye.draw(win)
            anotherEye = self.princessEye.clone()
            anotherEye.move(-0.6,0)
            anotherEye.draw(win)
            self.princessEye.setFill("black")
            anotherEye.setFill("black")
            self.princessMouse.draw(win)
            self.princessMouse.setFill("black")
            self.princessBlusher.draw(win)
            anotherBlusher = self.princessBlusher.clone()
            anotherBlusher.move(1,0)
            anotherBlusher.draw(win)
            self.princessBlusher.setFill("darkRed")
            anotherBlusher.setFill("darkRed")
    # when the reactangle moves, every part of it moves
    def moveUp(self,win):
        self.dir = 2
        self.rectangle.move(0,self.dir)
        self.arrowVerUp.move(0,self.dir)
        self.arrowVerLow.move(0,self.dir)
        return self.dir
    # when the reactangle moves, every part of it moves    
    def moveDown(self,win):
        self.dir = -2
        self.rectangle.move(0,self.dir)
        self.arrowVerUp.move(0,self.dir)
        self.arrowVerLow.move(0,self.dir)
        return self.dir
    # when the reactangle moves, every part of it moves    
    def moveLeft(self,win):
        self.dir = -2
        self.rectangle.move(self.dir,0)
        self.arrowHorLeft.move(self.dir,0)
        self.arrowHorRight.move(self.dir,0)
        return self.dir
    # when the reactangle moves, every part of it moves
    def moveRight(self,win):
        self.dir = 2
        self.rectangle.move(self.dir,0)
        self.arrowHorLeft.move(self.dir,0)
        self.arrowHorRight.move(self.dir,0)
        return self.dir

    # those 4 functions are used to GET the values of the Rectangle.           
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def getLeftLowerX(self):
        return self.leftLowerX
    def getLeftLowerY(self):
        return self.leftLowerY



# (FNC) functions of your own design not belonging to any class.
    # This one is giving the values of the Length, width,X ,and Y
def drawBlocks(win):
    # the different names means the differnt blocks. 
    verRecShort = Blocks(2,4,10,8,"darkslateblue")
       
    verRecLong1 = Blocks(2,6,8,2,"darkslateblue")
    
    verRecLong2 = Blocks(2,6,16,6,"darkslateblue")
    
    horRecShort1 = Blocks(4,2,8,12,"firebrick")
    
    horRecShort2 = Blocks(4,2,10,6,"firebrick")
    
    horRecLong1 = Blocks(6,2,12,2,"firebrick")
    
    horRecLong2 = Blocks(6,2,12,12,"firebrick")
    # the values for the hero
    heroo = Hero(4,2,6,8,"cyan")
    # values for the princess
    princess = Blocks(2,2,18,8,"lightcoral")
    princess.draw(win)
    
    return (verRecShort,verRecLong1,verRecLong2,horRecShort1,horRecShort2,horRecLong1,horRecLong2,heroo,princess)




    # the 8 function blow are used to check the mouse, if the mouse located on specific area, then return a number
def verRecShortMove(disVerRecShort,clickedPoint,win):
    clickedPointCheck = clickedPoint
    if 10 <= clickedPointCheck.getX() <= 12 and 10+disVerRecShort < clickedPointCheck.getY() <= 12+disVerRecShort:      
        return 3 # 3 means move up or move left
    elif 10 <= clickedPointCheck.getX() <= 12 and 8+disVerRecShort<= clickedPointCheck.getY() <= 10+disVerRecShort:
        return 4 # 4 means move down or move right 

def verRecLong1Move(disVerRecLong1,clickedPoint,win):
    clickedPointCheck = clickedPoint 
    if 8 <= clickedPointCheck.getX() <= 10 and 5+disVerRecLong1< clickedPointCheck.getY() <= 8+disVerRecLong1:
        return 3
    elif 8 <= clickedPointCheck.getX() <= 10 and 2+disVerRecLong1<= clickedPointCheck.getY() <= 5+disVerRecLong1:        
        return 4
    
def verRecLong2Move(disVerRecLong2,clickedPoint,win):    
    clickedPointCheck = clickedPoint
    if 16 <= clickedPointCheck.getX() <= 18 and 9+disVerRecLong2< clickedPointCheck.getY() <= 12+disVerRecLong2:
        return 3
    elif 16 <= clickedPointCheck.getX() <= 18 and 6+disVerRecLong2<= clickedPointCheck.getY() <= 9+disVerRecLong2:      
        return 4
    
def horRecShort1Move(disHorRecShort1,clickedPoint,win):
    clickedPointCheck = clickedPoint        
    if 8+disHorRecShort1 <= clickedPointCheck.getX() < 10+disHorRecShort1 and 12<= clickedPointCheck.getY() <= 14:      
        return 3
    elif 10+disHorRecShort1 <= clickedPointCheck.getX() <= 12+disHorRecShort1 and 12<= clickedPointCheck.getY() <= 14:       
        return 4
                
def horRecShort2Move(disHorRecShort2,clickedPoint,win):
    clickedPointCheck = clickedPoint
    if 10+disHorRecShort2 <= clickedPointCheck.getX() < 12+disHorRecShort2 and 6<= clickedPointCheck.getY() <= 8:   
        return 3 # 3 means move up or move left
    elif 12+disHorRecShort2 <= clickedPointCheck.getX() <= 14+disHorRecShort2 and 6<= clickedPointCheck.getY() <= 8:        
        return 4 #4 means move down or move right

def horRecLong1Move(disHorRecLong1,clickedPoint,win):
    clickedPointCheck = clickedPoint           
    if 12+disHorRecLong1 <= clickedPointCheck.getX() < 15+disHorRecLong1 and 2<= clickedPointCheck.getY() <= 4:
        return 3
    elif 15+disHorRecLong1 <= clickedPointCheck.getX() <= 18+disHorRecLong1 and 2<= clickedPointCheck.getY() <= 4:       
        return 4
        
def horRecLong2Move(disHorRecLong2,clickedPoint,win):
    clickedPointCheck = clickedPoint
    if 12+disHorRecLong2 <= clickedPointCheck.getX() < 15+disHorRecLong2 and 12<= clickedPointCheck.getY() <= 14:    
        return 3
    elif 15+disHorRecLong2 <= clickedPointCheck.getX() <= 18+disHorRecLong2 and 12<= clickedPointCheck.getY() <= 14:      
        return 4

def heroMovement(disHero,clickedPoint,win):
    clickedPointCheck = clickedPoint   
    if 6+disHero <= clickedPointCheck.getX() <= 8+disHero and 8 <= clickedPointCheck.getY() <= 10:
        return 3
    elif 8+disHero <= clickedPointCheck.getX() < 10+disHero and 8 <= clickedPointCheck.getY() <= 10:
        return 4

# this is most important function of the game.
# this calls the function to check how to move
# it calls function check the valid moves
# it draws the rectangles 
def gamesteps(win):

    # this is to lunch the Luck Draw. 
    spin = LuckDraw(win)

    # to get the values of all the squares, from the drawBlocks. 
    theBlocks = drawBlocks(win)
    (verRecShort,verRecLong1,verRecLong2,horRecShort1,horRecShort2,horRecLong1,horRecLong2,heroo,princess) = drawBlocks(win)

    # draw the rectangles 
    verRecShort.draw(win)
    verRecLong1.draw(win)
    verRecLong2.draw(win)
    horRecShort1.draw(win)
    horRecShort2.draw(win)
    horRecLong1.draw(win)
    horRecLong2.draw(win)
    heroo.drawHero(win)

    # those are the distance that the blocks have already moved 
    distanceVerRecShort = 0
    distanceVerRecLong1= 0 
    distanceVerRecLong2 = 0
    distanceHorRecShort1 = 0
    distanceHorRecShort2  = 0
    distanceHorRecLong1 = 0
    distanceHorRecLong2 = 0
    distanceHero = 0    
    dirUpDown = 0
    dirLR = 0 

    # the total possible number of clicks
    # the spin means the extra clicks from the Lucky Draw.
    
    clicks = 30+spin

    # we give the player 999 times to click around, to click everything, But nothing will happen. 
    for i in range(999):    
        clickedPoint = win.getMouse()
        if clicks > 0: # make sure that when the player run out of clicks, no more move.
            if verRecShortMove(distanceVerRecShort,clickedPoint,win) == 3: # the 3 is from the pervious functions that tells us the direction of the movement.
                # checkVerticalMoveValid is to make sure the move will not go over the edges of the game board
                # the occupation is to check if the spots have been taken by other rectangle. 
                if checkVerticalMoveValid(verRecShort,distanceVerRecShort,clickedPoint) == True and occupation("1",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:                            
                    dirUpDown = verRecShort.moveUp(win) # move the rectangle up
                    distanceVerRecShort += dirUpDown  # tracking the distance that the block moved 
                    clicks -= 1 # clicks chance -1 
                                                    
            elif verRecShortMove(distanceVerRecShort,clickedPoint,win) == 4:
                if checkVerticalMoveValid(verRecShort,distanceVerRecShort,clickedPoint) == True and occupation("2",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:             
                    dirUpDown = verRecShort.moveDown(win)
                    distanceVerRecShort += dirUpDown
                    clicks -= 1
                           
            elif verRecLong1Move(distanceVerRecLong1,clickedPoint,win) == 3:
                if checkVerticalMoveValid(verRecLong1,distanceVerRecLong1,clickedPoint) == True and occupation("3",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirUpDown = verRecLong1.moveUp(win)
                    distanceVerRecLong1 += dirUpDown
                    clicks -= 1
                    
            elif verRecLong1Move(distanceVerRecLong1,clickedPoint,win) == 4:
                if checkVerticalMoveValid(verRecLong1,distanceVerRecLong1,clickedPoint) == True and occupation("4",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirUpDown = verRecLong1.moveDown(win)
                    distanceVerRecLong1 += dirUpDown
                    clicks -= 1
                 
            elif verRecLong2Move(distanceVerRecLong2,clickedPoint,win) == 3:
                if checkVerticalMoveValid(verRecLong2,distanceVerRecLong2,clickedPoint) == True and occupation("5",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirUpDown = verRecLong2.moveUp(win)
                    distanceVerRecLong2 += dirUpDown
                    clicks -= 1
                    
            elif verRecLong2Move(distanceVerRecLong2,clickedPoint,win) == 4:
                if checkVerticalMoveValid(verRecLong2,distanceVerRecLong2,clickedPoint) == True and occupation("6",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirUpDown = verRecLong2.moveDown(win)
                    distanceVerRecLong2 += dirUpDown
                    clicks -= 1
                    
            elif horRecShort1Move(distanceHorRecShort1,clickedPoint,win) == 3:
                if checkHorizontalMoveValid(horRecShort1,distanceHorRecShort1,clickedPoint) == True and occupation("7",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecShort1.moveLeft(win)
                    distanceHorRecShort1 += dirLR
                    clicks -= 1
                    
            elif horRecShort1Move(distanceHorRecShort1,clickedPoint,win) == 4:
                if checkHorizontalMoveValid(horRecShort1,distanceHorRecShort1,clickedPoint) == True and occupation("8",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecShort1.moveRight(win)
                    distanceHorRecShort1 += dirLR
                    clicks -= 1
                
            elif horRecShort2Move(distanceHorRecShort2,clickedPoint,win) == 3:
                if checkHorizontalMoveValid(horRecShort2,distanceHorRecShort2,clickedPoint) == True and occupation("9",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecShort2.moveLeft(win)
                    distanceHorRecShort2 += dirLR
                    clicks -= 1
            elif horRecShort2Move(distanceHorRecShort2,clickedPoint,win) == 4:
                if checkHorizontalMoveValid(horRecShort2,distanceHorRecShort2,clickedPoint) == True and occupation("10",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecShort2.moveRight(win)
                    distanceHorRecShort2 += dirLR
                    clicks -= 1
        
            elif horRecLong1Move(distanceHorRecLong1,clickedPoint,win) == 3:
               if  checkHorizontalMoveValid(horRecLong1,distanceHorRecLong1,clickedPoint) == True and occupation("11",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecLong1.moveLeft(win)
                    distanceHorRecLong1 += dirLR
                    clicks -= 1
            elif horRecLong1Move(distanceHorRecLong1,clickedPoint,win) == 4:
                if checkHorizontalMoveValid(horRecLong1,distanceHorRecLong1,clickedPoint) == True and occupation("12",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecLong1.moveRight(win)
                    distanceHorRecLong1 += dirLR
                    clicks -= 1
        
            elif horRecLong2Move(distanceHorRecLong2,clickedPoint,win) == 3:
                if  checkHorizontalMoveValid(horRecLong2,distanceHorRecLong2,clickedPoint) == True and occupation("13",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecLong2.moveLeft(win)
                    distanceHorRecLong2 += dirLR
                    clicks -= 1
            elif horRecLong2Move(distanceHorRecLong2,clickedPoint,win) == 4:
                if  checkHorizontalMoveValid(horRecLong2,distanceHorRecLong2,clickedPoint) == True and occupation("14",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = horRecLong2.moveRight(win)
                    distanceHorRecLong2 += dirLR
                    clicks -= 1
   
            elif heroMovement(distanceHero,clickedPoint,win) == 3:
                if checkHorizontalMoveValid(heroo,distanceHero,clickedPoint) == True and occupation("15",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False: 
                    dirLR = heroo.heroMoveLeft(win)
                    distanceHero += dirLR
                    clicks -= 1
            elif heroMovement(distanceHero,clickedPoint,win) == 4:
                if  checkHorizontalMoveValid(heroo,distanceHero,clickedPoint) == True and occupation("16",distanceVerRecShort,distanceVerRecLong1,distanceVerRecLong2,distanceHorRecShort1,distanceHorRecShort2,distanceHorRecLong1,distanceHorRecLong2,distanceHero) != False:
                    dirLR = heroo.heroMoveRight(win)
                    distanceHero += dirLR
                    clicks -= 1
                    if checkWin(heroo,distanceHero) == True: # if the hero reach the win point. WON!! 
                        changeSteps(win,clicks)
                        theWinImage(win)
                        return clicks # then we return how many moves we used
                        break # break from the 999 times loop                        
            changeSteps(win,clicks)
            
        else:                             
            theLoseImage(win) # if the clicks is less or equal to 0, break fromt the loop and display the lose Image. 
            return clicks
            break
        
        
#(OTXT)           interactive output using Text
# this is to draw the steps left to the window. 
def draw_Steps(win):
    stepText = Text(Point(2,23),"Steps Left: ")
    stepText.setSize(20)
    stepText.setTextColor("darkslategray")
    stepText.setStyle("bold")
    steps_left = Text(Point(4,23),"30")
    steps_left.setTextColor("darkslategray")
    steps_left.setSize(20)
    steps_left.setStyle("bold")
    stepText.draw(win)
    steps_left.draw(win)

# we change the clicks numbers everytime, when their is a valid move   
def changeSteps(win,clicks):
# the cover is use to cover the old number 
    cover = Rectangle(Point(3.5,22.5),Point(6,23.5))
    cover.setFill("silver")
    cover.setOutline("silver")
    cover.draw(win)
    steps = Text(Point(4,23),clicks)
    steps.setTextColor("darkslategray")
    steps.setSize(20)
    steps.setStyle("bold")
    steps.draw(win)

# this function is use to display the lose image to the player for 1.5 sec, when they lose
def theLoseImage(win):
    loseImage = Image(Point(12,10),"lose.gif")
    loseImage.draw(win)
    time.sleep(1.5)
    loseImage.undraw()  
# this function is use to display the win image to the player for 1.5 sec, when they win
def theWinImage(win):
    winImage = Image(Point(12,10),"won.gif")
    winImage.draw(win)
    time.sleep(1.5)
    winImage.undraw()    

# to check the move is over the game board,if so Flase, if in the board, then this is a valid move
def checkVerticalMoveValid(blockName,getDistance,clickedPoint):
    
    pY = blockName.getLeftLowerY() + getDistance
    pY2 = blockName.getLeftLowerY() + blockName.getWidth() + getDistance
    # the Y-axis for top and bottom are 14 and 12
    if pY >2  and pY2 < 14: 
        return True
    elif pY2 == 14 and clickedPoint.getY() <= pY2 - blockName.getWidth()/2:
        return True
    elif pY == 2 and clickedPoint.getY() >= pY2 - blockName.getWidth()/2:
        return True

# to check the move is over the game board,if so Flase, if in the board, then this is a valid move
def checkHorizontalMoveValid(blockName,getDistance,clickedPoint):
     
    pX = blockName.getLeftLowerX()+ + getDistance
    pX2 = blockName.getLeftLowerX() + blockName.getLength() + getDistance
    # the X-axis for left and right are 6 and 18
    if pX >6  and pX2 < 18: 
        return True
    elif pX == 6 and clickedPoint.getX() >= pX2 - blockName.getLength()/2:
        return True
    elif pX2 == 18 and clickedPoint.getX() <= pX2 - blockName.getLength()/2:
        return True

# if the hero Block reaches X-axis = 18 then you WIN !!!!
def checkWin(heroBlock,heroMoved):
    pX = heroBlock.getLeftLowerX() + heroBlock.getLength() + heroMoved
    if pX == 18:
        return True
    else:
        return False
    
# (FNC) functions of your own design not belonging to any class.
def occupation(blockNum,movementVerRecShort,movementVerRecLong1,movementVerRecLong2,movementHorRecShort1,movementHorRecShort2,movementHorRecLong1,movementHorRecLong2,movementHero): 
# assuming that every square is a little spot, so we have 6 x 6 = 36 spots
# is their is a square on the spot, invalid move.
    
    moveUp = 1  # when move up, the y-axis +1. same idea for the rest
    moveDown = -1
    moveLeft = -1
    moveRight = 1

    # this list is to collect all the spot that has been occupated.
    # some rectangle might use 2 spots, some might use 3.
    aList = []  
    aList.append((3,4+int(movementVerRecShort/2)))#(verRecShortP1)
    aList.append((3,5+int(movementVerRecShort/2)))#(verRecShortP2)    
    aList.append((2,1+int(movementVerRecLong1/2)))#(verRecLong1P1)
    aList.append((2,2+int(movementVerRecLong1/2)))#(verRecLong1P2)
    aList.append((2,3+int(movementVerRecLong1/2)))#(verRecLong1P3)   
    aList.append((6,3+int(movementVerRecLong2/2)))#(verRecLong2P1)
    aList.append((6,4+int(movementVerRecLong2/2)))#(verRecLong2P2)
    aList.append((6,5+int(movementVerRecLong2/2)))#(verRecLong2P3)  
    aList.append((2+int(movementHorRecShort1/2),6))#(horRecShort1P1)
    aList.append((3+int(movementHorRecShort1/2),6))#(horRecShort1P2)   
    aList.append((3+int(movementHorRecShort2/2),3))#(horRecShort2P1)
    aList.append((4+int(movementHorRecShort2/2),3))#(horRecShort2P2)    
    aList.append((4+int(movementHorRecLong1/2),1))#(horRecLong1P1)
    aList.append((5+int(movementHorRecLong1/2),1))#(horRecLong1P2)
    aList.append((6+int(movementHorRecLong1/2),1))#(horRecLong1P3)    
    aList.append((4+int(movementHorRecLong2/2),6))#(horRecLong2P1)
    aList.append((5+int(movementHorRecLong2/2),6))#(horRecLong2P2)
    aList.append((6+int(movementHorRecLong2/2),6))#(horRecLong2P3)    
    aList.append((1+int(movementHero/2),4))#(herooP1)
    aList.append((2+int(movementHero/2),4))#(herooP2)

    
    if blockNum == "1":# this is the identifier from the call. is to identify the stop of itself.
        del aList[0:2] # delate itself's spot
        checkObject1 = (3,4+int(movementVerRecShort/2)+moveUp) # check if move up, is the spot been taken, 
        checkObject2 = (3,5+int(movementVerRecShort/2)+moveUp)
        if checkObject1 in aList: # if so, False,invalid move 
            return False
        elif checkObject2 in aList:
            return False
    
    elif blockNum == "2":
        del aList[0:2]
        checkObject1 = (3,4+int(movementVerRecShort/2)+moveDown) # check if move Down, is the spot been taken.  
        checkObject2 = (3,5+int(movementVerRecShort/2)+moveDown) # same idea for the rest 
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        
    elif blockNum == "3":
        del aList[2:5]
        checkObject1 = (2,1+int(movementVerRecLong1/2)+moveUp)
        checkObject2 = (2,2+int(movementVerRecLong1/2)+moveUp)
        checkObject3 = (2,3+int(movementVerRecLong1/2)+moveUp)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
    
    elif blockNum == "4":
        del aList[2:5]
        checkObject1 = (2,1+int(movementVerRecLong1/2)+moveDown)
        checkObject2 = (2,2+int(movementVerRecLong1/2)+moveDown)
        checkObject3 = (2,3+int(movementVerRecLong1/2)+moveDown)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False

    elif blockNum == "5":
        del aList[5:8]
        checkObject1 = (6,3+int(movementVerRecLong2/2)+moveUp)
        checkObject2 = (6,4+int(movementVerRecLong2/2)+moveUp)
        checkObject3 = (6,5+int(movementVerRecLong2/2)+moveUp)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
        
    elif blockNum == "6":
        del aList[5:8]
        checkObject1 = (6,3+int(movementVerRecLong2/2)+moveDown)
        checkObject2 = (6,4+int(movementVerRecLong2/2)+moveDown)
        checkObject3 = (6,5+int(movementVerRecLong2/2)+moveDown)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False

    elif blockNum == "7":
        del aList[8:10]
        checkObject1 = (2+int(movementHorRecShort1/2)+moveLeft,6)
        checkObject2 = (3+int(movementHorRecShort1/2)+moveLeft,6)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        
    elif blockNum == "8":
        del aList[8:10]
        checkObject1 = (2+int(movementHorRecShort1/2)+moveRight,6)
        checkObject2 = (3+int(movementHorRecShort1/2)+moveRight,6)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        
    elif blockNum == "9":
        del aList[10:12]
        checkObject1 = (3+int(movementHorRecShort2/2)+moveLeft,3)
        checkObject2 = (4+int(movementHorRecShort2/2)+moveLeft,3)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        
    elif blockNum == "10":
        del aList[10:12]
        checkObject1 = (3+int(movementHorRecShort2/2)+moveRight,3)
        checkObject2 = (4+int(movementHorRecShort2/2)+moveRight,3)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        
    elif blockNum == "11":
        del aList[12:15]
        checkObject1 = (4+int(movementHorRecLong1/2)+moveLeft,1)
        checkObject2 = (5+int(movementHorRecLong1/2)+moveLeft,1)
        checkObject3 = (6+int(movementHorRecLong1/2)+moveLeft,1)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
 
    elif blockNum == "12":
        del aList[12:15]
        checkObject1 = (4+int(movementHorRecLong1/2)+moveRight,1)
        checkObject2 = (5+int(movementHorRecLong1/2)+moveRight,1)
        checkObject3 = (6+int(movementHorRecLong1/2)+moveRight,1)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
        
    elif blockNum == "13":
        del aList[15:18]
        checkObject1 = (4+int(movementHorRecLong2/2)+moveLeft,6)
        checkObject2 = (5+int(movementHorRecLong2/2)+moveLeft,6)
        checkObject3 = (6+int(movementHorRecLong2/2)+moveLeft,6)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
        
    elif blockNum == "14":
        del aList[15:18]
        checkObject1 = (4+int(movementHorRecLong2/2)+moveRight,6)
        checkObject2 = (5+int(movementHorRecLong2/2)+moveRight,6)
        checkObject3 = (6+int(movementHorRecLong2/2)+moveRight,6)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
        elif checkObject3 in aList:
            return False
        
    elif blockNum == "15":
        del aList[18:]
        checkObject1 = (1+int(movementHero/2)+moveLeft,4)
        checkObject2 = (2+int(movementHero/2)+moveLeft,4)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False
    
    elif blockNum == "16":
        del aList[18:]
        checkObject1 = (1+int(movementHero/2)+moveRight,4)
        checkObject2 = (2+int(movementHero/2)+moveRight,4)
        if checkObject1 in aList:
            return False
        elif checkObject2 in aList:
            return False

# this function use to draw the Lucky Draw. 
# (FNC) functions of your own design not belonging to any class.

# those are teh arrow that will show and indicating the prize that the player will get.
def LuckDraw(win):
    theArrow1 = Line(Point(20,20),Point(20,22))
    theArrow1.setArrow("last")
    theArrow4 = Line(Point(20,20),Point(20+math.sqrt(2),20+math.sqrt(2)))
    theArrow4.setArrow("last")
    theArrow5 = Line(Point(20,20),Point(22,20))
    theArrow5.setArrow("last")
    theArrow2 = Line(Point(20,20),Point(20+math.sqrt(2),20-math.sqrt(2)))
    theArrow2.setArrow("last")
    theArrow6 = Line(Point(20,20),Point(20,18))
    theArrow6.setArrow("last")
    theArrow3 = Line(Point(20,20),Point(20-math.sqrt(2),20-math.sqrt(2)))
    theArrow3.setArrow("last")
    theArrow7 = Line(Point(20,20),Point(18,20))
    theArrow7.setArrow("last")
    theArrow8 = Line(Point(20,20),Point(20-math.sqrt(2),20+math.sqrt(2)))
    theArrow8.setArrow("last")

    # this is the animation that I made, to make a idea of it really just spinning. 
    for i in range(3):        
        theArrow1.draw(win)
        time.sleep(.1)
        theArrow1.undraw()
        time.sleep(.1)
        theArrow5.draw(win)
        time.sleep(.1)
        theArrow5.undraw()
        time.sleep(.1)
        theArrow3.draw(win)
        time.sleep(.1)
        theArrow3.undraw()
        time.sleep(.1)
        theArrow2.draw(win)
        time.sleep(.1)
        theArrow2.undraw()
        time.sleep(.1)
        theArrow8.draw(win)
        time.sleep(.1)
        theArrow8.undraw()
        time.sleep(.1)
        theArrow6.draw(win)
        time.sleep(.1)
        theArrow6.undraw()
        time.sleep(.1)
        theArrow7.draw(win)
        time.sleep(.1)
        theArrow7.undraw()
        time.sleep(.1)
        theArrow4.draw(win)
        time.sleep(.1)
        theArrow4.undraw()
        time.sleep(.1)
    # make no sence when stop at the bottom or the 2 lines of the circle.
    # so we only count from arrow 4 to 9
#(RND)   some randomness using the random class.
    random = randrange(4,9)  # when the arrow stops at 4, the total clicks + 3
    if random == 4:
        theArrow4.draw(win)
        showThe3StepsAdded(win) # this is to call the fuction that will show the steps are really added to the total steps. 
        return int(3)
        
    elif random == 5: # when the arrow stops at 5, the total clicks + 3
        theArrow5.draw(win)
        showThe3StepsAdded(win)
        return int(3)
        
    elif random == 6: # when the arrow stops at 6, the total clicks + 0     No prize
        theArrow6.draw(win)
        return int(0)
        
    elif random == 7: # when the arrow stops at 7, the total clicks + 6
        theArrow7.draw(win)
        showThe6StepsAdded(win)
        return int(6)
        
    elif random == 8: # when the arrow stops at 8, the total clicks + 6
        theArrow8.draw(win)
        showThe6StepsAdded(win)
        return int(6)

# Those 2 fucntion are drawing on window to show the prize.    
def showThe6StepsAdded(win):
    text = Text(Point(4.8,23),"+ 6")
    text.setSize(20)
    text.draw(win).setTextColor("darkslategray")    
def showThe3StepsAdded(win):    
    text = Text(Point(4.8,23),"+ 3")
    text.setSize(20)
    text.draw(win).setTextColor("darkslategray")
    
# this fuction is to draw the Lukcy draw infomations on the Window       
def luckyDrawText(win):
    prize1 = Text(Point(20-math.sqrt(2)+0.6,20+math.sqrt(2)-0.5),"STEPS")
    prize1P = Text(Point(20-math.sqrt(2)+0.6,20+math.sqrt(2)-0.9),"+6")
    prize2 = Text(Point(20+math.sqrt(2)-0.6,20+math.sqrt(2)-0.5),"STEPS")
    prize2P = Text(Point(20+math.sqrt(2)-0.6,20+math.sqrt(2)-0.9),"+3")
    prize3 = Text(Point(20,20-1.1)," Better Luck")
    prize3P = Text(Point(20,20-1.5)," Next Time")
    
    prize1.draw(win).setOutline("darkslategray")# 6 more steps
    prize2.draw(win).setOutline("darkslategray")# 3 more steps
    prize3.draw(win).setOutline("darkslategray")# no prize
    prize1P.draw(win).setOutline("darkslategray")
    prize2P.draw(win).setOutline("darkslategray")
    prize3P.draw(win).setOutline("darkslategray")
    
    

# This is to draw the botton of the lucky draw, if the user lick the botton, it will draw.        
def LuckyDrawStartBottom(win):
    # draw the wheel
    theWheel = Circle(Point(20,20),2)
    theWheel.draw(win).setFill("lightgrey")
    theWheel.setOutline("lightgrey")
    # draw the middle point of the Lucky Draw
    theMidPoint = Circle(Point(20,20),0.1)
    theMidPoint.draw(win).setFill("darkslategray")
    theMidPoint.setOutline("darkslategray")
    # draw the seperation Lines
    theSeperatingLine1 = Line(Point(20,20),Point(20+math.sqrt(2),20-math.sqrt(2)))
    theSeperatingLine2 = Line(Point(20,20),Point(20-math.sqrt(2),20-math.sqrt(2)))
    theSeperatingLine3 = Line(Point(20,20),Point(20,22))
    theSeperatingLine1.draw(win).setOutline("darkslategray")
    theSeperatingLine2.draw(win).setOutline("darkslategray")
    theSeperatingLine3.draw(win).setOutline("darkslategray")
    box = Rectangle(Point(19,16.5),Point(21,17.5))
    box.draw(win).setFill("dimgray")
    box.setOutline("dimgray")
    #draw the message informations
    messageStart = Text(Point(20,17),"S T A R T")
    messageStart.draw(win)

    

def playerName(win):
    # this is the fuction that get the user's name by the input
    # those drawing all of the informations that we need.
    theNameBox = Circle(Point(15.5,20),2)
    theNameBox.draw(win).setFill("lightgrey")
    theNameBox.setOutline("lightgrey")
    name = Rectangle(Point(14.5,16.5),Point(16.5,17.5))
    name.draw(win).setFill("dimgray")
    name.setOutline("dimgray")
    Nameinput = Text(Point(15.5,17),"CONFIRM")
    Nameinput.draw(win)
    playerInfo = Text(Point(15.5,20.6),"Player:")
    playerInfo.setSize(20)
    playerInfo.draw(win).setOutline("darkslategray")
#(IEB)   interactive input using Entry boxes
    entryBox = Entry(Point(15.5,19.4),10)
    entryBox.draw(win).setText("Your Name")
    return entryBox

    # this function is used to get the name. and use it as a value. 
def getPlayerName(entryBox):       
    nameValue = entryBox.getText()
    return nameValue

    # draw the quit botton
def quitButton(win):
    button = Rectangle(Point(22,0),Point(24,2))
    button.draw(win).setFill("lightgrey")
    button.setOutline("lightgrey")
    buttonText = Text(Point(23,1),"Quit")
    buttonText.draw(win).setOutline("darkslategray")

    # click the quit botton then quit the game. 
def quitGame(win):
    win.close()
    
#(CLOD)  At least one class of your own design with objects and methods that are used.
    # this class is drawing the instuctions and reset the insructions. 
class Instruction():
    def __init__(self,text): # get text from main()
        self.text = text
        self.outline = Rectangle(Point(8.5,17),Point(12.5,21.5))
        self.outline.setOutline("lightgrey")
        self.defaultText = Text(Point(10.5,20.1), "INSTRUCTION:")
        self.printText = Text(Point(10.5,18.7),self.text)
    # draw it    
    def drawInstruction(self,win):
        self.outline.draw(win).setWidth(30)
        self.defaultText.draw(win).setFill("darkslategray")
        self.printText.draw(win).setFill("darkslategray")
    # we need to clear the pervious text
    def clear(self):
        self.printText.setText(" ")



# this is to draw the deader Board and sort it by the steps left, then print to outfile also print to the window.
#(CLOD)  At least one class of your own design with objects and methods that are used.
class LeaderBoard:
    def __init__(self,name,step):
        self.name = name
        self.step = int(step)
    # draw the leader Board, and make the outfile.  
    def display(self,win,part):
        
        text_LeaderBoard = Text(Point(3,12),"LEADERBOARD\nTHE TOP 3")
    
        # part 1,2,3 are indicating the top 1,2,or 3. three different positions.
        if part == 1:          
            text_N = Text(Point(2.5,11),self.name)
            text_S = Text(Point(3.5,11),str(self.step))
#(OFL) a text output file            
            outfile = open("saved_record.txt","w")
            print(self.name+"\t"+str(self.step),file=outfile)
            outfile.close
 
        elif part == 2:            
            text_N = Text(Point(2.5,10),self.name)
            text_S = Text(Point(3.5,10),str(self.step))
               
            outfile = open("saved_record.txt","a")
            outfile.write(self.name+"\t"+str(self.step))
            outfile.close
            

        elif part == 3:
            text_N = Text(Point(2.5,9),self.name)
            text_S = Text(Point(3.5,9),str(self.step))
               
            outfile = open("saved_record.txt","a")
            outfile.write("\n"+self.name+"\t"+str(self.step))
            outfile.close
            
        text_LeaderBoard.draw(win)
        text_N.draw(win)
        text_S.draw(win)      
    # get the steps and return the value  
    def getSteps(self):
        return self.step
    # split the file, and split the name and steps. 
def make_the_record(line):
    terms = line.split("\t")
    separate_info = LeaderBoard(terms[0],terms[1])
    return separate_info 
def useSteps(aRecord):
    return aRecord.getSteps()
    # read the file, append the information to the list,sort it. then draw it to player. 
def modify_the_file(name,record,win):
    
    oldrecord = []
    newName = name
    newRecord = str(record) 
#(IFL)   a text input file
    infile = open("saved_record.txt","r") #open file
    for line in infile: #read file
        info = make_the_record(line)     
        oldrecord.append(info)  # appent to list     
    infile.close # close file
    
    newline = (newName+"\t"+newRecord) # the new record from this game, add it to the list
    pendingRecord = make_the_record(newline)
    oldrecord.append(pendingRecord)
        
    oldrecord.sort(key=useSteps,reverse=True) # sort the list from big to small.
    oldrecord.pop(-1)# pop the last number,so the txt always have 3 lines only. 
    
    part = 0 # part is indicating the position of different player. because we need to draw it to different position, 
    for i in oldrecord:
        part+=1
        i.display(win,part)
        
        
            
 
# (29 lines)
def main():

    win = setWin() # draw window
    drawBoard = mainBackBoard(win) # draw the game board
    name = playerName(win) # get player name
    quitButton(win) # draw the quit button 
    ins_message = Instruction("Insert player name")  # draw instruction
    ins_message.drawInstruction(win)
    draw_Steps(win) # draw the steps left.
    
# (IMS) mouse input making use of the location of the mouse click.   
    for possibleclick in range(999): #gives 999 chance to click what ever you want, but there is only one place you clicked and workd
        possibleclick = win.getMouse() 
        
        if 14.5 <= possibleclick.getX() <= 16.5 and 16.5 <= possibleclick.getY() <= 17.5: # clicked in here then lunch the rest of game
            nameToRecord = getPlayerName(name) # get the name from player(use this latter)
            # change the instruction
            ins_message.clear()           
            ins_message = Instruction("Click Start\nfor Lucky Draw")
            ins_message.drawInstruction(win)
            # lunch the lucky Draw
            drawTheLuckyDraw = LuckyDrawStartBottom(win)
            # draw the prize to the window,so the player can see it.
            luckyDrawText(win)
        
        elif 19 <= possibleclick.getX() <= 21 and 16.5 <= possibleclick.getY() <= 17.5:
            # draw the blocks
            block = drawBlocks(win)
            # change instructions
            ins_message.clear()
            ins_message = Instruction("Rescure\nThe princess")
            ins_message.drawInstruction(win)
            # start to play the game!
            stepsLeftToRecord = gamesteps(win)
            # change instructions
            ins_message.clear()
            ins_message = Instruction("Click Quit")
            ins_message.drawInstruction(win)
            if int(stepsLeftToRecord)>0:# if the steps is more than 0 print the leader board
                # modify the file
                modify_the_file(nameToRecord,stepsLeftToRecord,win)
                
        # if clicked at here, quit the game.
        elif 22 <= possibleclick.getX() <= 24 and 0 <= possibleclick.getY() <= 2:
            break  
    quitGame(win) # quit the game
    
main()





