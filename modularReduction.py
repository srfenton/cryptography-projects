import sys

def modularReduction(m, a):
    a = int(a)
    m = int(m)
    q = a // m
    r = a - q * m

    return r

m = input("Please enter the modulus: \n")
a = input("Please enter a number to reduce: \n")

print("\n", modularReduction(m, a), " mod ", m, "\n")

sys.exit()