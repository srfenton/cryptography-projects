from cgitb import small
import sys

while True:
    while True:
        try:
            firstNumber = int(input("Please enter a number: ").strip())
        except:
            print("the number must be a non-zero integer.")
            continue
        if int(firstNumber) == 0:
            print("the number must not be 0.")
            continue
        else:
            break
    while True:
        try:
            secondNumber = int(input("Please enter a number: ").strip())
        except:
            print("the number must be a non-zero integer.")
            continue
        if int(secondNumber) == 0:
            print("the number must not be 0.")
            continue
        else:
            break

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
        
        return remainderIterationsList          #the slicing removes the zero remainder since the 0 remainder doesn't suit our purposes and we may need to pop the list to completion when we get to the end of it. 
                                                #I am still looking for the least messy way to write a condition that both initializes the loop condition and terminates the loop without adding 0 to the remainder interations list
                                                #I removed the slicing [0:-1] because it returns an empty list for 8 and 8. 
                                                #better to have it working than contain extra information.

    remainderIterationsList = euclideanAlgorithm(firstNumber, secondNumber)

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

    quotientList = generateQuotientList(remainderIterationsList)

    print(remainderIterationsList, " is remainderIterationsList")
    print(quotientList, " is quotientList")

    class EuclideanAlrgorithmWithSubstitution: 
        def __init__(self, remainderIteration, remainderPrevious, quotientIteration, remainderCurrent):
            self.remainderIteration = remainderIteration
            self.remainderPrevious = remainderPrevious 
            self.quotientIteration = quotientIteration
            self.remainderCurrent = remainderCurrent

        def EuclideanAlrgorithmWithSubstitution(self):
            return self.remainderPrevious - (self.quotientIteration * self.remainderCurrent)

        def printEuclideanAlrgorithmWithSubstitution(self):
            pass
            #try to think of a way to concatinate these object properties to print the exact equation
            print(self.remainderIteration, " is remainderIteration /n ") 
            print(self.remainderPrevious, " is remainderPrevious/n ")
            print(self.quotientIteration, " is quotientIteration/n ")
            print(self. remainderCurrent, " is reaminderCurrent/n ")
        
        def interationsOfSolvedForRiList(self):
            pass
  
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