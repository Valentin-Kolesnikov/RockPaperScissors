from secrets import choice
from time import sleep
from random import uniform
from math import ceil
from sys import exit

def defcomputer():
    computer1 = []
    for i in range(3):
        number = uniform(0.000001, 3.0)
        numbers = ceil(number)
        computer1.append(numbers)
    return choice(computer1)

def defcomputer1():
    computer2 = []
    for i in range(3):
        number1 = uniform(0.000001, 3.0)
        numbers1 = ceil(number1)
        computer2.append(numbers1)
    return choice(computer2)
    
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

def final(player, computer, computer3000, finale):
    if finale == 3:
        result, computer1, computer2 = gamestart("MAYBELAST", 2)

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
        return player, computer, computer3000
        
    elif finale == 212:
        result, computer1, computer2 = gamestart("LAST", 1)

        if result == "computer":
            computer += 1
        elif result == "player":
            player += 1

        print(f"Computer chose: {computer1}")
        sleep(1)

        print(f'\nComputer: {computer}; Player: {player}\n')
        sleep(1)
        return player, computer
    
    elif finale == 213:
        while True:
            one = int(input("\nRock: 1; Paper: 2; Scissors: 3. Choose: "))
            computer2 = defcomputer1()
            sleep(1) 

            if one == 1:
                if computer2 == 1:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer2 == 2:
                    computer3000 += 1
                    break
                elif computer2 == 3:
                    player += 1
                    break
                
            elif one == 2:
                if computer2 == 1:
                    player += 1
                    break
                elif computer2 == 2:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer2 == 3:
                    computer3000 += 1
                    break
            
            elif one == 3:
                if computer2 == 1:
                    computer3000 += 1
                    break
                elif computer2 == 2:
                    player += 1
                    break
                elif computer2 == 3:
                    print("Draw. Again!\n")
                    sleep(1)
        sleep(1)
        print(f"Computer3000 chose: {computer2}")
        sleep(1)

        print(f'\nComputer3000: {computer3000}; Player: {player}')
        sleep(1)
        return player, computer3000
    
    elif finale == 223:
        while True:
            computer1 = defcomputer()
            computer2 = defcomputer1()
            sleep(1) 

            if computer == 1:
                if computer2 == 1:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer2 == 2:
                    computer3000 += 1
                    break
                elif computer2 == 3:
                    computer += 1
                    break
                
            elif computer == 2:
                if computer2 == 1:
                    computer += 1
                    break
                elif computer2 == 2:
                    print("Draw. Again!\n")
                    sleep(1)
                elif computer2 == 3:
                    computer3000 += 1
                    break
            
            elif computer == 3:
                if computer2 == 1:
                    computer3000 += 1
                    break
                elif computer2 == 2:
                    computer += 1
                    break
                elif computer2 == 3:
                    print("Draw. Again!\n")
                    sleep(1)
        sleep(1)
        print(f"Computer chose: {computer1}; Computer3000 chose: {computer2}")
        sleep(1)

        print(f'\nComputer: {computer}; Computer3000: {computer3000}')
        sleep(1)
        return computer, computer3000

entrance = int(input("\nLet's play Rock Paper Scissors! Yes - 1 or No - 0: "))
sleep(1) 
if entrance == 0:
    exit("Okay. Good luck")
elif entrance == 1:
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



max_score = max(player, computer, computer3000)
if player == computer == computer3000:             # 1==2==3
    print("You should win back!\n")
    answer = 3
    player, computer, computer3000 = final(player, computer, computer3000, answer)
    max_score = max(player, computer, computer3000)

    if player == computer == max_score:                                  # 1==2 and 1>3
        print("You should win back again!")
        answer = 212
        player, computer = final(player, computer, None, answer)
        max_score = max(player, computer)

        if player == max_score:                               # 1==
            print("Congratulations! You took 1st place!")
        elif computer == max_score:                             # 2==
            print("You lost! The computer took 1st place. Congratulate him!")

    elif player == computer3000 == max_score:                        # 1==3 and 1>2
        answer = 213
        player, computer3000 = final(player, None, computer3000, answer)
        max_score = max(player, computer3000)

        if player == max_score:                           # 1==
            print("Congratulations! You took 1st place!")
        elif computer3000 == max_score:                         # 3==
            print("You lost! The computer took 1st place. Congratulate him!")

    elif computer == computer3000 == max_score:                          #2==3 > 1
        answer = 223
        computer, computer3000 = final(None, computer, computer3000, answer)
        max_score = max(computer, computer3000)

        if computer == max_score:                         #2==
            print("You lost! The computer took 1st place. Congratulate him!")
        elif computer3000 == max_score:                       #3==
            print("You lost! The computer3000 took 1st place. Congratulate him!")
    
    elif player == max_score:                               #1> 2 and 3
        print("Congratulations! You took 1st place!")
    
    elif computer == max_score:
        print("You lost! The computer took 1st place. Congratulate him!")

    elif computer3000 == max_score:
        print("You lost! The computer3000 took 1st place. Congratulate him!")

elif player == computer == max_score:                       # 1==2 and 1>3
    print("You should win back!")
    answer = 212
    player, computer = final(player, computer, None, answer)
    max_score = max(player, computer)

    if player == max_score:                                   # 1==
        print("Congratulations! You took 1st place!")
    elif computer == max_score:                                 # 2==
        print("You lost! The computer took 1st place. Congratulate him!")

elif player == computer3000 == max_score:                                # 1==3 and 1>2
    print("You should win back!")
    answer = 213
    player, computer3000 = final(player, None, computer3000, answer)
    max_score = max(player, computer3000)

    if player == max_score:                               # 1==
        print("Congratulations! You took 1st place!")
    elif computer3000 == max_score:                             # 3==
        print("You lost! The computer3000 took 1st place. Congratulate him!")

elif computer == computer3000 == max_score:                 #2==3 > 1
    print("You should win back!")
    answer = 223
    computer, computer3000 = final(None, computer, computer3000, answer)
    max_score = max(computer, computer3000)

    if computer == max_score:                             #2==
        print("You lost! The computer took 1st place. Congratulate him!")
    elif computer3000 == max_score:                           #3==
        print("You lost! The computer3000 took 1st place. Congratulate him!")

elif player == max_score:                                   #1> 2 and 3
        print("Congratulations! You took 1st place!")
    
elif computer == max_score:                                 #2> 1 and 3
    print("You lost! The computer took 1st place. Congratulate him!")

elif computer3000 == max_score:                             #3> 1 and 2
    print("You lost! The computer3000 took 1st place. Congratulate him!")


input("\nThank you for playing. Press Enter to exit...")