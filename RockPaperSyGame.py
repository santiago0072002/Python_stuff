import random, sys

print("ROCK, PAPER, SCISSORS")

# variables to keep track of win, lose, or ties

wins = 0 
losses = 0 
ties = 0 

while True: 
    print(f"wins {wins}, losses {losses}, ties{ties}")
    while True: 
        print("enter your move : r for rock, p for paper, s for sissors or q to quit")
        player_move = input()
        if player_move == "q": 
            sys.exit()
        if player_move == "r" or player_move == "s" or player_move == "p":
            break
    if player_move == "r":
        print("rock vs...")
    elif player_move == "p":
        print("paper vs...")
    elif player_move == "s": 
        print("scissors vs ...")
    # this is what the computer picked 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1: 
        computer_move = "r"
        print("ROCK!")
    elif randomNumber == 2: 
        computer_move = "p"
        print("PAPER!")
    elif randomNumber == 3: 
        computer_move = "s"
        print("SCISSORS!")

    if player_move == computer_move: 
        print("it is a TIE!")
        ties += 1
    elif player_move == "r" and computer_move == "s": 
        print("You Win!")
        wins += 1 
    elif player_move == "p" and computer_move == "r": 
        print("You Win!")
        wins += 1 
    elif player_move == "s" and computer_move == "p": 
        print("You Win!")
        wins += 1
    elif player_move == "r" and computer_move == "p": 
        print("Computer Win!")
        losses+= 1
    elif player_move == "p" and computer_move == "s": 
        print("Computer Win!")
        losses+= 1
    elif player_move == "s" and computer_move == "r": 
        print("Computer Win!")
        losses+= 1
    if wins == 3 or losses == 3: 
        print("You scored!", wins, "the computer scored!", losses)
        if wins > losses: 
            print("You Win!")
        else: 
            print("The Computer won!")
        sys.exit()
