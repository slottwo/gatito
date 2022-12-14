import pygame
import sys
from settings import *
from level import Level


try:
    assert sys.version_info >= (3, 10)
except AssertionError:
    print('Unsupported Python version. Please, run with Python 3.10.x or newer')
    sys.exit(1)

class Game:
    def __init__(self) -> None:
        """Start and setup the Game. Init the game engine, set display, clock, 
        level...
        """

        # Pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption('Gatito')

        # Level setup
        self.level = Level(1)

    def run(self) -> None:
        """Start the game loop.
        """
        
        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # stop pygame
                    sys.exit(0)  # stop script

            self.screen.fill('#039ed9')  # draw a blue sky >i<
            self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
