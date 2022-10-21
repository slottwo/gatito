import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self) -> None:
        """Generate and setup the game settings: Display, level, clock...
        """
        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Gatito')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        """Start the game loop, run the level and update the display.
        """

        # event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BG_COLOR)
            self.level.run()

            # drawing logic
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
