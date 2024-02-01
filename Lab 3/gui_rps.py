# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Rock Paper Scissors Solo")

class Choice_Button(pygame.sprite.Sprite):
    def __init__(self, text):
        super(Choice_Button, self).__init__()
        self.surf = pygame.Surface((140, 60))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

        # Set up font
        self.font = pygame.font.Font(None, 36)
        self.text = text

        # Create a text surface and render the text on it
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        # Position the text in the center of the button
        text_rect = self.text_surface.get_rect(center=self.rect.center)

        # Blit the text surface onto the button surface
        self.surf.blit(self.text_surface, text_rect)

rock_choice = Choice_Button("Rock")
paper_choice = Choice_Button("Paper")
scissor_choice = Choice_Button("Scissors")

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    # Draw the player on the screen
    surf_center = (
    (SCREEN_WIDTH - rock_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - rock_choice.surf.get_height()) / 2
    )
    screen.blit(rock_choice.surf, surf_center)

    surf_center = (
    (SCREEN_WIDTH - 5 * paper_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - paper_choice.surf.get_height()) / 2
    )
    screen.blit(paper_choice.surf, surf_center)

    surf_center = (
    (SCREEN_WIDTH + 3 * scissor_choice.surf.get_width()) / 2,
    (SCREEN_HEIGHT - scissor_choice.surf.get_height()) / 2
    )
    screen.blit(scissor_choice.surf, surf_center)
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()