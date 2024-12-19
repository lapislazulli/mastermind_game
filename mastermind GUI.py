import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind Game")

# Colors (Pastel Versions)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 182, 193)
BLUE = (173, 216, 230)
GREEN = (144, 238, 144)
YELLOW = (255, 250, 205)
PURPLE = (216, 191, 216)
ORANGE = (255, 228, 181)
# Font
font = pygame.font.Font(None, 36)

# Game variables
palette = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
code = [random.choice(palette) for _ in range(4)]
current_guess = []
guesses = []
feedback = []

# Circle settings
CIRCLE_RADIUS = 20
PALETTE_Y = 500  # Y-coordinate for the color palette
GUESS_Y_START = 100  # Where guesses start
GAP_Y = 60  # Spacing between guess rows


# Function to draw the color palette
def draw_palette():
    # Draw each color circle for the palette
    for i in range(len(palette)):
        color = palette[i]
        x = 100 + i * 60
        pygame.draw.circle(screen, color, (x, PALETTE_Y), CIRCLE_RADIUS)
        pygame.draw.circle(screen, BLACK, (x, PALETTE_Y), CIRCLE_RADIUS, 2)  # Outline


# Function to draw guesses
def draw_guesses():
    # Loop through all guesses
    for guess_index in range(len(guesses)):
        guess = guesses[guess_index]
        for color_index in range(len(guess)):
            x = 200 + color_index * 60
            y = GUESS_Y_START + guess_index * GAP_Y
            pygame.draw.circle(screen, guess[color_index], (x, y), CIRCLE_RADIUS)

        # Draw feedback next to each guess
        feedback_text = font.render(feedback[guess_index], True, BLACK)
        screen.blit(feedback_text, (500, GUESS_Y_START + guess_index * GAP_Y))
        # Handle palette clicks to select colors
def handle_palette_click(pos):
    global current_guess
    for i in range(len(palette)):  # Loop through palette to see if a color is clicked
        x = 100 + i * 60
        y = PALETTE_Y
        if (pos[0] - x)*2 + (pos[1] - y)2 <= CIRCLE_RADIUS*2:
            if len(current_guess) < 4:  # Only allow 4 colors per guess
                current_guess.append(palette[i])

# Check if guess is valid and give feedback
def submit_guess():
    global current_guess, guesses, feedback
    if len(current_guess) == 4:  # Only submit when exactly 4 colors are selected
        guesses.append(current_guess[:])  # Add current guess to the list of guesses
        feedback.append(get_feedback(current_guess))
        if current_guess == code:  # Check if the guess matches the code
            feedback[-1] += " - You Win!"
        current_guess = []  # Clear the current guess


# Generate feedback for a guess
def get_feedback(guess):
    exact_matches = 0
    color_matches = 0

    # Check exact matches
    for i in range(len(code)):
        if guess[i] == code[i]:
            exact_matches += 1

    # Check color matches (ignoring exact matches)
    for color in palette:
        color_matches += min(guess.count(color), code.count(color))

    color_matches -= exact_matches
    return f"{exact_matches} correct, {color_matches} misplaced"
# Restart the game
def restart_game():
    global code, current_guess, guesses, feedback
    code = [random.choice(palette) for _ in range(4)]  # Create a new secret code
    current_guess = []
    guesses = []
    feedback = []
    # Main game loop
def main():
    clock = pygame.time.Clock()
    game_over = False

    while True:
        screen.fill(WHITE)

        # Draw the palette and guesses
        draw_palette()
        draw_guesses()

        # Draw the current guess at the top of the screen
        for i in range(len(current_guess)):
            x = 200 + i * 60
            pygame.draw.circle(screen, current_guess[i], (x, 50), CIRCLE_RADIUS)

        # Show "Game Over" message if the game is done
        if game_over:
            msg = font.render("Game Over! Press R to restart.", True, BLACK)
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT - 50))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # Handle mouse clicks
                handle_palette_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not game_over:  # Submit the guess
                    submit_guess()
                    if guesses and guesses[-1] == code:  # Check if the player won
                        game_over = True
                if event.key == pygame.K_r:  # Restart the game
                    restart_game()
                    game_over = False

        pygame.display.flip()
        clock.tick(60)


if _name_ == "_main_":
    main()