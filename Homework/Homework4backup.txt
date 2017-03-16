##########################################################################
#   Name: Mike Torchia
#   Assigment: Homework 4
#   Access ID: dz7995
#   PLEASE INCLUDE "TestFile1.txt" THAT WAS INCLUDED WITH THIS SUBMISSION
##########################################################################
import functools
import random

##########################################################################
#   Question 1  
##########################################################################



def mimic_dict(filename):
    mimicdict=dict()
    testFile=open(filename,"r")
    content=testFile.read()
    testFile.close() 
    _content=content.split()  #split the content of the file into a list with each element containing a word from the file
    nextWord=''
    for word in _content:
        mimicdict[nextWord] = mimicdict.get(nextWord, []) + [word] #use empty bracket for default value 
        nextWord=word                                              #because its consistent with list type
        #print (word)
    return mimicdict

####Have to set next word to empty because if not the first element in the dictionary will contain itself and
####thats not something we want. So what that line of code does is if mimicdict[nextWord] is not found then return
####and empty value ([]). If it is found though, add whatever "word" is as a value to the current key. Using
####"nextWord=word" at the end of the for loop keeps a the program pointing to two elements in "_content". nextWord
####being the current key that the program is on and "word" being the value to be added to the key.


def print_mimic(mimic_dict, word):
    if word not in mimic_dict:    #used to check if the word is even in the dictionary
        print ("The word you entered is not in the dictionary")
        return
    print("The key you entered is:",word)
    print("And its values are:")
    if(len(mimic_dict[word])>=5): #validation used to check if the values are bigger than 5 because we only want to output the first 5 values
        for i in range (5):
            print(mimic_dict[word][i])
    else:                         #still use a for loop to print values if the key has fewer than 5 values. just set the range to the number of values for each key
        for i in range (len(mimic_dict[word])):
            print(mimic_dict[word][i])
    return



myDict=mimic_dict("TestFile1.txt")
word=input("Eneter a single word to look up in the dictionary:")
print_mimic(myDict,word)


##########################################################################
#   Question 2
##########################################################################


##this just appends random numbers to the numbs list and then
##we use the reduce function and pass the min function along with
##the numbs list. this will find the min value of the first two elements
##then check that against the next element and find the mins and continue
##with this process until there is only one value left

numbs=[]
for i in range (10):
        numbs.append(random.randint(1,100))

print (numbs)
print(functools.reduce(min,numbs))


##because we are using sets we can use the "&" operator to check to see if
##there are intersections between each operand. currently in the solution below
##there is no intersection so when you run it the output is just "set()" (empty set)
##but if you were to add a 10 to "numbs3" then the output would be 10 because 10
##intersects with all 3 sets

numbs1=set([1,2,3,4,5,6,7,8,9,10])
numbs2=set([5,10,15,20])
numbs3=set([3,6,9,20])
numbs0=numbs1&numbs2&numbs3
print(numbs0)
