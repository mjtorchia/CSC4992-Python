##########################################################################
#   Name: Mike Torchia
#   Assigment: Homework 5
#   Access ID: dz7995
#   For best results individually run each part of Question 2
#   Comment out wherever part you are not running
##########################################################################
from turtle import Turtle
##########################################################################
#   Question 1  
##########################################################################


class RationalNumber:
    def __init__(self,n1,d1,n2,d2):     #constuctor
        self.n1=n1
        self.n2=n2
        self.d1=d1
        self.d2=d2

        #operations#
    def add(self):
        print((self.n1*self.d2 + self.n2*self.d1)/(self.d1*self.d2))
    def subtract(self):
        print((self.n1*self.d2 - self.n2*self.d1)/(self.d1 * self.d2))
    def multiply(self):
        print((self.n1*self.n2)/(self.d1*self.d2))
    def divide(self):
        print((self.n1*self.d2)/(self.d1*self.n2))
    def equalTo(self):
        if((self.n1*self.d2)==(self.n2*self.d1)):
            print("The two rational numbers are equal")
        else:
            print("The two rational numbers are not equal")

            #modifiers and accessors#
    def setN1(self,int):
        self.n1=int
    def setN2(self,int):
        self.n2=int
    def setD1(self,int):
        self.d1=int
    def setD2(self,int):
        self.d2=int
    def getN1(self):
        return self.n1
    def getN2(self):
        return self.n2
    def getD1(self):
        return self.d1
    def getD2(self):
        return self.d2


#Get inputs from user then run each operation on the inputs#
n1=float(input("Enter the numerator for the first number:"))
d1=float(input("Enter the denominator for the first number:"))
n2=float(input("Enter the numerator for the second number:"))
d2=float(input("Enter the denominator for the second number:"))
myTest=RationalNumber(n1,d1,n2,d2)
##print(myTest.getN1())
##print(myTest.getN2())
##print(myTest.getD1())
##print(myTest.getD2())


myTest.add()
myTest.subtract()
myTest.multiply()
myTest.divide()
myTest.equalTo()


##########################################################################
#   Question 2a  
##########################################################################


penta=Turtle()
penta.goto(0,0)
penta.down()
for i in range(5):  #number of sides
    penta.forward(300)
##    The angle of each point is 36 degrees so if we look at the first line draw
##    its at 180 degrees and we want the angle between that line and the next one drawn
##    to be 36 so if we drawn that on a peice of paper we can see the pointer needs to turn
##    x amount of degrees to get to that point (penta.left). so just by looking at the visual aid
##    drawn we can see that the value we need would be the amount that needs to be added to 36 to give us
##    180 degrees, which is 144. 36+x=180 : x=144
    penta.left(144)
penta.up()
penta.hideturtle


########################################################################
#   Question 2b
########################################################################

sprite=Turtle()
sprite.goto(0,0)
legs=int(input("Enter number of legs you want on your sprite:"))
for i in range(legs):
##    put the pen down then move it 200 units. then use the backwards fucntion passing the same length
##    (200) to put the pen back to the origin. next put the pen down and rotate it 360/legs degrees
##    and repeat that process until the for loop is complete
    sprite.down()
    sprite.forward(200)
    sprite.up()
    sprite.backward(200)
    sprite.down()
    sprite.left(360/legs)
sprite.hideturtle()
 















































