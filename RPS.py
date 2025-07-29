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

def gamestart(rounds, someplayers):
    print(f"\n\nRound {rounds}!!!\n")
    sleep(1)

    while True:
        one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
        computer1 = defcomputer()
        sleep(1) 

        if someplayers == 1:
            if one == 1:
                if computer1 == 1:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer1 == 2:
                    return "computer", computer1, None
                elif computer1 == 3:
                    return "player", computer1, None
                
            elif one == 2:
                if computer1 == 1:
                    return "player", computer1, None
                elif computer1 == 2:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer1 == 3:
                    return "computer", computer1, None
            
            elif one == 3:
                if computer1 == 1:
                    return "computer", computer1, None
                elif computer1 == 2:
                    return "player", computer1, None
                elif computer1 == 3:
                    print("Draw. Again!\n")
                    sleep(1)
           
        elif someplayers == 2:
            computer2 = defcomputer1() 

            if one == 1:
                if computer1 == 1:
                    if computer2 == 1: #111
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #112
                        return "computer3000", computer1, computer2
                    elif computer2 == 3: #113
                        return "player+computer", computer1, computer2
                        

                elif computer1 == 2:
                    if computer2 == 1: #121
                        return "computer", computer1, computer2
                    elif computer2 == 2: #122
                        return "computer+computer3000", computer1, computer2
                    elif computer2 == 3: #123
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 3:
                    if computer2 == 1: #131
                        return "player+computer3000", computer1, computer2
                    elif computer2 == 2: #132
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #133
                        return "player", computer1, computer2

            elif one == 2:
                if computer1 == 1:
                    if computer2 == 1: #211
                        return "player", computer1, computer2
                    elif computer2 == 2: #212
                        return "player+computer3000", computer1, computer2
                    elif computer2 == 3: #213
                        print("Draw. Again!\n")
                        sleep(1)

                elif computer1 == 2:
                    if computer2 == 1: #221
                        return "player+computer", computer1, computer2
                    elif computer2 == 2: #222
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #223
                        return "computer3000", computer1, computer2
                
                elif computer1 == 3:
                    if computer2 == 1: #231
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #232
                        return "computer", computer1, computer2
                    elif computer2 == 3: #233
                        return "computer+computer3000", computer1, computer2

            elif one == 3:
                if computer1 == 1:
                    if computer2 == 1: #311
                        return "computer+computer3000", computer1, computer2
                    elif computer2 == 2: #312
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 3: #313
                        return "computer", computer1, computer2
                        
                elif computer1 == 2:
                    if computer2 == 1: #321
                        print("Draw. Again!\n")
                        sleep(1)
                    elif computer2 == 2: #322
                        return "player", computer1, computer2
                        
                    elif computer2 == 3: #323
                        return "player+computer3000", computer1, computer2
                        
                elif computer1 == 3:
                    if computer2 == 1: #331
                        return "computer3000", computer1, computer2
                        
                    elif computer2 == 2: #332
                        return "player+computer", computer1, computer2
                    elif computer2 == 3: #333
                        print("Draw. Again!\n")
                        sleep(1)

entrance = int(input("\nLet's play Rock Paper Scissors! Yes - 1 or No - 0: "))
sleep(1) 
if entrance == 0:
    print("Okay. Good luck")
    exit()
else:
    someplayers = int(input("\n1 player or 2 players?: "))
    sleep(1)

    rounds = int(input("\nHow many rounds do you want?: "))
    print("")
    sleep(1)

    player = 0
    computer = 0
    computer3000 = 0

    for _rounds_ in range(1, rounds + 1):
        result, computer1, computer2 = gamestart(_rounds_, someplayers)

              
        if someplayers == 1:
            if result == "computer":
                computer += 1
            elif result == "player":
                player += 1

            print(f"Computer chose: {computer1}")
            sleep(1)

            print(f'\nComputer: {computer}; Player: {player}\n')
            sleep(1)

        elif someplayers == 2:
            if result == "computer":
                computer += 1
            elif result == "player":
                player += 1
            elif result == "computer3000":
                computer3000 += 1
            elif result == "player+computer":
                player += 1
                computer += 1
            elif result == "player+computer3000":
                player += 1
                computer3000 += 1
            elif result == "computer+computer3000":
                computer += 1
                computer3000 += 1
        
            print(f"Computer chose {computer1}; Computer3000 chose {computer2}")
            sleep(1)

            print(f"\nPlayer: {player}; Computer: {computer}; Computer3000: {computer3000}\n")   
            sleep(1)

#I need to remake it
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
                elif one == computer1:
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
        if player > computer and player > computer3000:
            print("Congratulations! You took 1st place")

        elif computer > player and computer > computer3000:
            print("You lost! The computer took 1st place. Congratulate him!")

        elif computer3000 > computer and computer3000 > player:
            print("You lost! The computer3000 took 1st place. Congratulate him!")

        elif player == computer and player > computer3000:
            while player == computer:
                one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
                computer1 = defcomputer() 
                sleep(1)
                if one == 1 and computer1 == 2 or one == 2 and computer1 == 3 or one == 3 and computer1 == 1:
                    computer += 1
                    break
                elif one == computer1:
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
                elif one == computer2:
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
                if computer1 == 1 and computer2 == 2 or computer1 == 2 and computer2 == 3 or computer1 == 3 and computer2 == 1:
                    computer3000 += 1
                    break
                elif computer1 == computer2:
                    print("Draw. Again!\n")
                    sleep(1)
                else:
                    computer += 1
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
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 3:
                        if computer2 == 1: #131
                            player += 1
                            computer3000 += 1
                            break
                        elif computer2 == 2: #132
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
                            print("Draw. Again!\n")
                            sleep(1)

                    elif computer1 == 2:
                        if computer2 == 1: #221
                            player += 1
                            computer += 1
                            break
                        elif computer2 == 2: #222
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #223
                            computer3000 += 1
                            break
                    
                    elif computer1 == 3:
                        if computer2 == 1: #231
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
                            print("Draw. Again!\n")
                            sleep(1)
                        elif computer2 == 3: #313
                            computer += 1
                            break
                    elif computer1 == 2:
                        if computer2 == 1: #321
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
                    if computer1 == 1 and computer2 == 2 or computer1 == 2 and computer2 == 3 or computer1 == 3 and computer2 == 1:
                        computer3000 += 1
                        break
                    elif computer1 == computer2:
                        print("Draw. Again!\n")
                        sleep(1)
                    else:
                        computer1 += 1
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
                    elif one == computer1:
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
                    elif one == computer2:
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