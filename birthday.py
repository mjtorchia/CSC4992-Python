from package import *
from turtle import Turtle
brush1=Turtle()
HOUSEBASE=300
HOUSEHEIGHT=250
startPoint=(-100,-100)
brush1.speed("fastest")
#Needs a lot of refactoring to make more abstract. Less hard coding

class Polygon(object):
    """Basic Class for defining chracteristics of a shape.
created with "number of sides",fill color, and pen color.
Example: myShape=Polygon(4,"red","blue")
Default values will be assigned to fill color and pen color if not specified

Functions:
inputSides() - Promts the user for length of each side
dispSides() - Displays sides to the screen"""
    def __init__(self,numOfSides,fill="",pen="black"):
        self.n=numOfSides
        self.sides=[0 for i in range(numOfSides)]
        self.fillColor=str(fill)
        self.penColor=str(pen)
    def inputSides(self):
        for i in range(self.n):
            self.edges=float(input("Enter Edge "+str(i+1)+" : "))
            self.sides[i]=self.edges
    def dispSides(self):
        for i in range(self.n):
            print("edge",i+1,"is",self.sides[i])

class Triangle(Polygon):
    """Class used to represent a triangle shape
Created with 3 tuples representing each point of the triangle (left,right,top), a fill color and pen color
Example: myTri=Triangle((1,1),(2,2),(3,3))
If the object is not specified points in the constructor, default values will be assigned

Functions:
    accessors for each point:
    getLeft(),getRight(),getTop()
drawRoof(turtle) - draws the roof for the house

    """
    def __init__(self,left=(0,0),right=(0,4),top=(2,4),fill="",pen="black"):
        super().__init__(3,fill,pen)
        self._left=left
        self._right=right
        self._top=top
    def __str__(self):
        return ('Left Point =' +str(self._left)+'\n'+'Right Point =' +str(self._right)+
                '\n'+'Top Point ='+str(self._top)+'\n'+'Fill Color ='+self.fillColor+'\n'
                +'Pen Color ='+self.penColor)
    def getLeft(self):
        return self._left
    def getRight(self):
        return self._right
    def getTop(self):
        return self._top
    def drawRoof(self,brush):
        brush.goto(self._right)
        brush.fillcolor(self.fillColor)
        brush.begin_fill()
        brush.down()
        brush.goto(self._top)
        brush.goto(self._left)
        brush.end_fill()
        brush.up()
        
class Rectangle(Polygon):
    """Class used to represent a rectangle shape
Created with 2 tuples representing the lower left point of the
rectangle and the upper right point, a fill color and pen color
Example: myRect=Rectangle((0,0),(5,5))
If not specified default values will be assigned.

Functions:
    accessors for each point:
    getLLeft(),getURight()
drawWindow(turtle) - draws a window on the house
drawHouse(turtle) - draws the "base" of the house
drawDoor(trutle) - draws the door on the house"""
    def __init__(self,lLeft=(0,0),uRight=(4,3),fill="",pen="black"):
        super().__init__(4,fill,pen)
        self._lLeft=lLeft
        self._uRight=uRight
    def __str__(self):
        return('Lower Left Point ='+str(self._lLeft)+'\n'+'Upper Right Ponit ='+str(self._uRight)+
               '\n'+'Fill Color ='+self.fillColor+'\n'
                +'Pen Color ='+self.penColor)
    def getLLeft(self):
        return self._lLeft
    def getURight(self):
        return self._uRight
    def drawWindow(self,brush):
        brush.up()
        brush.goto(self._lLeft)
        brush.fillcolor(self.fillColor)
        brush.begin_fill()
        brush.down()
        brush.goto(self._uRight[0],self._lLeft[1])
        brush.goto(self._uRight)
        brush.goto(self._lLeft[0],self._uRight[1])
        brush.goto(self._lLeft)
        brush.end_fill()
        brush.up()
        if self._lLeft[0]>200:
            brush.goto(45.25,190.75)
            brush.setheading(270)
            brush.down()
            brush.fillcolor("red")
            brush.begin_fill()
            brush.circle(30,180)
            brush.end_fill()
            brush.up()
            brush.setheading(90)
        brush.goto(195,190.6)
        brush.setheading(270)
        brush.down()
        brush.fillcolor("red")
        brush.begin_fill()
        brush.circle(30,180)
        brush.end_fill()
        brush.up()
        brush.setheading(90)
        
    def drawHouse(self,brush):
        brush.goto(self._uRight[0],0)
        brush.fillcolor(self.fillColor)
        brush.begin_fill()
        brush.goto(self._uRight)
        brush.goto(0,self._uRight[1])
        brush.goto(self._lLeft)
        brush.end_fill()
        brush.fillcolor()
        brush.up()
    def drawDoor(self,brush):
        brush.goto(self._lLeft)
        brush.fillcolor(self.fillColor)
        brush.begin_fill()
        brush.down()
        brush.goto(self._uRight[0],self._lLeft[1])
        brush.goto(self._uRight)
        brush.goto(self._lLeft[0],self._uRight[1])
        brush.goto(self._lLeft)
        brush.end_fill()
        brush.up()
    def drawSky(self,brush):
        brush.goto(self._lLeft)
        brush.fillcolor(self.fillColor)
        brush.begin_fill()
        brush.down()
        brush.goto(self._uRight[0],self._lLeft[1])
        brush.goto(self._uRight)
        brush.goto(self._lLeft[0],self._uRight[1])
        brush.goto(self._lLeft)
        brush.end_fill()
        brush.up()

