import sys

def integerCheck(integer):                          #takes an input and returns false if its empty or cannot be converted to an integer
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

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

while True:
    while True:
        group = input("enter a group: ")
        if integerCheck(group) == False:
            continue
        elif int(group) == 0:
            print("the group must not be 0.")
            continue
        else:
            break
    cyclicGroup = []
    for eachElement in range (1, int(group)):
        if euclideanAlgorithm(int(eachElement), group) == 1:
            cyclicGroup.append(int(eachElement))
    while True:
        element = input("enter an element of that group: ")
        if integerCheck(element) == False:
            continue
        element = int(element)
        if element not in cyclicGroup:
            print("Sorry. The element ", element, " is not in the finite group ", group)
            print(cyclicGroup, "are the elements in the finite group ", group)
            continue
        else:
            break
    remainder = None
    exponent = 0
    while remainder != 1:
        exponent += 1
        remainder = modularReduction(group, int(element) ** exponent)
    print("the order of ", element, " in the group ", group," is ", exponent)

    continuance()



sys.exit()