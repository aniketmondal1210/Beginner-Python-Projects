import random
 
# The computer selects a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Guess the secret number between 1 and 100!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {guess} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
