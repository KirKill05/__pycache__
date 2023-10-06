import random
def throw():
    resth = random.randrange(2, 13)
    if resth <= 12 and resth > 10:
        print("Critical win")
        return True
    elif resth <= 10 and resth >= 8:
        print("Win")
        return True
    elif resth <= 7 and resth >= 4:
        print("Lose")
        return True
    else:
        print("Critical lose")
        return True
    
if throw() is True:
    print("Success")
else;
    print("Failure :(")