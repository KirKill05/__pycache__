chs == "Death":
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
        if throw(HT) is True:
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