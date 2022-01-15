import sys

def integerCheck(integer):              #checks for a value error to make sure the input is neither empty or a string
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

def modularReduction(modulus, a):
    a = int(a)
    modulus = int(modulus)
    r = a % modulus

    return r

while True:
    while True:                     #this loop takes an input for the modulus and makes sure it is valid
        modulus = input("Please enter a modulus: ").strip()
        if integerCheck(modulus) == False:
            continue
        elif int(modulus) <= 0:
            print("the modulus must be greater than 0.")
            continue
        else:
            break

    while True:                     #this loop takes an input for the a value or number to reduce and makes sure it is valid
        a = input("Please enter a number to reduce: ").strip()
        if integerCheck(a) == False:
            continue
        else:
            break
    print("\n", modularReduction(modulus, a), " mod ", modulus, "\n")

    while True:
        continuance = input("do you want to do another calculation? \n enter yes or no \n ")
        if continuance.lower().strip() == "yes":
            break
        elif continuance.lower().strip() == "no":
            print("\n thank you \n")
            sys.exit()
        else:
            print("your input was not valid")

sys.exit()