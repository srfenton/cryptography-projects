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


def isPrime(number):
    for x in range(2, int(number/2) +1):
        if number % x == 0:
            return False
    return True

while True:
    prime = int(input("please input a prime number: "))
    print(isPrime(prime))
    continuance()

