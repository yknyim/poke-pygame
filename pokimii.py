import pygame

def main():
    width = 512
    height = 480
    background = pygame.image.load('../poke-pygame/images/bg.png')

    pygame.mixer.init()
    sound = pygame.mixer.Sound('../poke-pygame/sounds/ViridianF.wav')

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pokimii')
    clock = pygame.time.Clock()

    # Game initialization
    pikachu_image = pygame.image.load('../poke-pygame/images/pikachu.png').convert_alpha()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound.play()
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.blit(background, [0,0])

        # Game display
        screen.blit(pikachu_image, (203, 200))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
