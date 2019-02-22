import pygame, sys
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../poke-pygame/images/pikachu.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = pos

def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    background = pygame.image.load('../poke-pygame/images/VForest.png')
    size =[1050, 1050]
    pygame.mixer.init()
    sound = pygame.mixer.Sound('../poke-pygame/sounds/ViridianF.wav')
    sound.play()

    screen = pygame.display.set_mode(size)

    player = Block([185, 160])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 8
    player.vy = 8


    wall = Block([570, 1080])

    wall_group = pygame.sprite.Group()
    wall_group.add(wall)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]

        screen.blit(background, [-12,-12])

        # first parameter takes a single sprite
        # second parameter takes sprite groups
        # third parameter is a do kill commad if true
        # all group objects colliding with the first parameter object will be
        # destroyed. The first parameter could be bullets and the second one
        # targets although the bullet is not destroyed but can be done with
        # simple trick bellow
        hit = pygame.sprite.spritecollide(player, wall_group, True)

        if hit:
            # if collision is detected call a function in your case destroy
            # bullet
            # player.image.fill((255, 255, 255))
            pygame.display.set_caption('You Win!')
            size = [1050, 1050]
            screen = pygame.display.set_mode(size)
            
            clock = pygame.time.Clock()
            
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('PIKA PIKA OVER!', True, (255, 255, 255), (0, 0, 0))
            textrect = text.get_rect()
            textrect.centerx = screen.get_rect().centerx
            textrect.centery = screen.get_rect().centery
            
            screen.blit(background, [-12,-12])
            screen.blit(text, textrect)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        # sys.exit()
                clock.tick(20)


        player_group.draw(screen)
        wall_group.draw(screen)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()