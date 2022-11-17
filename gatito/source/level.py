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

                match cell:
                    case '1':
                        Tile('water/top', (x,y), self.visible_sprites)
                    case '2':
                        Tile('water/bubbles', (x,y), self.visible_sprites)
                    case '3':
                        Tile('water/deep', (x,y), self.visible_sprites)
                    case '4':
                        Tile('grass/left', (x,y), self.visible_sprites, self.collision_sprites)
                    case '5':
                        Tile('grass/top', (x,y), self.visible_sprites, self.collision_sprites)
                    case '6': 
                        Tile('grass/right', (x,y), self.visible_sprites, self.collision_sprites)
                    case '7':
                        Tile('rock/left', (x,y), self.visible_sprites, self.collision_sprites)
                    case '8':
                        Tile('rock/right', (x,y), self.visible_sprites, self.collision_sprites)
                    case '9':
                        Tile('rock/full', (x,y), self.visible_sprites, self.collision_sprites)
                    case '10':
                        Tile('rock/bot_left_air', (x,y), self.visible_sprites, self.collision_sprites)
                    case '11':
                        Tile('rock/bot_right_air', (x,y), self.visible_sprites, self.collision_sprites)
                    case '12':
                        Tile('rock/bot_air', (x,y), self.visible_sprites, self.collision_sprites)
                    case '13':
                        Tile('rock/bot_left', (x,y), self.visible_sprites, self.collision_sprites)
                    case '14':
                        Tile('rock/bot_right', (x,y), self.visible_sprites, self.collision_sprites)
                    case '15':
                        Tile('rock/bot', (x,y), self.visible_sprites, self.collision_sprites)

    def run(self):

        # game logic
        self.active_sprites.update()

        # game graphics
        self.visible_sprites.draw(self.display_surface)
