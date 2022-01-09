import sys

def integerCheck(integer):                          #takes one input, converts it to an integer and makes sure it's not empty
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True


def euclideanAlgorithm(firstNumber, secondNumber):   #takes two inputs and finds the greatest common divisor
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

while True:
    while True:
        firstNumber = input("Please enter a number: ")
        if integerCheck(firstNumber) == False:
            continue
        elif int(firstNumber) == 0:
            print("the number must be greater than 0.")
            continue
        else:
            break
    while True:
        secondNumber = input("Please enter another number: ")
        if integerCheck(secondNumber) == False:
            continue
        elif int(firstNumber) == 0:
            print("the number must not be 0.")
            continue
        else:
            break
    while True:
        continuance = input("do you want to do another calculation? \n enter yes or no \n ")
        if continuance.lower() == "yes":
            break
        elif continuance.lower() == "no":
            print("\n thank you \n")
            sys.exit()
        else:
            print("your input was not valid")
print(euclideanAlgorithm(firstNumber, secondNumber), "is the GCD of ", firstNumber," and ", secondNumber)


sys.exit()