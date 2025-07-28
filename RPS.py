from random import randrange
from time import sleep

def defcomputer():
    computerchoice = ["Rock", "Paper", "Scissors"]
    computer1 = randrange(len(computerchoice))
    return computer1 + 1

def defcomputer1():
    computerchoice1 = ["Rock", "Paper", "Scissors"]
    computer2 = randrange(len(computerchoice1))
    return computer2 + 1

entrance = int(input("\nLet's play Rock Paper Scissors! Yes - 1 or No - 0: "))
sleep(1) 
if entrance == 0:
    print("Okay. Good luck")
    exit()
else:
    someplayers = int(input("\n1 player or 2 players?: "))
    sleep(1)

    rounds = int(input("\n3 rounds or 6 rounds?: "))
    sleep(1)

    player = 0
    computer = 0
    computer3000 = 0



    print('\n\nRound 1!!!\n')
    sleep(1)

    while True:
        one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
        computer1 = defcomputer()
        sleep(1) 

        if someplayers == 1:
            if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                computer += 1
                break
            elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                player += 0
                print("Draw. Again!\n")
                sleep(1)
            else:
                player += 1
                break
           
        elif someplayers == 2:
            computer1 = defcomputer() 
            computer2 = defcomputer1() 

            if one == 1:
                if computer1 == 1:
                    if computer2 == 1: #111
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #112
                        computer3000 += 1
                        break
                    elif computer2 == 3: #113
                        player += 1
                        computer += 1
                        break

                elif computer1 == 2:
                    if computer2 == 1: #121
                        computer += 1
                        break
                    elif computer2 == 2: #122
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #123
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 3:
                    if computer2 == 1: #131
                        player += 1
                        computer2 += 1
                        break
                    elif computer2 == 2: #132
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #133
                        player += 1
                        break

            elif one == 2:
                if computer1 == 1:
                    if computer2 == 1: #211
                        player += 1
                        break
                    elif computer2 == 2: #212
                        player += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #213
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 2:
                    if computer2 == 1: #221
                        player += 1
                        computer1 += 1
                        break
                    elif computer2 == 2: #222
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #223
                        computer3000 += 1
                        break
                
                elif computer1 == 3:
                    if computer2 == 1: #231
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #232
                        computer += 1
                        break
                    elif computer2 == 3: #233
                        computer += 1
                        computer3000 += 1
                        break

            elif one == 3:
                if computer1 == 1:
                    if computer2 == 1: #311
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 2: #312
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #313
                        computer += 1
                        break
                elif computer1 == 2:
                    if computer2 == 1: #321
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #322
                        player += 1
                        break
                    elif computer2 == 3: #323
                        player += 1
                        computer3000 += 1
                        break
                elif computer1 == 3:
                    if computer2 == 1: #331
                        computer3000 += 1
                        break
                    elif computer2 == 2: #332
                        player += 1
                        computer += 1
                    elif computer2 == 3: #333
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

    sleep(1)        
    if someplayers == 1:
        print(f"Computer chose: {computer1}")
        sleep(1)

        print(f'\nComputer: {computer}; Player: {player}\n')
        sleep(1)

    elif someplayers == 2:
        print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
        sleep(1)

        print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")   
        sleep(1) 
    

    print("\nRound 2!\n")
    sleep(1)

    while True:
        one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
        computer1 = defcomputer()
        sleep(1)

        if someplayers == 1:
            if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                computer += 1
                break
            elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                player += 0
                print("Draw. Again!\n")
                sleep(1)
            else:
                player += 1
                break
            
        elif someplayers == 2:

            computer1 = defcomputer() 
            computer2 = defcomputer1() 

            if one == 1:
                if computer1 == 1:
                    if computer2 == 1: #111
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #112
                        computer3000 += 1
                        break
                    elif computer2 == 3: #113
                        player += 1
                        computer += 1
                        break

                elif computer1 == 2:
                    if computer2 == 1: #121
                        computer += 1
                        break
                    elif computer2 == 2: #122
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #123
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 3:
                    if computer2 == 1: #131
                        player += 1
                        computer2 += 1
                        break
                    elif computer2 == 2: #132
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #133
                        player += 1
                        break

            elif one == 2:
                if computer1 == 1:
                    if computer2 == 1: #211
                        player += 1
                        break
                    elif computer2 == 2: #212
                        player += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #213
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 2:
                    if computer2 == 1: #221
                        player += 1
                        computer1 += 1
                        break
                    elif computer2 == 2: #222
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #223
                        computer3000 += 1
                        break
                
                elif computer1 == 3:
                    if computer2 == 1: #231
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #232
                        computer += 1
                        break
                    elif computer2 == 3: #233
                        computer += 1
                        computer3000 += 1
                        break

            elif one == 3:
                if computer1 == 1:
                    if computer2 == 1: #311
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 2: #312
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #313
                        computer += 1
                        break
                elif computer1 == 2:
                    if computer2 == 1: #321
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #322
                        player += 1
                        break
                    elif computer2 == 3: #323
                        player += 1
                        computer3000 += 1
                        break
                elif computer1 == 3:
                    if computer2 == 1: #331
                        computer3000 += 1
                        break
                    elif computer2 == 2: #332
                        player += 1
                        computer += 1
                    elif computer2 == 3: #333
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

    sleep(1)        
    if someplayers == 1:
        print(f"Computer chose: {computer1}")
        sleep(1)

        print(f'\nComputer: {computer}; Player: {player}\n')
        sleep(1)

    elif someplayers == 2:
        print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
        sleep(1)

        print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")
        sleep(1)
    

    print("\nRound 3!\n")
    sleep(1)

    while True:
        one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
        computer1 = defcomputer()
        sleep(1)

        if someplayers == 1:
            if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                computer += 1
                break
            elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                player += 0
                print("Draw. Again!\n")
                sleep(1)
            else:
                player += 1
                break
            
        elif someplayers == 2:
            computer1 = defcomputer() 
            computer2 = defcomputer1() 

            if one == 1:
                if computer1 == 1:
                    if computer2 == 1: #111
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #112
                        computer3000 += 1
                        break
                    elif computer2 == 3: #113
                        player += 1
                        computer += 1
                        break

                elif computer1 == 2:
                    if computer2 == 1: #121
                        computer += 1
                        break
                    elif computer2 == 2: #122
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #123
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 3:
                    if computer2 == 1: #131
                        player += 1
                        computer2 += 1
                        break
                    elif computer2 == 2: #132
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #133
                        player += 1
                        break

            elif one == 2:
                if computer1 == 1:
                    if computer2 == 1: #211
                        player += 1
                        break
                    elif computer2 == 2: #212
                        player += 1
                        computer3000 += 1
                        break
                    elif computer2 == 3: #213
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 2:
                    if computer2 == 1: #221
                        player += 1
                        computer1 += 1
                        break
                    elif computer2 == 2: #222
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #223
                        computer3000 += 1
                        break
                
                elif computer1 == 3:
                    if computer2 == 1: #231
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #232
                        computer += 1
                        break
                    elif computer2 == 3: #233
                        computer += 1
                        computer3000 += 1
                        break

            elif one == 3:
                if computer1 == 1:
                    if computer2 == 1: #311
                        computer += 1
                        computer3000 += 1
                        break
                    elif computer2 == 2: #312
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #313
                        computer += 1
                        break
                elif computer1 == 2:
                    if computer2 == 1: #321
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #322
                        player += 1
                        break
                    elif computer2 == 3: #323
                        player += 1
                        computer3000 += 1
                        break
                elif computer1 == 3:
                    if computer2 == 1: #331
                        computer3000 += 1
                        break
                    elif computer2 == 2: #332
                        player += 1
                        computer += 1
                    elif computer2 == 3: #333
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)

    sleep(1)        
    if someplayers == 1:
        print(f"Computer chose: {computer1}")
        sleep(1)

        print(f'\nComputer: {computer}; Player: {player}\n')
        sleep(1)

    elif someplayers == 2:
        print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
        sleep(1)

        print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")
        sleep(1)

    if rounds == 6:
        print("\nRound 4!\n")
        sleep(1)

        while True:
            one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
            computer1 = defcomputer()
            sleep(1)

            if someplayers == 1:
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
                
            elif someplayers == 2:
                computer1 = defcomputer() 
                computer2 = defcomputer1() 

                if one == 1:
                    if computer1 == 1:
                        if computer2 == 1: #111
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #112
                            computer3000 += 1
                            break
                        elif computer2 == 3: #113
                            player += 1
                            computer += 1
                            break

                    elif computer1 == 2:
                        if computer2 == 1: #121
                            computer += 1
                            break
                        elif computer2 == 2: #122
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #123
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 3:
                        if computer2 == 1: #131
                            player += 1
                            computer2 += 1
                            break
                        elif computer2 == 2: #132
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #133
                            player += 1
                            break

                elif one == 2:
                    if computer1 == 1:
                        if computer2 == 1: #211
                            player += 1
                            break
                        elif computer2 == 2: #212
                            player += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #213
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 2:
                        if computer2 == 1: #221
                            player += 1
                            computer1 += 1
                            break
                        elif computer2 == 2: #222
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #223
                            computer3000 += 1
                            break
                    
                    elif computer1 == 3:
                        if computer2 == 1: #231
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #232
                            computer += 1
                            break
                        elif computer2 == 3: #233
                            computer += 1
                            computer3000 += 1
                            break

                elif one == 3:
                    if computer1 == 1:
                        if computer2 == 1: #311
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 2: #312
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #313
                            computer += 1
                            break
                    elif computer1 == 2:
                        if computer2 == 1: #321
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #322
                            player += 1
                            break
                        elif computer2 == 3: #323
                            player += 1
                            computer3000 += 1
                            break
                    elif computer1 == 3:
                        if computer2 == 1: #331
                            computer3000 += 1
                            break
                        elif computer2 == 2: #332
                            player += 1
                            computer += 1
                        elif computer2 == 3: #333
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

        sleep(1)        
        if someplayers == 1:
            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}\n')
            sleep(1)

        elif someplayers == 2:
            print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
            sleep(1)

            print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")
            sleep(1)

        print("\nRound 5!\n")
        sleep(1)

        while True:
            one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
            computer1 = defcomputer()
            sleep(1)

            if someplayers == 1:
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
                
            elif someplayers == 2:
                computer1 = defcomputer() 
                computer2 = defcomputer1() 

                if one == 1:
                    if computer1 == 1:
                        if computer2 == 1: #111
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #112
                            computer3000 += 1
                            break
                        elif computer2 == 3: #113
                            player += 1
                            computer += 1
                            break

                    elif computer1 == 2:
                        if computer2 == 1: #121
                            computer += 1
                            break
                        elif computer2 == 2: #122
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #123
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 3:
                        if computer2 == 1: #131
                            player += 1
                            computer2 += 1
                            break
                        elif computer2 == 2: #132
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #133
                            player += 1
                            break

                elif one == 2:
                    if computer1 == 1:
                        if computer2 == 1: #211
                            player += 1
                            break
                        elif computer2 == 2: #212
                            player += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #213
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 2:
                        if computer2 == 1: #221
                            player += 1
                            computer1 += 1
                            break
                        elif computer2 == 2: #222
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #223
                            computer3000 += 1
                            break
                    
                    elif computer1 == 3:
                        if computer2 == 1: #231
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #232
                            computer += 1
                            break
                        elif computer2 == 3: #233
                            computer += 1
                            computer3000 += 1
                            break

                elif one == 3:
                    if computer1 == 1:
                        if computer2 == 1: #311
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 2: #312
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #313
                            computer += 1
                            break
                    elif computer1 == 2:
                        if computer2 == 1: #321
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #322
                            player += 1
                            break
                        elif computer2 == 3: #323
                            player += 1
                            computer3000 += 1
                            break
                    elif computer1 == 3:
                        if computer2 == 1: #331
                            computer3000 += 1
                            break
                        elif computer2 == 2: #332
                            player += 1
                            computer += 1
                        elif computer2 == 3: #333
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

        sleep(1)        
        if someplayers == 1:
            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}\n')
            sleep(1)

        elif someplayers == 2:
            print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
            sleep(1)

            print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")
            sleep(1)

        print("\nRound 6!\n")
        sleep(1)

        while True:
            one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
            computer1 = defcomputer() 
            sleep(1)

            if someplayers == 1:
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
                
            elif someplayers == 2:
                computer1 = defcomputer() 
                computer2 = defcomputer1() 

                if one == 1:
                    if computer1 == 1:
                        if computer2 == 1: #111
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #112
                            computer3000 += 1
                            break
                        elif computer2 == 3: #113
                            player += 1
                            computer += 1
                            break

                    elif computer1 == 2:
                        if computer2 == 1: #121
                            computer += 1
                            break
                        elif computer2 == 2: #122
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #123
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 3:
                        if computer2 == 1: #131
                            player += 1
                            computer2 += 1
                            break
                        elif computer2 == 2: #132
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #133
                            player += 1
                            break

                elif one == 2:
                    if computer1 == 1:
                        if computer2 == 1: #211
                            player += 1
                            break
                        elif computer2 == 2: #212
                            player += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #213
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 2:
                        if computer2 == 1: #221
                            player += 1
                            computer1 += 1
                            break
                        elif computer2 == 2: #222
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #223
                            computer3000 += 1
                            break
                    
                    elif computer1 == 3:
                        if computer2 == 1: #231
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #232
                            computer += 1
                            break
                        elif computer2 == 3: #233
                            computer += 1
                            computer3000 += 1
                            break

                elif one == 3:
                    if computer1 == 1:
                        if computer2 == 1: #311
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 2: #312
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #313
                            computer += 1
                            break
                    elif computer1 == 2:
                        if computer2 == 1: #321
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #322
                            player += 1
                            break
                        elif computer2 == 3: #323
                            player += 1
                            computer3000 += 1
                            break
                    elif computer1 == 3:
                        if computer2 == 1: #331
                            computer3000 += 1
                            break
                        elif computer2 == 2: #332
                            player += 1
                            computer += 1
                        elif computer2 == 3: #333
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

        sleep(1)
        if someplayers == 1:
            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}')
            sleep(1)

        elif someplayers == 2:
            print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
            sleep(1)

            print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")
            sleep(1)

    if someplayers == 1:
        if player > computer:
            print("Congratulations! You took 1st place")
        elif player < computer:
            print("You lost! The computer took 1st place. Congratulate him!")

        elif player == computer:
            while player == computer:
                one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                computer1 = defcomputer() 
                sleep(1)
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
            sleep(1)
            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}')
            sleep(1)

            if player > computer:
                print("Congratulations! You took 1st place")
            elif player < computer:
                print("You lost! The computer took 1st place. Congratulate him!")                    

    elif someplayers == 2:
        if player > computer or player > computer3000:
            print("Congratulations! You took 1st place")

        elif computer > player or computer > computer3000:
            print("You lost! The computer took 1st place. Congratulate him!")

        elif computer3000 > computer or computer3000 > player:
            print("You lost! The computer3000 took 1st place. Congratulate him!")

        elif player == computer and player > computer3000:
            while player == computer:
                one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                computer1 = defcomputer() 
                sleep(1)
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break

            sleep(1)
            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}')
            sleep(1)

            if player > computer:
                print("Congratulations! You took 1st place")
            elif player < computer:
                print("You lost! The computer took 1st place. Congratulate him!")
        
        elif player == computer3000 and player > computer:
            while player == computer3000:
                one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                computer2 = defcomputer1() 
                sleep(1)
                if one == 1 and computer2 == 2 or one == 2 and computer2 == 3 or one == 3 and computer2 == 1:
                    computer3000 += 1
                    break
                elif one == 1 and computer2 == 1 or one == 2 and computer2 == 2 or one == 3 and computer2 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
            sleep(1)
            print(f"Computer3000 chose: {computer2}")
            sleep(1)

            print(f'\nComputer3000: {computer2}; Player: {player}')
            sleep(1)

            if player > computer3000:
                print("Congratulations! You took 1st place")
            elif player < computer3000:
                print("You lost! The computer took 1st place. Congratulate him!")

        elif computer == computer3000 and computer > player:
            while computer == computer3000:
                computer1 = defcomputer()
                computer2 = defcomputer1() 
                sleep(1)
                if one == 1 and computer2 == 2 or one == 2 and computer2 == 3 or one == 3 and computer2 == 1:
                    computer3000 += 1
                    break
                elif one == 1 and computer2 == 1 or one == 2 and computer2 == 2 or one == 3 and computer2 == 3:
                    player += 0
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    player += 1
                    break
            sleep(1)
            print(f"Computer chose: {computer1}; Computer3000 chose: {computer2}")
            sleep(1)

            print(f'\nComputer: {computer}; Computer3000: {computer3000}')
            sleep(1)

            if computer > computer3000:
                print("You lost! The computer took 1st place. Congratulate him!")
            elif computer < computer3000:
                print("You lost! The computer3000 took 1st place. Congratulate him!")

        elif player == computer == computer3000:
            while player == computer == computer3000:
                one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                computer1 = defcomputer() 
                computer2 = defcomputer1() 
                if one == 1:
                    if computer1 == 1:
                        if computer2 == 1: #111
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #112
                            computer3000 += 1
                            break
                        elif computer2 == 3: #113
                            player += 1
                            computer += 1
                            break

                    elif computer1 == 2:
                        if computer2 == 1: #121
                            computer += 1
                            break
                        elif computer2 == 2: #122
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #123
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 3:
                        if computer2 == 1: #131
                            player += 1
                            computer2 += 1
                            break
                        elif computer2 == 2: #132
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #133
                            player += 1
                            break

                elif one == 2:
                    if computer1 == 1:
                        if computer2 == 1: #211
                            player += 1
                            break
                        elif computer2 == 2: #212
                            player += 1
                            computer3000 += 1
                            break
                        elif computer2 == 3: #213
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 2:
                        if computer2 == 1: #221
                            player += 1
                            computer1 += 1
                            break
                        elif computer2 == 2: #222
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #223
                            computer3000 += 1
                            break
                    
                    elif computer1 == 3:
                        if computer2 == 1: #231
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #232
                            computer += 1
                            break
                        elif computer2 == 3: #233
                            computer += 1
                            computer3000 += 1
                            break

                elif one == 3:
                    if computer1 == 1:
                        if computer2 == 1: #311
                            computer += 1
                            computer3000 += 1
                            break
                        elif computer2 == 2: #312
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #313
                            computer += 1
                            break
                    elif computer1 == 2:
                        if computer2 == 1: #321
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 2: #322
                            player += 1
                            break
                        elif computer2 == 3: #323
                            player += 1
                            computer3000 += 1
                            break
                    elif computer1 == 3:
                        if computer2 == 1: #331
                            computer3000 += 1
                            break
                        elif computer2 == 2: #332
                            player += 1
                            computer += 1
                        elif computer2 == 3: #333
                            player += 0
                            print("Draw. Again!\n")
                            sleep(1)

            if player > computer and computer >= computer3000:
                print("Congratulations! You took 1st place")

            elif computer > player and player >= computer3000:
                print("You lost! The computer took 1st place. Congratulate him!")

            elif computer3000 > player and player >= computer:
                print("You lost! The computer3000 took 1st place. Congratulate him!")

            elif computer == computer3000 and computer > player:
                while computer == computer3000:
                    computer1 = defcomputer()
                    computer2 = defcomputer1() 
                    sleep(1)
                    if one == 1 and computer2 == 2 or one == 2 and computer2 == 3 or one == 3 and computer2 == 1:
                        computer3000 += 1
                        break
                    elif one == 1 and computer2 == 1 or one == 2 and computer2 == 2 or one == 3 and computer2 == 3:
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    else:
                        player += 1
                        break
                
                sleep(1)
                print(f"Computer chose: {computer1}; Computer3000 chose: {computer2}")
                sleep(1)

                print(f'\nComputer: {computer}; Computer3000: {computer3000}')
                sleep(1)

                if computer > computer3000:
                    print("You lost! The computer took 1st place. Congratulate him!")
                elif computer < computer3000:
                    print("You lost! The computer3000 took 1st place. Congratulate him!")

            elif player == computer and player > computer3000:
                while player == computer:
                    one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                    computer1 = defcomputer()
                    sleep(1)

                    if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                        computer += 1
                        break
                    elif one == 1 and computer1 == 1 or one == 2 and computer1 == 2 or one == 3 and computer1 == 3:
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    else:
                        player += 1
                        break

                sleep(1)
                print(f"Computer chose: {computer1}")
                sleep(1)

                print(f'\nComputer: {computer}; Player: {player}')
                sleep(1)

                if player > computer:
                    print("Congratulations! You took 1st place")
                elif player < computer:
                    print("You lost! The computer took 1st place. Congratulate him!")

            elif player == computer3000 and player > computer:
                while player == computer3000:
                    one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                    computer2 = defcomputer1()
                    sleep(1)
                    if one == 1 and computer2 == 2 or one == 2 and computer2 == 3 or one == 3 and computer2 == 1:
                        computer += 1
                        break
                    elif one == 1 and computer2 == 1 or one == 2 and computer2 == 2 or one == 3 and computer2 == 3:
                        player += 0
                        print("Draw. Again!\n")
                        sleep(1)
                    else:
                        player += 1
                        break
            sleep(1)
            print(f"Computer chose: {computer2}")
            sleep(1)

            print(f'\nComputer3000: {computer3000}; Player: {player}')
            sleep(1)

            if player > computer3000:
                print("Congratulations! You took 1st place")
            elif player < computer3000:
                print("You lost! The computer took 1st place. Congratulate him!")