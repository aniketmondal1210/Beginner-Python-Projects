# Guess the random number game in Python
'''
-> random no = assuming
-> user input = guess no
-> guess > random no = greater than guess, please try again
-> guess < random no = less than guess, please try again
-> guess == random no = won!
-> count = tries = result
'''

#guess
import random
n = int(input())
guess = random.randint(1,n+1)

#vars
counter  = 0
user_guess = None

#greet
print("Welcome to number guessing game.")
print("I have thought of a number between 1 and",n,"can you guess it?")

while user_guess != guess:
    user_guess = int(input("Enter your guessed number: "))
    counter+=1 #counter = counter + 1

    #logic
    if (user_guess < guess):
        print("Less than original guess, please try again!")
    elif (user_guess < guess):
        print("More than original guess, please try again!")
    else:
        print("You won the game in",counter,"attempts!")
    