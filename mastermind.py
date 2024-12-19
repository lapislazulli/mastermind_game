import random

# The colors for the game
colors = ['Y', 'B', 'R', 'G', 'O', 'N']  # Yellow, Blue, Red, Green, Orange, Black
code = []

# Generate the secret code
while len(code) < 4:
    picked_color = random.choice(colors)  # Pick a random color
    code.append(picked_color)  # Add the color to the code

print("Welcome to Mastermind!")
print("Colors you can choose: Y (Yellow), B (Blue), R (Red), G (Green), O (Orange), N (Black)")
print("Try to guess the secret code of 4 colors.")
print("For example: Y B G R")
print("You have 10 attempts. Good luck!")

# Variables for the game
attempts = 10
current_attempt = 1
# Start the game loop
while current_attempt <= attempts:
    print("\nAttempt", current_attempt, "out of", attempts)
    guess = input("Enter your guess (4 colors separated by spaces): ").strip().split()

    # Check the length of the guess
    if len(guess) != 4:
        print("Error: You must guess exactly 4 colors!")
        continue