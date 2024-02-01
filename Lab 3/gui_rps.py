# Import and initialize the pygame library
import time
import random
import pygame
from pygame.locals import (
    K_r,
    K_p,
    K_s
)

pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Rock Paper Scissors Solo")

class Choice_Button(pygame.sprite.Sprite):
    def __init__(self, text):
        super(Choice_Button, self).__init__()
        self.surf = pygame.Surface((190, 90))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        # Set up font
        self.font = pygame.font.Font(None, 28)
        self.text = text

        # Create a text surface and render the text on it
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        # Position the text in the center of the button
        text_rect = self.text_surface.get_rect(center=self.rect.center)

        # Blit the text surface onto the button surface
        self.surf.blit(self.text_surface, text_rect)

def rps(player_choice, rps_bot_choice):
    win_message = ""

    if player_choice == rps_bot_choice:
        win_message = "TIE"
    elif player_choice == "rock":
        if rps_bot_choice == "paper":
            win_message = "RPS Bot WINS"
        else:
            win_message = "Player WINS"
    elif player_choice == "paper":
        if rps_bot_choice == "scissors":
            win_message = "RPS Bot WINS"
        else:
            win_message = "Player WINS"
    elif player_choice == "scissors":
        if rps_bot_choice == "rock":
            win_message = "RPS Bot WINS"
        else:
            win_message = "Player WINS"
    
    return win_message

def draw_choice_buttons():    
    rock_choice = Choice_Button("Rock (Press R)")
    paper_choice = Choice_Button("Paper (Press P)")
    scissor_choice = Choice_Button("Scissors (Press S)")

    surf_center = (
    (SCREEN_WIDTH - 4 * rock_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - rock_choice.surf.get_height()) / 2
    )
    screen.blit(rock_choice.surf, surf_center)

    surf_center = (
    (SCREEN_WIDTH - paper_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - paper_choice.surf.get_height()) / 2
    )
    screen.blit(paper_choice.surf, surf_center)

    surf_center = (
    (SCREEN_WIDTH + 2 * scissor_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - scissor_choice.surf.get_height()) / 2
    )
    screen.blit(scissor_choice.surf, surf_center)

def draw_rps(player_choice, rps_bot_choice):
    image_path = f"./{player_choice}.jpg"  # Replace with the path to your image file
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (250, 250))
    screen.blit(image, (50, 120))
    # Set up font
    font = pygame.font.Font(None, 38)
    text = "Player"
    # Create a text surface and render the text on it
    text_surface = font.render(text, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(160, 100))
    screen.blit(text_surface, text_rect)


    text = "VS"
    # Create a text surface and render the text on it
    text_surface = font.render(text, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(400, 200))
    screen.blit(text_surface, text_rect)

    image_path = f"./{rps_bot_choice}.jpg"  # Replace with the path to your image file
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (250, 250))
    screen.blit(image, (500, 120))
    text = "RPS Bot"
    # Create a text surface and render the text on it
    text_surface = font.render(text, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(630, 100))
    screen.blit(text_surface, text_rect)

    win_font = pygame.font.Font(None, 80)
    win_message = rps(player_choice, rps_bot_choice)
    # Create a text surface and render the text on it
    text_surface = win_font.render(win_message, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(400, 400))
    screen.blit(text_surface, text_rect)

choosing_mode = True
player_choice = ""
rps_random_seed = random.randint(0, 2)
match rps_random_seed:
    case 0:
        rps_bot_choice = "rock"
    case 1:
        rps_bot_choice = "paper"
    case 2:
        rps_bot_choice = "scissors"

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_r]:
            print("rock")
            player_choice = "rock"
            choosing_mode = False
        elif pressed_keys[K_p]:
            print("paper")
            player_choice = "paper"
            choosing_mode = False
        elif pressed_keys[K_s]:
            print("scissors")
            player_choice = "scissors"
            choosing_mode = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # Draw the player on the screen
    
    if (choosing_mode):
        draw_choice_buttons()
    else:
        draw_rps(player_choice, rps_bot_choice)
        #choosing_mode = True

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()