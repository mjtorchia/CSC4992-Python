########################################################################
#   Name: Mike Torchia
#   Assigment: Homework 2
#   Access ID: dz7995
########################################################################
import math
import collections


########################################################################
#   Question 1
########################################################################
print("Question 1")

#Regular alphabet and the alphabet shifted 3 characters to the right
alphabet = ["a","b","c","d","e","f","g","h",
            "i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]

shiftAlphabet = ["d","e","f","g","h","i","j","k",
                  "l","m","n","o","p","q","r","s",
                  "t","u","v","w","x","y","z","a","b","c",]


#Regular digits and digits shifted 4 digits to the right
#Represented them as strings because it made the encryption easier to handle
digit = ["0","1","2","3","4","5","6","7","8","9"]
shiftDigit = ["4","5","6","7","8","9","0","1","2","3"]



inputString=(input("Enter a string: "))
outputString=""
tempChar=""
#loop through the inputString
for x in range(len(inputString)):
    #use this tempChar to test in the if loop below
    tempChar=inputString[x]
    #loop through the alphabet
    for i in range(len(alphabet)):
        #when the tempChar and alphabet are equal
        #appened the outputString with the shiftAlphabet[i]
        #because alphabet[] and shift alphabet are the same
        #just shifted by 3 characters
        if tempChar==alphabet[i]:
            outputString=outputString+shiftAlphabet[i]

print(outputString)


#The same logic is applied here as above

tempDigit=""
outputDigit=""

inputDigit=str((input("Enter a distance: ")))
for x in range(len(inputDigit)):
    tempDigit=inputDigit[x]
    for i in range(len(digit)):
        if tempDigit==digit[i]:
            outputDigit=outputDigit+shiftDigit[i]
print(outputDigit)


########################################################################
#   Question 2
########################################################################


#Open the file and write these 5 sentences. Two have ! and ? to test the methods below for
#counting number of sentences
testFile=open("TestFile.txt","w")
testFile.write("Hello World.\n")
testFile.write("The brown dog jumps over the fence.\n")
testFile.write("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.\n")
testFile.write("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo?\n")
testFile.write("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo!\n")
testFile.close()


testFile=open("TestFile.txt","r")
wordCount=0
for line in testFile:
    #every time the the line splits add 1 to wordCount, which happens
    #at every white space
    wordCount=wordCount+ len(line.split())
print("Number of words:",wordCount)

#Using the counter container, read the line and split them.
#Simillar to the method above the but the counter will keep track
#of how many times its seen each word
testFile=open("TestFile.txt","r")
freqCount=collections.Counter(testFile.read().split())
print(freqCount)


#Simply using the count method and passing in each type of
#punctuation. I can add the return value to sentenceCount and
#then print that number to count the sentences
testFile=open("TestFile.txt","r")
sentenceCount=testFile.read().count('.')
testFile=open("TestFile.txt","r")
sentenceCount+=testFile.read().count('!')
testFile=open("TestFile.txt","r")
sentenceCount+=testFile.read().count('?')
print("Number of Sentences: ",(sentenceCount))



testFile.close()
