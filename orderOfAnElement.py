import sys

def integerCheck(integer):                          #takes an input and returns false if its empty or cannot be converted to an integer
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

def continuance():                                  #creates a loop which prompts the user to continue or exit
    while True:
        continuance = input("do you want to do another calculation? \n enter yes or no \n ")
        if continuance.lower().strip == "yes":
            break
        elif continuance.lower().strip == "no":
            print("\n thank you \n")
            sys.exit()
        else:
            print("your input was not valid")

def euclideanAlgorithm(firstNumber, secondNumber):   #takes two inputs and returns the GCD
    remainder = None
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)

    if firstNumber > secondNumber:
        smallerNumber = secondNumber
        largerNumber = firstNumber
    else:
        smallerNumber = firstNumber
        largerNumber = secondNumber

    while remainder != 0:
        remainder = largerNumber % smallerNumber
        largerNumber = smallerNumber
        smallerNumber = remainder

    return largerNumber

def modularReduction(modulus, a):                   #takes two inputs and returns the remainder of the modular arithemtic operation between them
    a = int(a)
    modulus = int(modulus)
    r = a % modulus

    return r





group = input("enter a group: ")
element = input("enter an element of that group: ")

cyclicGroup = []
for eachElement in range (1, int(group)):
    if euclideanAlgorithm(int(eachElement), group) == 1:
        cyclicGroup.append(eachElement)
if element not in cyclicGroup:
    print("Sorry. The element ", element, " is not in the finite group ", group)
    print(cyclicGroup, "are the elements in the finite group ", group)

