#this program takes one input and determines if it can be made into an integer.

def integerCheck(integer):
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

while True:
    test = input("enter an integer:")
    if integerCheck(test) == False:
        continue
    else:
        break
