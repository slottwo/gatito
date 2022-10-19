import pygame
import sys
from settings import *
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gatito')
clock = pygame.time.Clock()

if __name__ == '__main__':
    level = Level()

    # event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BG_COLOR)
        level.run()

        # drawing logic
        pygame.display.update()
        clock.tick(60)
