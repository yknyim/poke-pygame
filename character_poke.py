import pygame

def main():
    width = 1000
    height = 800
    blank_color = (255, 255, 255)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    pikachu_image = pygame.image.load('../poke-pygame/images/pikachu.png').convert_alpha()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blank_color)

        # Game display
        screen.blit(pikachu_image, (450, 350))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
