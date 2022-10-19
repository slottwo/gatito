import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, topleft: tuple[int], groups: pygame.sprite.Group):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE,)*2)
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=topleft)

