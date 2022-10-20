from turtle import speed
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

        # move player
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = 16
        self.gravity = 0.8
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.direction.y = -self.jump_speed
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.apply_gravity()
