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

def nextFactor(number):                                   #this function takes an integer and returns the next factor reducable 
        for x in range(number-1, 1, -1):
            if number % x == 0:
                return x

def countExponents(primeFactorsList):                     #counts exponents by taking a list of prime factors as an input and returns a dictionary with distinct prime factors as keys and their degree as values
    primeFactorsDict = {}

    for x in primeFactorsList:
        if x in primeFactorsDict:
            primeFactorsDict[x] += 1
        else:
            primeFactorsDict[x] = 1
    return primeFactorsDict

class factorTree:                                          #factorTree class is used to create branch objects that identify prime factors on the right and reducable factors on the left

    def __init__(self, left, right):
        self.left = left
        self.right = right


while True:
    n = int(input("Please enter a number: "))
    primeFactorsList = []


    while True:
        if nextFactor(n) is None:
            break
        branch = factorTree(nextFactor(n) , int(n / nextFactor(n)))

        if isThisPrime(branch.left) == True:
            primeFactorsList.append(int(branch.left))
            print("prime factor added from left ", branch.left)

        if isThisPrime(int(branch.right)) == True:
            primeFactorsList.append(int(branch.right))
            print("prime factor added from right ", branch.right)

        n = nextFactor(n)

    primeFactorsDict = countExponents(primeFactorsList)

    primeFactorsEvaluatedList = []

    for x in primeFactorsDict.keys():
        product = x ** primeFactorsDict.get(x) - x ** (primeFactorsDict.get(x) - 1)
        primeFactorsEvaluatedList.append(product)
    for i in range(len(primeFactorsEvaluatedList)):
        if i == 0:
            phi = primeFactorsEvaluatedList[i]
        else:
            phi = phi * primeFactorsEvaluatedList[i]
            
    print(phi)
 
    continuance()
