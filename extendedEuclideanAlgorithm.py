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


def euclideanAlgorithm(remainderIterationsList):   #takes two inputs and returns the GCD.
    remainder = None
    largerNumber = remainderIterationsList[0]
    smallerNumber = remainderIterationsList[1]

    while remainder != 0:
        remainder = largerNumber % smallerNumber
        remainderIterationsList.append(remainder)
        largerNumber = smallerNumber
        smallerNumber = remainder
    
    return remainderIterationsList[0:-1]            #slicing removes the zero remainder. I am still looking for the least messy way to write a condition that both initializes the loop condition and terminates the loop without adding 0 to the remainder interations list


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

   
    remainderIterationsList = [None, None,]
    remainderIterationsList[0] = max(int(firstNumber), int(secondNumber))
    remainderIterationsList[1] = min(int(firstNumber), int(secondNumber))
    
    print(euclideanAlgorithm(remainderIterationsList))
    
    remainderIterationsList = euclideanAlgorithm(remainderIterationsList)
    quotientList = []
    
    for x in range(0, len(remainderIterationsList)-1):
        print(x, " is x", remainderIterationsList[x], " is x index", remainderIterationsList[x + 1], " is x +1")
        quotientList.append(remainderIterationsList[x] // remainderIterationsList[x + 1])
        print(quotientList)
        x += 1
    #5/4 - I left off trying to figfure out how to terminate the loop which creates the list of quotients values without getting a zero division error. Probably should have just started with making this a function.
    
    print(quotientList)
    
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