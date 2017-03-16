########################################################################
#   Name: Mike Torchia
#   Assigment: Homework 3
#   Access ID: dz7995
########################################################################

########################################################################
#   Question 1
########################################################################

#Function Definition
####################################
def problem1(list=[]):
    tempInt=0
    tempLoc=0
    for x in range (len(list)):
        if list[x]>tempInt:
            tempInt=list[x]
            tempLoc=x
    print(tempInt,end=" ")
    list[tempLoc]=0
####################################         




################
#MAIN
################        
probList=[]                         #declare list  
for x in range (10):                #Enter integers one by one and append the list
    tempInt=int(input("Enter 1 (one) Integer: "))
    probList.append(tempInt)
    
for x in range (len(probList)):     #preform the function on the list
    problem1(probList)
print("\n")






    
  
########################################################################
#   Question 2
########################################################################

#define vowles list
VOWELS=["A","a","E","e","I","i","O","o","U","u",]

#get sentence from user
def getSentence():
    inputString=input("Enter a sentence: ")
    inputList=inputString.split(" ")
    return inputList



def englishToPig(list=[]):
    #iterate by size of list
    for x in range(len(list)):
        vowel=False                         #set the vowel flag to false
        tempString=list[x]                  #tempString is a test vaule and it equal to the next value in the list
        for i in range(len(VOWELS)):        #iterate by size of VOWELS list to check for vowels
            if tempString[0]==VOWELS[i]:    #if the first letter is a vowel, set the vowel flag
                vowel=True
        if vowel==True:                     #translate like this if the first letter is a vowel then reset the flag       
            printString=tempString+("hay")
            print(printString)  
        if vowel==False:                    #translate like this if the first letter is not a vowel
            firstLetter=tempString[:1]
            slicedString=tempString[1:]
            printString=(slicedString+firstLetter)+"ay"
            print(printString)
                    



################
#MAIN
################
inputList=getSentence()
englishToPig(inputList)

        
    




