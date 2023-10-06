import random
def throw(r):
    resth = random.randrange(2 + r, 13 + r)
    if resth <= 12 and resth > 10:
        print(resth)
        print("Critical win")
        return True
    elif resth <= 10 and resth >= 8:
        print(resth)
        print("Win")
        return True
    elif resth <= 7 and resth >= 4:
        print(resth)
        print("Lose")
        return False
    else:
        print(resth)
        print("Critical lose")
        return False
    
if throw(-1) is True:
    print("Success")
else:
    print(lol)