import pygame
from pygame.math import Vector2
from settings import *


STATUSES = ('idle', 'walk', 'jump', 'fall')


class Player(pygame.sprite.Sprite):
    animations: dict[str, list[pygame.Surface]]

    def __init__(self, topleft: tuple[int],
                 *groups: pygame.sprite.AbstractGroup,
                 colliders: pygame.sprite.AbstractGroup) -> None:
        """_summary_

        Args:
            topleft (tuple[int]): Character sprite starting position.
            *groups (tuple[AbstractGroup]): Sprite groups the player belongs to.
            colliders (AbstractGroup): Sprite group that can collide with player.

        Raises:
            Exception: If it was unable to load character's assets.
        """

        # creates the base character's sprite with Sprite class, and associates
        # it with its sprite groups
        super().__init__(*groups)

        # animation setup
        self.status = 'idle'
        self.frame_index = 0
        self.frame_speed = 0.25 / FPS

        if not self.load_assets():
            raise Exception('Error loading character assets')

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=topleft)

        # movement setup
        self.position = Vector2(topleft)
        self.direction = Vector2()

        self.move_speed = 4  # 250 px per sec (at 60 FPS)
        self.jump_speed = -12
        self.gravity = 0.8  # 50 px per sec (at 60 FPS)
        self.terminal_speed = 120  # before 165 ticks (2 seconds at 60 FPS)

        self.colliders = colliders

    def load_assets() -> bool:
        ...
