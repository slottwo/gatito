import pygame
from pygame.math import Vector2
from settings import *
from sprite_strip_anim import SpriteStripAnim


ASSETS_PATH = 'gatito/assets/sprites/cat/'


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

        self.animations = self.load_assets()

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

    def load_assets() -> dict[str, SpriteStripAnim]:
        """_summary_

        Returns:
            dict[str, SpriteStripAnim]: _description_
        """

        return {
            'idle': SpriteStripAnim(ASSETS_PATH + 'idle', (0, 0, 16, 16), True),
            'walk': SpriteStripAnim(ASSETS_PATH + 'walk', (0, 0, 16, 16), True),
            'jump_in': SpriteStripAnim(ASSETS_PATH + 'jump_in', (0, 0, 16, 16)),
            'jump': SpriteStripAnim(ASSETS_PATH + 'jump', (0, 0, 16, 16), True),
            'fall': SpriteStripAnim(ASSETS_PATH + 'fall', (0, 0, 16, 16), True),
            'fall_out': SpriteStripAnim(ASSETS_PATH + 'fall_out', (0, 0, 16, 16))
        }
