import sys

def integerCheck(integer):
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
    if a > 0:
        r = a % modulus
    elif a < 0:
        pass


    return r

while True:
    print("Please enter a modulus: ")
    modulus = input()
    if integerCheck(modulus) == False:
        continue
    elif int(modulus) <= 0:
        print("the modulus must be greater than 0.")
        continue
    else:
        break

while True:
    print("Please enter a number to reduce: ")
    a = input()
    if integerCheck(a) == False:
        continue
    else:
        break

print("\n", modularReduction(modulus, a), " mod ", modulus, "\n")

sys.exit()