from cgitb import small
import sys

def canThisBeAnInteger(integer):                          #takes one input, converts it to an integer and makes sure it's not empty
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True


def euclideanAlgorithm(firstNumber, secondNumber):   #takes two inputs and returns the GCD.
    remainder = None
    largerNumber = max(int(firstNumber), int(secondNumber))
    smallerNumber = min(int(firstNumber), int(secondNumber))

    while remainder != 0:
        remainder = largerNumber % smallerNumber
        largerNumber = smallerNumber
        smallerNumber = remainder
    gcd = largerNumber

    return gcd


def euclideanAlgortihmSolvedForRi(remainderLarger, remainderSmaller, quotient):
    remainderIteration = remainderLarger - (remainderSmaller * quotient)
    return euclideanAlgortihmSolvedForRi(remainderIteration, remainderSmaller, )
    # return remainderIteration


def euclideanAlgorithmWithSubstitution():
    pass


while True:
    while True:
        firstNumber = input("Please enter a number: ").strip()
        if canThisBeAnInteger(firstNumber) == False:
            continue
        elif int(firstNumber) == 0:
            print("the number must not be 0.")
            continue
        else:
            break
    while True:
        secondNumber = input("Please enter another number: ").strip()
        if canThisBeAnInteger(secondNumber) == False:
            continue
        elif int(secondNumber) == 0:
            print("the number must not be 0.")
            continue
        else:
            break

    print(euclideanAlgorithm(firstNumber,secondNumber))
    i = 2
    remainderIteration = None
    remainderIterationsList = [(max(int(firstNumber), int(secondNumber)), (min(int(firstNumber), int(secondNumber))]
    quotientList = [remainderIterationsList[0] // remainderIterationsList[1]]
    remainderIteration = euclideanAlgortihmSolvedForRi(remainderIterationList[i], remainderIterationList[i], quotient[i] )
    while remainderIterationsList[-1] != 1:
        break

  #04/25 - left off figuring out where to set the iteration count since r0 and r1 are given.
  #I also need to figure out how to determine the relationship between the i count, the quotent and the remainder
  #I am conisdering whether or not ill be able to solve this problem recursively
    
    break


    # while True:
    #     continuance = input("do you want to do another calculation? \n enter yes or no \n ")
    #     if continuance.lower().strip() == "yes":
    #         break
    #     elif continuance.lower().strip() == "no":
    #         print("thank you")
    #         sys.exit()
    #     else:
    #         print("your input was not valid")



sys.exit()