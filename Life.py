#Life character
if chs == "Life":
    wincond = 0
    print("Life starts its journey to restore the balance.")
    DX = -1
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
            if throw(HT) is True:
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