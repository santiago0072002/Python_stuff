import random
# another way we can write this import is from random import randint

random_num = random.randint(0,100)# this means that I am going to get a random 
# number inside the method first val is the number that i want to guess from 
# and the second number will be up to that number inclusive
go = True
while go is True:
    guess = int(input("please try to guess my number"))
    if guess == random_num:
        go = False
    elif guess < random_num:
        print("that Number is lower")
    else:
        print("that number is higher")
print(f"you guessed your number and it is: {random_num}")