import sys

def integerCheck(integer):                          #takes an input and returns false if its empty or cannot be converted to an integer
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

def isPrime(number):
    for x in range(2, int(number/2) +1):
        if number % x == 0:
            return False
    return True

def nextFactor(number):
        for x in range(number-1, 1, -1):
            if number % x == 0:
                return x

class Node:

    def __init__(self, left, right):
        self.left = left
        self.right = right


while True:
    n = int(input("Please enter a number: "))
    primeFactors = []

    while True:
        if nextFactor(n) is None:
            break
        branch = Node(nextFactor(n) , n / nextFactor(n))
        if isPrime(branch.left) == True:
            primeFactors.append(branch.left)
        if isPrime(int(branch.right)) == True:
            primeFactors.append(int(branch.right))
        n = nextFactor(n)

    print(primeFactors)

    continuance()


