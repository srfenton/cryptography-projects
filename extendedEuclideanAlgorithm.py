from cgitb import small
import sys

class EuclideanAlgorithmSolvedForRi:
    def __init__(self, remainderIteration, remainderPrevious, quotientIteration, remainderCurrent):
        remainderIteration = self.remainderIteration
        remainderPrevious = self.remainderPrevious
        quotientIteration = self.quotientIteration 

    def solveEuclideanAlgorithmSolvedForR(self):
        return self.remainderPrevious - (self.quotientIteration * self.remainderCurrent)


class EuclideanAlrgorithmWithSubstitution:
    def __init__(self, EuclideanAlgorithmSolvedForRi):
        pass

    #05.16: I am leaving off here in defining classes which will make it easier to solve the EEA problem.
    #next I need to define the withsub objects / methods and see and then try to remember how to actually do the substitution part
    #Ideally, I would like to be able to plugin the iteration value to any of these objects or methods and be able to reason about different coefficients in the current iteration as a whole. 
    #Meaning, using OOP should make the subtitution part easy
    #I did not use OOP to generate my remainder and quotient lists 
    #because they do not need to be re-created at any point. 
    #The numbers we start with determine those lists and they do not need to change


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
    for x in range(0, len(remainderIterationsList)-2):  #the iteration count is one less than usual to leave off the quotient between the 2nd to last remainder and the 1 value.
        try:
            quotientList.append(remainderIterationsList[x] // remainderIterationsList[x+1])
            print(remainderIterationsList[x], "is the remainder at index position, ", x)
            print(remainderIterationsList[x+1], "is the remainder at index position, ", x+1)
            print(remainderIterationsList[x] // remainderIterationsList[x+1], " is what is getting appended to the quotient list as a result of the above values")
        except ZeroDivisionError:
            print("ZeroDivisionError detected")
            return quotientList

        x += 1

    return quotientList


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