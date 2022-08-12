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
        
        return remainderIterationsList          

    remainderIterationsList = euclideanAlgorithm(firstNumber, secondNumber)

    def generateQuotientList(remainderIterationsList):
        quotientList = []
        for x in range(0, len(remainderIterationsList)-2):  #the iteration count excludes the final quotient.  
            try:
                quotientList.append(remainderIterationsList[x] // remainderIterationsList[x+1])
                # print(remainderIterationsList[x], "is the remainder at index position, ", x)
                # print(remainderIterationsList[x+1], "is the remainder at index position, ", x+1)
                # print(remainderIterationsList[x] // remainderIterationsList[x+1], " is what is getting appended to the quotient list as a result of the above values")
            except ZeroDivisionError:
                print("ZeroDivisionError detected")
                return quotientList
            x += 1
        return quotientList

    quotientList = generateQuotientList(remainderIterationsList)

    print(remainderIterationsList, " is remainderIterationsList")
    print(quotientList, " is quotientList")

    class EuclideanAlrgorithmWithSubstitution: 
        def __init__(self, remainderIteration, remainderMinusTwo, quotientIteration, remainderMinusOne):
            self.remainderIteration = remainderIteration
            self.remainderMinusTwo = remainderMinusTwo 
            self.quotientIteration = quotientIteration
            self.remainderMinusOne = remainderMinusOne
        
        equationlist = []

        def pushIterationToEquationList(self, equationList):
            currentIterationList = []
            currentIterationList.extend(self.remainderIteration, self.remainderMinusTwo, self.quotientIteration, self.remainderMinusOne)
            equationList.append(currentIterationList)
            print(currentIterationList, " is currentIterationList")
            print(equationList, "is equation List")


        def printEuclideanAlrgorithmWithSubstitution(self):
            #try to think of a way to concatinate these object properties to print the exact equation
            print(self.remainderIteration, " is remainderIteration") 
            print(self.remainderMinusTwo, " is remainderMinusTwo")
            print(self.quotientIteration, " is quotientIteration")
            print(self.remainderMinusOne, " is remainderMinusOne")
            print(self.remainderIteration, " = ", self.remainderMinusTwo, " + (", self.quotientIteration," * ", self.remainderMinusOne,")")
        
        def solveEquation(self):
            return self.remainderIteration == self.remainderMinusTwo - (self.quotientIteration * self.remainderMinusOne)

        def interationsOfSolvedForRiList(self):
            pass
    for x in range(2, len(remainderIterationsList)-1):
        currentIteration = EuclideanAlrgorithmWithSubstitution(remainderIterationsList[x], remainderIterationsList[x-2], quotientList[x-2], remainderIterationsList[x-1])
        currentIteration.printEuclideanAlrgorithmWithSubstitution()
        print(currentIteration.solveEquation())

    class ExtendedEuclideanAlgorithmEquation:
        def __init__(self, s, t):
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
