import pygame
# from debug import debug
from map import Map
from tile import Tile
from item import Item
from player import Player
from settings import *


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
            level_id: ...
        """
        self.map = Map(level_id, self)
        for layer in self.map.data['layers']:
            if layer['visible']:
                if layer['type'] == 'tilelayer':
                    for index, id in enumerate(layer['data']):
                        if TILE_DICT[id][0] == 'water':
                            Tile(TILE_DICT[id],
                                 (int(index % SCREEN_WIDTH) * TILE_SIZE,
                                 int(index / SCREEN_WIDTH) * TILE_SIZE),
                                 self.visible_sprites,
                                 opacity=layer['opacity'])
                        else:
                            Tile(TILE_DICT[id],
                                 (int(index % SCREEN_WIDTH) * TILE_SIZE,
                                 int(index / SCREEN_WIDTH) * TILE_SIZE),
                                 self.collision_sprites, self.visible_sprites,
                                 opacity=layer['opacity'])
                elif layer['type'] == 'objectgroup':
                    for entity in layer['objects']:
                        if entity['class'] == 'Cloud':
                            ...
                        if entity['class'] == 'CloudPinky':
                            ...
                        if entity['class'] == 'Fish':
                            Item('fish', (entity['x'], entity['y']), 8,
                                 self.visible_sprites, 
                                 self.collision_sprites)
                        if entity['class'] == 'Player':
                            Player((entity['x'], entity['y']),
                                   self.visible_sprites, 
                                   self.collision_sprites)

    def run(self):

        # game logic
        self.active_sprites.update()

        # game graphics
        self.visible_sprites.draw(self.display_surface)
