def integerCheck(integer):              #takes one input, converts it to an integer and makes sure it's not empty
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

def modularReduction(m, a):             #takes two inputs, a modulus and a value to reduce (a)
    a = int(a)
    m = int(m)
    q = a // m
    r = a - q * m

    return r

def euclideanAlgorithm(firstNumber, secondNumber)   #takes two inputs and finds the greatest common divisor
    #ri = ri-2 - (qi · ri-1)
    quotient = 0                        #initialzing this variable
    if firstNumber > secondNumber:
        smallerNumber = secondNumber
        largerNumber = firstNumber
    else:
        smallerNumber = firstNumber
        largerNumber = secondNumber

        quotient = smallerNumber // largerNumber
        remainder = modularReduction(largerNumber, smallerNumber)



while True:
    print("Please enter a number: ")
    m = input()
    if integerCheck(firstNumber) == False:
        continue
    elif int(m) == 0:
        print("the modulus must be greater than 0.")
        continue
    else:
        break

while True:
    print("Please enter another number: ")
    a = input()
    if integerCheck(secondNumber) == False:
        continue
    else:
        break


sys.exit()