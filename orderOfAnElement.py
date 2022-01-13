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

group = input("enter a group: ")
element = input("enter an element of that group: ")


cyclicGroup = []
for eachElement in range (1, int(group)):
    if euclideanAlgorithm(int(eachElement), group) == 1:
        cyclicGroup.append(eachElement)
if element not in cyclicGroup:
    print("Sorry. The element ", element, " is not in the finite group ", group)
    print(cyclicGroup, "are the elements in the finite group ", group)
