import pygame
from settings import *
from tools import loadmap
# from debug import debug
from tile import Tile
from item import Item
from player import Player
from item import Item


class Level:
    def __init__(self, level_id: int) -> None:
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

        self.setup_level(level_id)

    def setup_level(self, level_id: int) -> None:
        """Instantiate and associate the tiles and entities

        Args:
            level_map (list[str]):  Matrix of tiles and entities on in their respective positions.
        """

        level_map = loadmap(level_id)

    def run(self):

        # game logic
        self.active_sprites.update()

        # game graphics
        self.visible_sprites.draw(self.display_surface)
