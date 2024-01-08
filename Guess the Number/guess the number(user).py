import random
 
def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        try:
            user_guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess < random_number:
            print('Sorry, guess again. Too low.')
        elif user_guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  # could also be high b/c low = high
        feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1

    print(f'Yay! The computer guessed your number, {computer_guess}, correctly!')

# Example usage:
computer_guess(10)
