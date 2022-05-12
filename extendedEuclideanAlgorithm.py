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


def euclideanAlgorithm(firstNumber, secondNumber):   #takes two integer inputs and returns a list of the remainders with the GCD as the final element.
    remainder = None
    remainderIterationsList = []
    largerNumber = max(int(firstNumber), int(secondNumber))
    smallerNumber = min(int(firstNumber), int(secondNumber))
    remainderIterationsList.append(largerNumber)
    remainderIterationsList.append(smallerNumber)

    while remainder != 0:
        remainder = largerNumber % smallerNumber
        remainderIterationsList.append(remainder)
        largerNumber = smallerNumber
        smallerNumber = remainder
    
    return remainderIterationsList[0:-1]            #the slicing removes the zero remainder since the 0 remainder doesn't suit our purposes and we may need to pop the list to completion when we get to the end of it. I am still looking for the least messy way to write a condition that both initializes the loop condition and terminates the loop without adding 0 to the remainder interations list


def generateQuotientList(remainderIterationsList):
    quotientList = []
    for x in range(0, len(remainderIterationsList)-1):
        try:
            quotientList.append(remainderIterationsList[x] // remainderIterationsList[x+1])

        except ZeroDivisionError:
            print("ZeroDivisionError detected")
            return quotientList

        x += 1

    return quotientList


def euclideanAlgortihmSolvedForRi(remainderLarger, remainderSmaller, quotient):
    pass


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

    remainderIterationsList = euclideanAlgorithm(firstNumber, secondNumber)
    quotientList = generateQuotientList(remainderIterationsList)
    print(remainderIterationsList, " is remainderIterationsList")
    print(quotientList, " is quotientList")

    
    
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