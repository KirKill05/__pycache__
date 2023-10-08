elif chs == "The Death": 
    wincond = 0 #variable responsable for deciding result of the game
    print("Death descends in the depth of his realm.")
    DX = 2 #Dextrecity
    IQ = 1 #Inteligence
    HT = -1 #Health
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