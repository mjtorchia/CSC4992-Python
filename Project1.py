##########################################################################
#   Name: Mike Torchia
#   Assigment: Project part 1
#   Access ID: dz7995   
##########################################################################
#parent class
class Employee(object):

    #initilize attributes
    def __init__(self,name="N/A",number=0):
        self._name=name
        self._number=number

    #write methodd for str() function
    def __str__(self):
        return 'Employee Name: '+self._name+'\n'+\
               'Employee Number: '+str(self._number)+'\n'

    #accessors and mutators
    def getName(self):
        return self._name
    def setName(self,name):
        self._name=name
    def getNumber(self):
        return self._number
    def setNumber(self,number):
        self._number=number
        
class ProductionWorker(Employee):
    #initilize attributes, while also passing values to init parent class
    def __init__(self,_name="",_num=0,shiftnum=0,wage=0,):
        super().__init__(_name,_num)
        self._shiftnum=shiftnum
        self._wage=wage

    #write methodd for str() function
    def __str__(self):
        return 'Employee Name: '+self._name+'\n'+\
               'Employee Number: '+str(self._number)+'\n'+\
               'Shift Number: '+str(self._shiftnum)+'\n'+\
               'Wage: '+str(self._wage)+'\n'

    #accessors and mutators
    def getShiftnum(self):
        return self._shiftnum
    def setShiftnum(self,shiftnum):
##        temp=input("Enter shift number. 1 for day shift. 2 for night shift")
##        while(temp <1 or temp>2):
##            temp=input("Invalid shift number. Please try again")
        self._shiftnum=shiftnum
    def getWage(self):
        return self._wage
    def setWage(self,wage):
        self._wage=wage

class ShiftSupervisor(Employee):
    #initilize attributes, while also passing values to init parent class
    def __init__(self,_name=0,_num=0,salary=0,bonus=0):
        super().__init__(_name,_num)
        self._salary=salary
        self._bonus=bonus

    #write methodd for str() function
    def __str__(self):
        return 'Employee Name: '+self._name+'\n'+\
               'Employee Number: '+str(self._number)+'\n'+\
               'Salary: '+str(self._salary)+'\n'+\
               'Bonus: '+str(self._bonus)+'\n'

    #accessors and mutators
    def getSalary(self):
        return self._salary
    def setSalary(self,salary):
        self._salary=salary
    def getBonus(self):
        return self._bonus
    def setBonus(self,bonus):
        self._bonus=bonus

def main():

    ##Promt the user for inputs for each object. While also providing verification loops
    ##to make sure inputs are correct for their respective object attributes
    tempName=input("Enter name for production worker: ")

    tempNum=int(input("Enter ID number for production worker: "))
    while type(tempNum) != int:
        tempNum=int(input("Invalid ID number. Please try again: "))

    tempShift=int(input("Please enter shift number: (1 for day. 2 for night)"))
    while type(tempShift) !=int:
        tempShift=int(input("Invalid shift number. Please try again: "))
    while (tempShift <1 or tempShift>2):
        tempShift=int(input("Invalid shift number. Please try again: "))

    tempWage=float(input("Enter production worker wage: "))
    while type(tempWage) !=float:
        tempWage=float(input("Invalid wage. Please try again: "))

    ##Create object with data from user
    proletariat=ProductionWorker(tempName,tempNum,tempShift,tempWage)

    ##Print object's attributes using accessors
    print('Employee Name: '+proletariat.getName()+'\n'+\
               'Employee Number: '+str(proletariat.getNumber())+'\n'+\
               'Shift Number: '+str(proletariat.getShiftnum())+'\n'+\
               'Wage: '+str(proletariat.getWage())+'\n')

   #Can also use the str function to print in the same way
   # print(str(proletariat))
    
    ##Promt the user for inputs for each object. While also providing verification loops
    ##to make sure inputs are correct for their respective object attributes
    tempName=input("Enter name for shift supervisor: ")

    tempNum=int(input("Enter ID number for shift supervisor: "))
    while type(tempNum) != int:
        tempNum=int(input("Invalid ID number. Please try again: "))

    tempSalary=float(input("Enter salary for shift supervisor: "))
    while type(tempSalary)!=float:
        tempSalary=float(input("Invalid salary. Please try again:"))

    tempBonus=float(input("Enter bonus for shift supervisor: "))
    while type(tempBonus)!=float:
        tempBonus=float(input("Invalid bonus. Please try again: "))

    ##Create object with data from user
    bourgeoisie=ShiftSupervisor(tempName,tempNum,tempSalary,tempBonus)

    ##Print object's attributes using accessors
    print('Employee Name: '+bourgeoisie.getName()+'\n'+\
               'Employee Number: '+str(bourgeoisie.getNumber())+'\n'+\
               'Salary: '+str(bourgeoisie.getSalary())+'\n'+\
               'Bonus: '+str(bourgeoisie.getBonus())+'\n')

    #Can also use the str function to print in the same way
    #print(str(bourgeoisie))
    input("Press enter to exit ;)")

#Run program
main()  
        
