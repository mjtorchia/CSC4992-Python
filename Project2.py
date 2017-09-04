##########################################################################
#   Name: Mike Torchia
#   Assigment: Project part 2
#   Access ID: dz7995   
##########################################################################
from turtle import Turtle
brush1=Turtle()
HOUSEBASE=300
HOUSEHEIGHT=250
startPoint=(-100,-100)
print("THIS PROGRAM IS USED TO DRAW A SMIPLE HOUSE UISNG")
print("3 BASIC SHAPES. TRIANGLE, CRICLE, AND RECTANGLE")
print("Note: Base=200,Height=150 produces best results")
print()
      
HOUSEBASE=int(input("Enter size of house base: (Greather than 100)"))#200
while HOUSEBASE <100:
    HOUSEBASE=int(input("Invalid. Please try again: "))
HOUSEHEIGHT=int(input("Enter size of house height: (Greater than 100)"))#150
while HOUSEHEIGHT <100:
    HOUSEHEIGHT=int(input("Invalid. Please try again: "))

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
    


#Object Creation
    #Based on values user enters for HOUSEBASE and HOUSEHEIGHT
roof=Triangle((0,HOUSEHEIGHT),(HOUSEBASE,HOUSEHEIGHT),((HOUSEBASE/2),HOUSEHEIGHT+(HOUSEHEIGHT/3)),"red")
base=Rectangle((0,0),(HOUSEBASE,HOUSEHEIGHT),"blue")
handle=Circle((20,20),(HOUSEBASE/66.67))

#Divided HOUSEBASE and/or HOUSEHEIGHT to allow for proper scaling based on user input
door=Rectangle(((HOUSEBASE/2)-(HOUSEBASE/10),0),((HOUSEBASE/2)+(HOUSEBASE/10),(HOUSEHEIGHT/3)),"green")
leftWindow=Rectangle(((HOUSEBASE/2)-(HOUSEBASE/2.86),(HOUSEHEIGHT/2)),((HOUSEBASE/2)-(HOUSEBASE/6.67),(HOUSEHEIGHT/2)+(HOUSEHEIGHT/3.75)),"light grey")
rightWindow=Rectangle(((HOUSEBASE/2)+(HOUSEBASE/2.86),(HOUSEHEIGHT/2)),((HOUSEBASE/2)+(HOUSEBASE/6.67),(HOUSEHEIGHT/2)+(HOUSEHEIGHT/3.75)),"light grey")

#Calling the drawHouse function passing our objects
drawHouse(base,roof,door,handle,leftWindow,rightWindow)


#Printing docstrings for each class
print("Printing docstrings for each object...")
print()
print("Triangle:")
print(roof.__doc__)
print()
print("Rectangle:")
print(base.__doc__)
print()
print("Circle:")
print(handle.__doc__)
print()


#Testing the __str__ function for each object
print('Information for roof object:'+'\n'+str(roof))
print()
print('Information for base object:'+'\n'+str(base))
print()
print('Information for handle object:'+'\n'+str(handle))
print()
print('Information for door object:'+'\n'+str(door))
print()
print('Information for leftWindow object:'+'\n'+str(leftWindow))
print()
print('Information for rightWindow object:'+'\n'+str(rightWindow))
input("Press enter to exit)")

