# Pokemii Game

import pygame
import random
from os import path

width, height = 1050, 1050
fps = 60

# Define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)

# Set up assets folders
img_folder = path.join(path.dirname(__file__), 'img')

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pokemii!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game loop
running = True

while running:
    # keep loop running at the right speed
    clock.tick(fps)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Render (draw)
    screen.fill(black)
    all_sprites.draw(screen)

    # *after* drawing everthing, flip the display
    pygame.display.flip()

pygame.quit()