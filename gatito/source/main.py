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

        previous_frame = 0
        previous_x = player.position.x

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
            self.level.run(delta_time)

            # debug

            # frame_velocity = (player.frame_index - previous_frame) / delta_time
            # previous_frame = player.frame_index

            player_velocity_x = (player.position.x - previous_x) / delta_time
            previous_x = player.position.x

            debug('x:', round(player.position.x, 3), 'y:', player.position.y)
            debug(player.status, y=24)
            debug('dt:', round(delta_time, 3), y=36)
            debug('dx/dt:', round(player_velocity_x), y=48)

            # drawing logic
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
