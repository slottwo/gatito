import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self) -> None:

        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        self.setup_level()
    
    
    def setup_level(self):
        for row_index, row in enumerate(LEVEL_MAP):
            y = row_index * TILE_SIZE
            for column_index, column in enumerate(row):
                x = column_index * TILE_SIZE
                
                match column:
                    case 'P':
                        Player((x,y), self.visible_sprites, self.active_sprites)
                    case 'X':
                        Tile((x,y), self.visible_sprites)



    def run(self):
        # run the entire game (level)
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
