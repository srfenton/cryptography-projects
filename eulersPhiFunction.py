import sys
from turtle import left

def canThisBeAnInteger(integer):                          #takes an input and returns false if its empty or cannot be converted to an integer
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

def continuance():
    while True:
            continuance = input("do you want to do another calculation? \n enter yes or no \n ")
            if continuance.lower().strip() == "yes":
                break
            elif continuance.lower().strip() == "no":
                print("\n thank you \n")
                sys.exit()
            else:
                print("your input was not valid")

def isThisPrime(number):
    for x in range(2, int(number/2) +1):
        if number % x == 0:
            return False
    return True

def nextFactor(number):
        for x in range(number-1, 1, -1):
            if number % x == 0:
                return x

def countExponents(primeFactors):
    primeFactorsDict = {}

    for x in primeFactors:
        if x in primeFactorsDict:
            primeFactorsDict[x] += 1
        else:
            primeFactorsDict[x] = 1
   
    return primeFactorsDict

class Node:

    def __init__(self, left, right):
        self.left = left
        self.right = right


while True:
    n = int(input("Please enter a number: "))
    primeFactorsList = []


    while True:
        if nextFactor(n) is None:
            break
        branch = Node(nextFactor(n) , n / nextFactor(n))

        if isThisPrime(branch.left) == True:
            primeFactorsList.append(branch.left)

        if isThisPrime(int(branch.right)) == True:
            primeFactorsList.append(int(branch.right))

        n = nextFactor(n)

    print(primeFactorsList)
    primeFactorsDict = countExponents(primeFactorsList)
    print(countExponents(primeFactorsList))

    primeFactorsEvaluatedList = []

    for x in primeFactorsDict.keys():
        product = x ** primeFactorsDict.get(x) - x ** (primeFactorsDict.get(x) - 1)
        primeFactorsEvaluatedList.append(product)
        print(primeFactorsEvaluatedList)
        
    #fill in with product of list

    
 
    continuance()
