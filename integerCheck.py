def integerCheck(integer):
    try:
        integer = (int(integer))
    except ValueError:
        print("Your input was invalid.")
        print("1")
        return False
    else:
        return True

while True:
    test = input("enter an integer:")
    if integerCheck(test) == False:
        continue
    else:
        break
