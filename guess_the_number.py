import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

for guessTaken in range(1, 7): 
    print("Guess a number! ")
    guess = int(input())
    
   
    if guess < secret_number: 
        print("The number that you entered is lower than what I am thinking")

    elif guess > secret_number: 
        print("The number is higher than what I am thinking")
    else: 
        break 

if guess == secret_number: 
    print("Good Job you guess the number in ", guessTaken," times!")
else: 
    print("you didn't guess the number correctly, the number was", secret_number )


