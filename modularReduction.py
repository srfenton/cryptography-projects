import sys

def integerCheck(integer):
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        return False
    else:
        return True

def modularReduction(m, a):
    a = int(a)
    m = int(m)
    q = a // m
    r = a - q * m

    return r

while True:
    print("Please enter a modulus: ")
    m = input()
    if integerCheck(m) == False:
        continue
    elif int(m) == 0:
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

print("\n", modularReduction(m, a), " mod ", m, "\n")

sys.exit()