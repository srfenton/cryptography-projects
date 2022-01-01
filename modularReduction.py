import sys

def integerCheck(integer):
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        print("1")
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
    m = input("enter an integer:")
    if integerCheck(m) == False:
        continue
    elif m == 0
        print("the modulus must be great than 0.")
    else:
        break

while True:
    while True:
    a = input("enter an integer:")
    if integerCheck(a) == False:
        continue
    else:
        break

print("\n", modularReduction(m, a), " mod ", m, "\n")

sys.exit()