class Circle():
    """Class used to represent the circle class
Created with one tuple for the center and one float value for the radius, a fill color and pen color
Example: myCir=Circle((1,1),3.14)

Functions:
    accessors for center and radius:
    getRadius(),getCenter()
drawHandle(turtle) - draws a handle on the door"""
    def __init__(self,center=(0,0),radius=1.0):
        self._center=center
        self._radius=radius
    def __str__(self):
        return('Center ='+str(self._center)+'\n'+'Radius ='+str(self._radius))
    def getRadius(self):
        return self._radius
    def getCenter(self):
        return self._center
    def drawHandle(self,brush):
        brush.goto(door.getLLeft()[0]+8,door.getURight()[1]/2)
        brush.down()
        brush.circle(self._radius)


def drawHouse(base,roof,door,handle,window1,window2):
    """Function used to draw the house.
Musted be passed with all of the objects of the house"""
    base.drawHouse(brush1)
    roof.drawRoof(brush1)
    door.drawDoor(brush1)
    handle.drawHandle(brush1)
    leftWindow.drawWindow(brush1)
    rightWindow.drawWindow(brush1)
    
def drawGrass(turtle):
    turtle.setheading(0)
    offset=(-475)
    turtle.up()
    turtle.goto(offset,0)
    turtle.begin_fill()
    turtle.down()
    turtle.fillcolor("green")
    turtle.pencolor("green")
    for i in range(100):
        turtle.left(75)
        turtle.forward(25)
        turtle.right(155)
        turtle.forward(25)
        turtle.setheading(0)
        turtle.up()
        offset=offset+12
        turtle.goto(offset,0)
        turtle.down()
    turtle.end_fill()
    turtle.up()

def drawSun(turtle):
    turtle.up()
    turtle.goto(-250,270)
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.goto(-250,310)

    turtle.pencolor("red")
    turtle.down()
    for i in range(50):
        turtle.up()
        turtle.forward(40)
        turtle.down()
        turtle.forward(20)
        turtle.up()
        turtle.backward(60)
        turtle.down()
        turtle.left(360/50)

def drawSky(turtle):
    turtle.up()
    turtle.goto(-475,0)

def drawFace(turtle):
    turtle.pencolor("blue")
    turtle.up()
    turtle.down()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(37)
    turtle.left(90)
    turtle.forward(20)
    turtle.setheading(270)
    turtle.down()
    turtle.pencolor("yellow")
    turtle.circle(20,180)
    turtle.up()
    turtle.setheading(180)
    turtle.forward(20)
    turtle.setheading(90)
    turtle.forward(17)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.down()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(90)
    turtle.forward(8.5)
    turtle.setheading(180)
    turtle.forward(29)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(0)

