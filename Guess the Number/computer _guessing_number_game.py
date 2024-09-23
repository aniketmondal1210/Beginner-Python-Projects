low = 1
high = 100
attempts = 0

print("Think of a number between 1 and 100, and I'll try to guess it!")

while True:
    attempts += 1
    guess = (low + high) // 2  # Computer guesses the middle number
    print(f"My guess is {guess}.")
    
    # Get feedback from the user
    response = input("Is it too high (H), too low (L), or correct (C)? ").upper()

    if response == 'H':
        high = guess - 1  # Adjust the range down
    elif response == 'L':
        low = guess + 1   # Adjust the range up
    elif response == 'C':
        print(f"I guessed your number in {attempts} attempts!")
        break
    else:
        print("Please enter H for high, L for low, or C for correct.")
