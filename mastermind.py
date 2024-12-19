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