def drawCloud(x,y,turtle):
    turtle.pencolor("white")
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(90)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.down()
    for i in range (3):
        turtle.circle(30,180)
        turtle.setheading(90)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(180)
    turtle.forward(15)
    turtle.setheading(270)
    turtle.begin_fill()
    turtle.down()
    for i in range(3):
        turtle.circle(30,180)
        turtle.setheading(270)
    turtle.end_fill()
    turtle.up()
    turtle.pencolor("black")

def drawFlower(x,y,height,turtle):
    turtle.up()
    turtle.goto(x,y)
    turtle.pensize(5)
    turtle.pencolor("green")
    turtle.setheading(90)
    turtle.down()
    turtle.forward(height)
    turtle.up()
    turtle.pencolor("yellow")
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.fillcolor("yellow")
    turtle.down()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(90)
    turtle.forward(8)
    turtle.setheading(0)
    turtle.down()
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.circle(12)
    turtle.end_fill()
    turtle.up()
    turtle.showturtle()
    turtle.setheading(90)
    turtle.forward(12)
    turtle.setheading(0)
    turtle.pensize(2)
    for i in range(30):
        if i%2==0:
            turtle.pencolor("red")
        if i%2!=0:
            turtle.pencolor("orange")
        turtle.up()
        turtle.forward(20)
        turtle.down()
        turtle.forward(10)
        turtle.up()
        turtle.backward(30)
        turtle.down()
        turtle.left(360/30)


sky=Rectangle((-475,0),(475,475),"light blue")
sky.drawSky(brush1)

drawCloud(-270,270,brush1)
drawCloud(-90,350,brush1)
drawCloud(-20,230,brush1)
drawCloud(250,350,brush1)
drawCloud(370,220,brush1)
drawCloud(450,310,brush1)

roof=Triangle((0,HOUSEHEIGHT),(HOUSEBASE,HOUSEHEIGHT),((HOUSEBASE/2),HOUSEHEIGHT+(HOUSEHEIGHT/3)),"green")
base=Rectangle((0,0),(HOUSEBASE,HOUSEHEIGHT),"blue")
handle=Circle((20,20),(HOUSEBASE/66.67))


door=Rectangle(((HOUSEBASE/2)-(HOUSEBASE/10),0),((HOUSEBASE/2)+(HOUSEBASE/10),(HOUSEHEIGHT/3)),"yellow")
leftWindow=Rectangle(((HOUSEBASE/2)-(HOUSEBASE/2.86),(HOUSEHEIGHT/2)),((HOUSEBASE/2)-(HOUSEBASE/6.67),(HOUSEHEIGHT/2)+(HOUSEHEIGHT/3.75)),"light grey")
rightWindow=Rectangle(((HOUSEBASE/2)+(HOUSEBASE/2.86),(HOUSEHEIGHT/2)),((HOUSEBASE/2)+(HOUSEBASE/6.67),(HOUSEHEIGHT/2)+(HOUSEHEIGHT/3.75)),"light grey")


drawHouse(base,roof,door,handle,leftWindow,rightWindow)


drawGrass(brush1)
drawSun(brush1)
drawFlower(-170,10,55,brush1)
drawFlower(-300,10,40,brush1)
drawFlower(345,10,60,brush1)
brush1.up()
brush1.goto(-300,-100)
brush1.write("HAPPY BIRTHDAY!!!",font=('Arial',50))
faceX=-300
faceY=-190
brush1.up()
brush1.goto(faceX,faceY)
for i in range (6):
    brush1.down()
    drawFace(brush1)
    brush1.up()
    faceX=faceX+120
    brush1.goto(faceX,faceY)
    brush1.up()

faceX=-300
faceY=-190
faceY=faceY-120
brush1.goto(faceX,faceY)
for i in range (6):
    brush1.down()
    drawFace(brush1)
    brush1.up()
    faceX=faceX+120
    brush1.goto(faceX,faceY)
    brush1.up()
    
brush1.hideturtle()
input("Press enter to exit ;)")






