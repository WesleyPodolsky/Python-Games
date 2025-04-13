"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame

# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'
BLUE = (0, 0, 255)
colors = ['blue','red', 'yellow', 'green', 'pink', 'orange']
# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tiled Background')

def make_tiled_bg(screen, bg_file):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    
    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image

background = make_tiled_bg(screen, assets/'background_tile.gif')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color_surface = pygame.Surface((100,600)) 
    

    screen.blit(background,(0,0))

    for i in range(7):
        screen.blit(color_surface,((i-1)*100, 0))
        chosen_color = colors[i-1]
        color_surface.fill(chosen_color)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
