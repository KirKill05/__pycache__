import random
def throw(r): #function for dice
    resth = random.randrange(2 + r, 13 + r)
    if resth <= 15 and resth > 10:
        print(resth)
        print("Critical Win")
        return True
    elif resth <= 10 and resth >= 8:
        print(resth)
        print("Win")
        return True
    elif resth <= 7 and resth >= 4:
        print(resth)
        print("Loss")
        return False
    else:
        print(resth)
        print("Critical Loss")
        return False
    
def load(): #function for "loading" effect
    print("Loading...")
    print("...")
    print("...")
    print("...")

#intro for the game and possible inputs by user
print("Welcome, to the *Quest to the Balance* game!")
print("Balance in the world has been disturbed and forces from above try to restore or destroy it completly.")
print("Game rules: For each character there are 3 challenges which use dices that have a value of 2-12.",  
      "Each character has different bonuses for their characteristics.")
print("To win the challenge you need to get a value of 8-12, good luck!")
print("To start the game choose your character (Type their name down to choose them):")
print("Life")
print("Death")


chs = input() #input for the character
if chs == "Life":
    wincond = 0 #varuable responsable for user's win
    print("Life starts its journey to restore the balance.")
    DX = -1 #Character stats
    IQ = 2
    HT = 1
    print("Character stats:")
    print("Dexterity:", DX)
    print("Intelligence:", "+", IQ)
    print("Health:", "+", HT)
    load()
    while True:
        print("The Water Trial") #first challenge
        print("Floods all across the world take people's lives unfairly. Your Intelligence is being tested, throw the dice!")
        print("Type: throw")
        if input() == "throw":
            if throw(IQ) is True:
                print("After that, everything becomes quiet, people celebrate, and cheer in the name of Life, but there is no time to feast!\n",  
                    "Another catastrophe beacons at the horizon.")
                wincond += 1
                break
            else:
                print("With all your strength, you were unable to save most of the people, but there is no time to dwell.\n",
                    "Soon, there will be another catastrophe. Water made your clothes heavier, Dexterity decreased.")
                DX -= 1
                break
        
    load()
    print("The Air Trial") #second challenge
    print("Hurricanes sweep towns and howling of the wind drowns out screams of the villagers. Think fast, your Dexterity is being tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(DX) is True:
                print("The storm clears and humans cheer, the last obstacle is in sight.")
                wincond += 1
                break
            else:
                print("As many lives as possible were saved, but you need to keep going. The last obstacle is the most important.\n", 
                    "Hurricane hurts you, Health decreased.")
                HT -= 1
                break
    load()
    print("The Nature Trial") #third challenge
    print("Forest is full of thorns now, but after it, is the centre of the disasters. Your Health is being tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(HT) is True or wincond == 2:
                print("Going through the thorns you reach the end where light shines like the sun.\n", 
                    "What is left there of the light are imbalanced scales and a little note: 'Til next time =)")
                wincond += 1
                break
            elif wincond >= 1:
                print("Thorns tear your clothes turning them into rags. You collect all your strength in your fist and reach the end.\n",
                        "There are only broken scales standing there; Silently.")
                break
            else:
                print("This is over, no... more... strength...\n", "Game over, try again after restarting.")
                break

    if wincond >= 2:
        print("Conratulations, you got the Good Ending, thank you for playing my game!")
    elif wincond == 1:
        print("Luck is not on your side today! You got the Neutral Ending, thank you for playing my game!")
        
elif chs == "Death":
    wincond = 0
    print("Death descends in the depth of its realm.")
    DX = 2
    IQ = 1
    HT = -1
    print("Character stats:")
    print("Dexterity:", "+", DX)
    print("Intelligence:", "+", IQ)
    print("Health:", HT)
    load()
    print("The Greed Trial") #first challenge
    print("In front of you there is a room with loads of gems, piles of gold, and a door to the next trial.\n", 
          "The voices whisper, hypnotizing you: 'Take some, it will definitely benefit you =)'.\n", 
          "Your Intelligence (Wisdom) is being tested, throw the dice!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(IQ) is True:
                print("Hypnosis didn't work on you and with your feet you sweep the gold away to reach the next door.",  
                    "Another trial is waiting.")
                wincond += 1
                break
            else:
                print("'Yes...' you reply, 'yes, it won't hurt taking some.'\n",
                    "With heavy tinkling bag you approach the door to the next obstacle, Dexterity decreased.")
                DX -= 1
                break
    load()
    print("The Anger Trial") #second challenge
    print("'So, do you understand what is hapenning, the Immortal Lord? We, deadly sins, are sick of being your slaves, fight us!' Anger shouts.\n", 
          "Prepare for battle, your Dexterity is being tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(DX) is True:
                print("'I am just one of the obstacles, the last one is scarier.' Anger disappears into the black void with evil laughter.\n",
                    "'Who is pulling your strings?' you ask approaching the door.")
                wincond += 1
                break
            else:
                print("In the intense battle you manage to deal the final blow to Anger.\n", 
                    "'After him what is the last obstacle?' you question yourself.\n", 
                    "You were injured during the battle, Health decreased.")
                HT -= 1
                break
    load()
    print("The Gluttony Trial") #third challenge
    print("In front of you there is a long banquet table at the end of which sits an obese monstrosity with no eyes and a giagintic mouth on his belly.")
    print("You look around, but there is no door to enter to the centre of catastrophes. Deep-tone laughter interrups the silence.\n", 
          "'Looking for something you silly Lord? It is right inside of me, but before I let you take it, try some tasty cake and I will let you in.'\n", 
          "Your Health is tested!")
    print("Type: throw")
    while True:
        if input() == "throw":
            if throw(HT) is True or wincond == 2:
                print("Poison in the cake was unable to affect you. 'Huh, I knew he was tricking me, but a deal is a deal' Gluttony opens his mouth wide and you get in.", 
                    "Interestingly, you get in the room with imbalanced scales and a little note: 'Til next time =)")
                wincond += 1
                break
            elif wincond >= 1:
                print("You feel dizzy and everything is swaying from side to side, but you stand. 'Bahahaha, tough nut eh? Still, you are alive, so just get inside.'\n",
                        "You get through Glutonny's belly mouth and get in the room. There are only broken scales standing there; Silently.")
                break
            else:
                print("Everything starts to fade before your eyes and you fall in the everlasting sleep.\n",
                    "'But...I am.....The Death...'\nGame over, try again after restarting.")
                break
    
    if wincond >= 2:
        print("Conratulations, you got the Good Ending, thank you for playing my game!")
    elif wincond == 1:
        print("Luck is not on your side today! You got the Neutral Ending, thank you for playing my game!")

else:
    print("Oops! It seems like something went wrong! Please restart the game.")

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


