########################################################################
#   Name: Mike Torchia
#   Assigment: Homework 1
#   Access ID: dz7995
########################################################################
import hashlib
import math

_KEY=(hash("mypassword")%541)

########################################################################
#   Question 1
########################################################################
print('Question 1')
#variables
taxRate=0.06 #6% tax rate
standDeduc=100.0 #100 standard deduction
deducPer=50.0 #50 per dependent
taxableIncome=0.0 #calculated later
incomeTax=0.0 #calculated later

#inputs
grossInc = float(input('Enter your gross income: '))
if grossInc < 0:
    print('Error: Gross income cannot be less than 0')

numOfDepend=float(input('Enter number of dependents: '))
if numOfDepend < 0:
    print('Error: Number of dependents cannot be less than 0') 


#calculations
taxableIncome = grossInc - standDeduc - (deducPer * numOfDepend)
incomeTax= taxableIncome * taxRate


#outputs
print('The Income Tax is: ', incomeTax)

print()


########################################################################
#   Question 2
########################################################################
print('Question 2')
firstNum=float(input('Enter left operand: '))
secondNum=float(input('Enter right operand: '))
print(firstNum, ' times ' , secondNum, ' equals ' , firstNum*secondNum)
print('The smallest of the two numbers is: ', min(firstNum,secondNum))
print('The largest of the two numbers is: ', max(firstNum,secondNum))
               
print()

########################################################################
#   Question 3
########################################################################
print('Question 3')
numOfTries=0
print('You have 3 tries to guess the password. Good Luck')
while(numOfTries<3):
    userPassword=input('Enter the password: ')
    userHash=(hash(userPassword)%541)
    if userHash==_KEY: #check if the user password matches the key
        print('You guessed the right password')
        numOfTries=3 #breaks the while loop
    else:
        if numOfTries>=2: #this is so after the last try it says game over instead of try again
            print('Sorry. Game Over')
            numOfTries+=1
        else:
            print('Sorry. Try Again')
            numOfTries+=1

print()


########################################################################
#   Question 4
########################################################################
print('Question 4')

sqrNum=float(input('Enter a number: '))
print('Using import math the square root of that number is: ',math.sqrt(sqrNum))

#guess=float(input('Using Newtons Method, enter a guess for the square root of your number: '))
###########################################
#Newtons method
#(1/2)*(guess)+(number being rooted)/(guess)
###########################################

x=float(input("Enter a number: "))
tolerance=0.00001
guess=x/2
while not (abs(guess*guess-x)< tolerance):
    guess=(guess+(x/guess))/2.0
print('Using Newtons method the square root of that number is: ',(guess))



#newton=(1/2)*((guess)+(sqrNum/guess))
#print('The estimation using Newtons Method is: ',newton)
#print('Square root of number using python: ',math.sqrt(sqrNum))

