import random
def throw(r): #function for dice
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
def load(): #function for "loading" effect
    print("Loading...")
    print("...")
    print("...")
    print("...")
Ecl = False #varuable that hides unlockable character
#intro for the game and possible inputs by user
print("Welcome, to the *Quest to the Balance* game!")
print("Balance in the world has been disturbanced and forces from above try to restore or destroy it completly.")
print("Game rules: For each character there are 2 challenges which use dices that have value 2-12.",  
      "Each character has buffs or debuffs for their characteristics.")
print("To win challenge you need to get value 8-12, good luck!")
print("To start the game chose your character(Type their name down to choose them):")
print("The Life")
print("The Death")
if Ecl is False:
    print("Not yet Unlocked")
else:
    print("The Eclipse =)")

chs = input()
if chs == "The Life":
    wincond = 0
    print("Life starts her journey to restore balance.")
    DX = -1
    IQ = 2
    HT = 0
    print("Character stats:")
    print("Dextresity:", DX)
    print("Intelligence:", "+", IQ)
    print("Health:", HT)
    load()
    print("The Water Trial") #first challenge
    print("Floods all across world bury people in the waters. So many lives, took unfairly. Your Intelligence is tested, throw the dice!")
    print("Type: throw")
    if input() == "throw":
        if throw(2) is True:
            print("After that evrything quitens and people celebrate and cheer in the name of The Life, but there is no time to celebrate.",  
                "Another catastrophe beacons on the horizon.")
            wincond += 1
        else:
            print("With all her migth she was unable to save most of the people, but there is no time to dwell.",
                "Soon, there wil be another catastrophe.")
    load()
    print("The Air Trial") #second challenge
    print("Hurricanes sweep towns and howling of the wind drowns out screams of the villagers. Think fast, your Detresity is tested!")
    print("Type: throw")
    if input() == "throw":
        if throw(-1) is True:
            print("Storm clears and humans cheer, the last obstacle is in sight.")
            wincond += 1
        else:
            print("As many lives as possible were saved, there is no time for more. Last obstacle is the more important.")
    load()
    print("The Nature Trial") #third challenge
    print("Forest is full of thorns now, but after it is the centre of the disasters. Your Health is tested!")
    print("Type: throw")
    if input() == "throw":
        if throw(0) is True:
            print("Through thorns you reach the end where light with shining like sun.", 
                "What is left there of the light ate imbalanced scales. And a little note: Next time =)")
            wincond += 1
        else:
            if wincond == 1:
                print("Thorns tear your clothes turning them into rags You collect all your strength in your fist and reach the end.",
                      "There is ")
        
elif chs == "The Death":
    print("Death descends in the depth of his realm.")

#elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is True:
#    print("The opposing forces join the play =).")
#
#elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is False:
#    print("The time...has't come...yet =). Restart the game and choose avaliable options.")

else:
    print("Ops! It seems like something went wrong! Please restart the game.")



