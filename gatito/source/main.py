import pygame
import sys
import time
from settings import *
from level import Level
from debug import debug
from player import Player


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

        # pick the player sprite for debug
        player: Player = None
        for sprite in self.level.active_sprites.sprites():
            if type(sprite) == Player:
                player = sprite
                break

        print(*player.rect.size)

        previous_frame = 0
        previous_x = player.position.x
        previous_y = player.position.y

        # initial time
        previous_time = time.perf_counter()

        # event loop
        while True:
            delta_time = time.perf_counter() - previous_time
            previous_time = time.perf_counter()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BG_COLOR)
            self.level.run()

            # debug

            # frame_velocity = (player.frame_index - previous_frame) / delta_time
            # previous_frame = player.frame_index

            player_velocity_x = (player.position.x - previous_x) / delta_time
            previous_x = player.position.x
            player_velocity_y = (player.position.y - previous_y) / delta_time
            previous_y = player.position.y

            debug('x:', round(player.position.x, 3),
                  'y:', round(player.position.y, 3))
            debug(player.status, y=2)
            debug('dt:', round(delta_time, 3), y=3)
            debug('dx/dt:', round(player_velocity_x), y=4)
            debug('dy/dt:', round(player_velocity_y), y=5)
            debug('x/tick:', round(player.direction.x), y=6)
            debug('y/tick:', round(player.direction.y), y=7)

            # drawing logic
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
