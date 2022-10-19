import pygame, os
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int], *groups: pygame.sprite.Group):
        super().__init__(groups)
        
        # image = pygame.image.load('gatito/assets/sprite.png')
        # self.size = (40, 64)
        # self.image = pygame.transform.scale(image, self.size)
        
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=topleft)


