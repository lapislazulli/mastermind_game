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
     # Check if all colors in the guess are valid
    invalid_guess = False
    for color in guess:
        if color not in colors:
            print("Error:", color, "is not a valid color! Choose from", ", ".join(colors))
            invalid_guess = True
            break
    if invalid_guess:
        continue

    # Compare the guess with the secret code
    correct_position = 0
    correct_color = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:  # Correct color in the correct position
            correct_position += 1
        elif guess[i] in code:  # Correct color but wrong position
            correct_color += 1
               # Give feedback to the player
    print("Correct colors in the right position (*):", correct_position)
    print("Correct colors in the wrong position (-):", correct_color)

    # Check if the player has won
    if correct_position == 4:
        print("Congratulations! You guessed the code:", " ".join(code))
        break

    # Increment the attempt
    current_attempt += 1

# If the player runs out of attempts
if current_attempt > attempts:
    print("Game over! The secret code was:", " ".join(code))
