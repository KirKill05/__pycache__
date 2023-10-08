import random
def throw(r): #function for dice
    resth = random.randrange(2 + r, 13 + r)
    if resth <= 15 and resth > 10:
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
#intro for the game and possible inputs by user
print("Welcome, to the *Quest to the Balance* game!")
print("Balance in the world has been disturbanced and forces from above try to restore or destroy it completly.")
print("Game rules: For each character there are 2 challenges which use dices that have value 2-12.",  
      "Each character has buffs or debuffs for their characteristics.")
print("To win challenge you need to get value 8-12, good luck!")
print("To start the game chose your character(Type their name down to choose them):")
print("The Life")
print("The Death")


chs = input()
if chs == "The Life":
    wincond = 0
    print("Life starts her journey to restore balance.")
    DX = -1
    IQ = 2
    HT = 1
    print("Character stats:")
    print("Dextresity:", DX)
    print("Intelligence:", "+", IQ)
    print("Health:", HT)
    load()
    while True:
        print("The Water Trial") #first challenge
        print("Floods all across world bury people in the waters. So many lives, took unfairly. Your Intelligence is tested, throw the dice!")
        print("Type: throw")
        if input() == "throw":
            if throw(IQ) is True:
                print("After that evrything quitens and people celebrate and cheer in the name of The Life, but there is no time to celebrate.\n",  
                    "Another catastrophe beacons on the horizon.")
                wincond += 1
                break
            else:
                print("With all her migth she was unable to save most of the people, but there is no time to dwell.\n",
                    "Soon, there wil be another catastrophe. Water made your clothes heavier, Dextresity decreased.")
                DX -= 1
                break
        
    load()
    print("The Air Trial") #second challenge
    print("Hurricanes sweep towns and howling of the wind drowns out screams of the villagers. Think fast, your Detresity is tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(DX) is True:
                print("Storm clears and humans cheer, the last obstacle is in sight.")
                wincond += 1
                break
            else:
                print("As many lives as possible were saved, there is no time for more. Last obstacle is the most important.\n", 
                    "Hurricane hurt you, Health decreased.")
                HT -= 1
                break
    load()
    print("The Nature Trial") #third challenge
    print("Forest is full of thorns now, but after it is the centre of the disasters. Your Health is tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(HT) is True:
                print("Through thorns you reach the end where light with shining like sun.\n", 
                    "What is left there of the light are imbalanced scales and a little note: Next time =)")
                wincond += 1
                break
            elif wincond == 1:
                print("Thorns tear your clothes turning them into rags You collect all your strength in your fist and reach the end.\n",
                        "There are only broken scales standing there. Silently.")
                break
            else:
                print("This is over, no... more... strength...\n", "Game over, try again after restarting.")
                break

    if wincond >= 2:
        print("Conratulations, you got the Good ending, thank you for playing my game!")
    elif wincond == 1:
        print("Luck is not on your side today! You got Neutral Ending, thank you for playing my game!")
        
elif chs == "The Death":
    wincond = 0
    print("Death descends in the depth of his realm.")
    DX = 2
    IQ = 1
    HT = -1
    print("Character stats:")
    print("Dextresity:", DX)
    print("Intelligence:", "+", IQ)
    print("Health:", HT)
    load()
    print("The Greed Trial") #first challenge
    print("In front of you there is a room with loads of shiny stones and piles of gold sand and a door to next trial.\n", 
          "The voices whisper, hypnotizing you: take some, it will definitely benefit you =).\n", 
          "Your Intelligence(Wisdom) is tested, throw the dice!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(IQ) is True:
                print("Hypnosis didn't work on you and with your feet you sweep the gold away to reach the next door.",  
                    "Another trial is waiting.")
                wincond += 1
                break
            else:
                print("Yes - you reply - yes, it won't hurt taking some, just some gold pieces.\n",
                    "With heavy tinkling bag you approach door to the next obstacle, Dextresity decreased.")
                DX -= 1
                break
    load()
    print("The Anger Trial") #second challenge
    print("So, do you understand what is hapenning, the Immortal Lord? We - deadly sins are sick of being your slaves, fight us!\n", 
          "Prepare for battle, your Detresity is tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(DX) is True:
                print("I am just one of the obstacles, the last is scarier - Anger disappears in the black void with evil laughter.\n",
                    "Who is pulling your strings? - you ask approaching the door.")
                wincond += 1
                break
            else:
                print("In the intense battle you manage to deal the final blow to Anger.\n", 
                    "After him what is the last obstacle? - you question yourself.\n", 
                    "You were injured during the battle, Health decreased.")
                HT -= 1
                break
    load()
    print("The Gluttony Trial") #third challenge
    print("In front of you there is a long banquet table in the end of which obesse monstrosity with no eyes and giagintic mouth on his belly enjoys the feast.")
    print("You look around, but there is no door to enter to the centre. Deep-tone laughter interrups the silence.\n", 
          "Looking for something you silly lord? It is right inside me, but before I let you take it, try some tasty Cake and I will let you in.\n", 
          "Your Health is tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(HT) is True:
                print("Poison in the cake was unable to affect you. Huh, I knew he was tricking me, but deal is deal - Gluttone opens wide his mouth and you get in.", 
                    "Intrestengly you get in the room with imbalanced scales and a little note: Next time =)")
                wincond += 1
                break
            elif wincond == 1:
                print("You feel dizzy and everything is swaying from side to side, but you stand. Bahaha, tough nut eh? Still, you are alive, so just get inside.\n",
                        "You get through Glutonne's belly mouth and get in the room. There are only broken scales standing there. Silently.")
                break
            else:
                print("Everything starts to fade before your eyes and you fall in the everlasting sleep.\n",
                    "But...I am.....The death...\nGame over, try again after restarting.")
                break
    
    if wincond >= 2:
        print("Conratulations, you got the Good ending, thank you for playing my game!")
    elif wincond == 1:
        print("Luck is not on your side today! You got Neutral Ending, thank you for playing my game!")

else:
    print("Ops! It seems like something went wrong! Please restart the game.")

#Unused stuff for third character
#Ecl = False #varuable that hides unlockable character
#if Ecl is False:
#    print("Not yet Unlocked")
#else:
#    print("The Eclipse =)")

#elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is True:
#    print("The opposing forces join the play =).")
#
#elif (chs == "The Eclipse" or  chs == "The Eclipse =)") and Ecl is False:
#    print("The time...has't come...yet =). Restart the game and choose avaliable options.") 


