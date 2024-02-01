# Import and initialize the pygame library
import ast
import time
import paho.mqtt.client as mqtt
import random
import pygame
from pygame.locals import (
    K_r,
    K_p,
    K_s,
    K_SPACE
)

win_message = ""
mode = "choosing"

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("rps/server", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
# The default message callback.
# (you can create separate callbacks per subscribed topic)

def on_message(client, userdata, message):
    message = message.payload.decode()
    global win_message
    win_message = message
    print(f"Recieved Message: {message}")
    global mode
    mode = "result"

# 1. create a client instance.
client = mqtt.Client()

# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async("mqtt.eclipseprojects.io")
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

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

def draw_waiting():
    font = pygame.font.Font(None, 40)
    text = "Waiting for server response..."
    # Create a text surface and render the text on it
    text_surface = font.render(text, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(400, 300))
    screen.blit(text_surface, text_rect)

def determine_win(win_message):
    result_list = win_message.split("|")
    win_message = result_list[0]
    choices = ast.literal_eval(result_list[1])
    
    if player_choice == win_message and choices[0] == choices[1]:
        win_message = "TIE!"
    elif player_choice != win_message:
        win_message = "YOU LOST!"
    else:
        win_message = "YOU WON!"
    
    return (win_message + " (Press SPACE to play again!)", choices)

def draw_rps(win_message, choices):
    image_path = f"./{choices[0]}.jpg"  # Replace with the path to your image file
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (250, 250))
    screen.blit(image, (50, 120))
    # Set up font
    font = pygame.font.Font(None, 38)
    text = "Player 1"
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

    image_path = f"./{choices[1]}.jpg"  # Replace with the path to your image file
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (250, 250))
    screen.blit(image, (500, 120))
    text = "Player 2"
    # Create a text surface and render the text on it
    text_surface = font.render(text, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(630, 100))
    screen.blit(text_surface, text_rect)

    win_font = pygame.font.Font(None, 50)
    # Create a text surface and render the text on it
    text_surface = win_font.render(win_message, True, (0, 0, 0))
    # Position the text in the center of the button
    text_rect = text_surface.get_rect(center=(400, 450))
    screen.blit(text_surface, text_rect)

player_choice = ""
rps_bot_choice = ""

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if mode == "choosing":
                if event.key == K_r:
                    player_choice = "rock"
                    client.publish("rps", player_choice, qos=1)
                    mode = "waiting"
                    print("rock")
                if event.key == K_p:
                    player_choice = "paper"
                    client.publish("rps", player_choice, qos=1)
                    choosing_mode = "waiting"
                    print("paper")
                if event.key == K_s:
                    player_choice = "scissors"
                    client.publish("rps", player_choice, qos=1)
                    mode = "waiting"
            elif event.key == K_SPACE and mode == "result":
                mode = "choosing"
                player_choice = ""

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # Draw the player on the screen
    
    if mode == "choosing":
        draw_choice_buttons()
    elif mode == "waiting":
        draw_waiting()
    elif mode == "result":
        winner, choices = determine_win(win_message)
        draw_rps(winner, choices)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()