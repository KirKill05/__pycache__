if chs == "The Life":
    wincond = 0 #variable responsable for deciding result of the game
    print("Life starts her journey to restore balance.")
    DX = -1 #Dextrecity
    IQ = 2 #Inteligence 
    HT = 1 #Health
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