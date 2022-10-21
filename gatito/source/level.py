import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self, level_map: list[str] = LEVEL_MAP) -> None:
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
        """Load the level map

        Args:
            level_map (list[str]): An matrix with the initial position of tiles and entities
        """

        for row_index, row in enumerate(level_map):
            y = row_index * TILE_SIZE
            for column_index, column in enumerate(row):
                x = column_index * TILE_SIZE

                match column:
                    case 'P':
                        Player((x, y),
                               self.visible_sprites, self.active_sprites,
                               colliders=self.collision_sprites)
                    case 'X':
                        Tile((x, y), self.visible_sprites,
                             self.collision_sprites)

    def run(self):
        """Run the entire game (level).
        """

        # Game logic
        self.active_sprites.update()

        # Game graphics
        self.visible_sprites.draw(self.display_surface)
