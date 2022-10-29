import pygame
from settings import *
# from debug import debug
from tile import Tile
from player import Player


class Level:
    def __init__(self, level_map: list[str] = TILE_MAP) -> None:
        """Create and load the entire game (level)
        Args:
            level_map (list[str], optional): Matrix of tile and entities. Defaults to LEVEL_MAP.
        """

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level(level_map)

    def setup_level(self, level_map: list[str]) -> None:
        """Instantiate and associate the tiles and entities

        Args:
            level_map (list[str]):  Matrix of tiles and entities on in their respective positions.
        """

        for line_row, row in enumerate(level_map):
            y = line_row * TILE_SIZE
            for column_index, cell in enumerate(row):
                x = column_index * TILE_SIZE

                if cell == '1':
                    Tile((x,y), self.visible_sprites, self.collision_sprites)

    def run(self):

        # game logic
        self.active_sprites.update()

        # game graphics
        self.visible_sprites.draw(self.display_surface)
