import sys
from random import randint

# generate 1-10
answer = randint(1, 10)
# get input from user

# check if input is 1-10
while True:
    try:
        guess = int(input("guess a number from 1 - 10? "))
        if 0 < guess < 11:
            if guess == answer:
                print("fabulous")
                break
        else:
            print("Hey, told you to enter from 1 -10")
    except ValueError:
        print("Enter the number only")
        continue
# check if num is right or enter again.





